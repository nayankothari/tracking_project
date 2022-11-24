from django.db import models
from accounts.models import Pincode, CNoteHistory, BookingType
from accounts.models import RefrenceCourier, Country, Pincode
from django.contrib.auth.models import User


class RouteMaster(models.Model):
    area_name = models.CharField(max_length=250)
    pincode = models.ForeignKey(Pincode, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Route Master"

    def __str__(self):        
        return "{0.area_name}-{0.pincode}".format(self)


class DeliveryBoy(models.Model):
    delivery_boy_name = models.CharField(max_length=120)
    mobile_number = models.BigIntegerField()
    alternate_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField()
    area_name = models.ForeignKey(RouteMaster, on_delete=models.CASCADE)
    pincode = models.ForeignKey(Pincode, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = "Delivery Boy Master"
    
    def __str__(self):
        return self.delivery_boy_name


class PartyMaster(models.Model):
    party_name = models.CharField(max_length=256)
    in_person_name = models.CharField(max_length=256)
    mobile_number = models.BigIntegerField()    
    alternate_numnber = models.BigIntegerField(blank=True)
    email = models.EmailField(blank=True)
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=30)
    party_address = models.TextField(blank=True)
    is_gst_enabled_party = models.BooleanField(default=False)
    gst_number = models.CharField(max_length=15, blank=True)
    remarks = models.TextField(blank=True)
    opening_balance = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)            
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Party Master"
    
    def __str__(self):
        return self.party_name    


class PaymentMaster(models.Model):
    payment_type = models.CharField(max_length=250)
    opening_balance = models.FloatField()
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)       

    class Meta:
        verbose_name_plural = "Payment Master"
    
    def __str__(self):
        return self.payment_type    

class Booking(models.Model):
    c_note_number = models.OneToOneField(CNoteHistory, on_delete=models.CASCADE)
    booking_type = models.ForeignKey(BookingType, on_delete=models.CASCADE)
    refernce_courier_name = models.ForeignKey(RefrenceCourier, on_delete=models.CASCADE)
    reference_courier_number = models.CharField(max_length=25)
    payment_mode = models.CharField(max_length=30)
    booking_datetime = models.DateTimeField()
    consignor_name = models.ForeignKey(PartyMaster, on_delete=models.CASCADE)
    consignor_mobile_number = models.BigIntegerField(blank=False)
    consignor_address = models.TextField()
    consignor_gst_number = models.CharField(max_length=16)
    consignee_name = models.CharField(max_length=250)
    consignee_mobile_number = models.BigIntegerField(blank=False)
    consignee_address = models.TextField()
    consignee_gst_number = models.CharField(max_length=16)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=256)
    pincode = models.ForeignKey(Pincode, on_delete=models.CASCADE)
    weight_in_gms = models.FloatField()
    charge_weight = models.FloatField()
    declare_value = models.FloatField()
    risk_coverage_charges = models.FloatField()
    apply_gst = models.BooleanField(default=False)
    tax_percentage = models.FloatField()
    tax_amount = models.FloatField()
    hsn_number = models.CharField(max_length=15)
    courier_charges = models.FloatField()
    fuel_charges = models.FloatField()
    insurance_charges = models.FloatField()
    other_charges = models.FloatField()
    to_pay = models.BooleanField(default=False)
    to_pay_amount = models.FloatField()    
    booking_last_status = models.CharField(max_length=256)
    remarks = models.TextField()
    status = models.BooleanField(default=True)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Booking Master"
    
    def __str__(self):
        return self.c_note_number    


class LoadOutWard(models.Model):    
    lot_no = models.BigIntegerField()
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_destination = models.CharField(max_length=256)
    to_destination = models.CharField(max_length=256)
    additional_mainifest_no = models.CharField(max_length=30)
    c_note_number = models.BigIntegerField()    
    document_destination = models.CharField(max_length=30)
    consignee_name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)       

    class Meta:
        verbose_name_plural = "Load Outward"
    
    def __str__(self):
        return "{0.created_at} - {0.to_destination}".format(self)
    

class LoadInWard(models.Model):
    c_note_number = models.BigIntegerField()
    consignee_name = models.CharField(max_length=256)
    document_destination = models.CharField(max_length=30)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_mainifest_no = models.CharField(max_length=30)    
    received_by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_by_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)       

    class Meta:
        verbose_name_plural = "Load Inward"
    
    def __str__(self):
        return "{0.updated_at} - {0.from_user}".format(self)


class GenerateDrs(models.Model):
    drs_number = models.BigIntegerField()
    load_number = models.CharField(max_length=200)
    drs_date = models.DateTimeField()
    area_name = models.ForeignKey(RouteMaster, on_delete=models.CASCADE)
    delivery_boy = models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)
    c_note_numbetr = models.BigIntegerField()
    from_center = models.CharField(max_length=256)
    receiver = models.CharField(max_length=256)
    method = models.ForeignKey(BookingType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Generate DRS"
    
    def __str__(self):
        return "{0.drs_number} - {0.drs_date}".format(self)


class UploadDrs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drs_no = models.BigIntegerField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        verbose_name_plural = "Upload DRS."
    
    def __str__(self):
        return "{0.drs_no}".format(self)


class DocumentHistory(models.Model):
    c_note_number = models.BigIntegerField()
    from_destination = models.CharField(max_length=256)
    to_center = models.CharField(max_length=256)
    booking_datetime = models.DateTimeField()
    consignee = models.CharField(max_length=256)
    current_status = models.CharField(max_length=25)
    status_date = models.DateTimeField()
    tracking_status = models.CharField(max_length=256)
    from_user = models.ForeignKey(User, on_delete=models.PROTECT)
    to_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="to_user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        verbose_name_plural = "Treacking history"
    
    def __str__(self):
        return "{0.c_note_number}".format(self)

