from django import utils    
from django.db import models
from django.db.models import Max
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


def return_max_cnote_number(*args, **kwargs):    
    data = CNoteMaseter.objects.aggregate(Max('c_note_end'))            
    if not data.get("c_note_end__max"):
        return 111150001
    else:
        return data.get("c_note_end__max") + 1

class Country(models.Model):
    country_name = models.CharField(max_length=100, blank=False, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name
    class Meta:
        verbose_name_plural = "Country"

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.CharField(max_length=150, blank=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "State"
    
    def __str__(self):
        return self.state

class District(models.Model):
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.CharField(max_length=150, blank=False)    
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "District"    
    
    def __str__(self):
        return self.district

class Pincode(models.Model):
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    pincode = models.BigIntegerField(blank=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     

    class Meta:
        verbose_name_plural = "Pincode"
    
    def __str__(self):
        return str(self.pincode)

class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 254, blank=True)
    user_business_name = models.CharField(max_length=254)
    mobile_number = models.BigIntegerField(blank=False)
    alternate_mobile_number = models.CharField(max_length=15, blank=False)    
    owner_name = models.CharField(max_length=150)    
    address = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    Pincode = models.ForeignKey(Pincode, on_delete=models.CASCADE)
    business_status = models.BooleanField(default=True)
    is_gst_enabled_user = models.BooleanField(default=False)
    gst_number = models.CharField(max_length=15, blank=True)
    remarks = models.TextField()
    user_status = models.BooleanField(default=True)
    licence_expire = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.user.username

class CNoteHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_note_number = models.BigIntegerField(blank=False, unique=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "C Note history"
        # ordering = ["id"]
    
    def __str__(self):
        return str(self.c_note_number)

class CNoteMaseter(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_note_start = models.BigIntegerField(blank=False, default=return_max_cnote_number)
    c_note_end = models.BigIntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "C. Note master"    
    
    def __str__(self):
        return self.user.username   

class RefrenceCourier(models.Model):
    courier_name = models.CharField(max_length=254)
    link = models.TextField()
    type = models.CharField(max_length=60, choices=[("External", "External"), ("Internal", "Internal")],
        default="External")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "Refrence courier"

    def __str__(self):
        return self.courier_name

class BookingType(models.Model):
    booking_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Booking type"
    
    def __str__(self):
        return self.booking_type

class ReturnReason(models.Model):
    return_reason = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "Return reason"
    
    def __str__(self):
        return self.return_reason


# Django Signals 
def c_note_pre_save(sender, instance, *args, **kwargs):        
    if instance.c_note_end > instance.c_note_start:
        ...
    else:        
        raise Exception('OMG')

def c_note_post_save(sender, instance, *args, **kwargs):                    
    data = [
        CNoteHistory(
            user=instance.user,
            c_note_number=i,
            status=False,
        )
        for i in range(instance.c_note_start, instance.c_note_end + 1)]
    CNoteHistory.objects.bulk_create(data)            

pre_save.connect(c_note_pre_save, sender=CNoteMaseter)
post_save.connect(c_note_post_save, sender=CNoteMaseter)