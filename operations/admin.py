from django.contrib import admin
from .models import DeliveryBoy, RouteMaster, PartyMaster, UploadDrs
from .models import PaymentMaster, Booking, LoadInWard, LoadOutWard
from .models import GenerateDrs, DocumentHistory


class DateTimeDisplay(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at",)


admin.site.register(RouteMaster, DateTimeDisplay)
admin.site.register(DeliveryBoy, DateTimeDisplay)
admin.site.register(PartyMaster, DateTimeDisplay)
admin.site.register(PaymentMaster, DateTimeDisplay)
admin.site.register(Booking, DateTimeDisplay)
admin.site.register(LoadOutWard, DateTimeDisplay)
admin.site.register(LoadInWard, DateTimeDisplay)
admin.site.register(UploadDrs, DateTimeDisplay)
admin.site.register(GenerateDrs, DateTimeDisplay)
admin.site.register(DocumentHistory, DateTimeDisplay)