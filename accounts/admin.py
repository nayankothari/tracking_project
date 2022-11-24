from django.contrib import admin
from .models import Country, State, District, Pincode, Accounts, CNoteHistory
from .models import CNoteMaseter, BookingType, RefrenceCourier, ReturnReason


admin.site.site_header = "Airship Express"
admin.site.site_title = "Airship Express"
admin.site.index_title = "Admin portal"

class CNoteMaseterAdmin(admin.ModelAdmin):
    readonly_fields = ('c_note_start',)

class CNoteHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at",)

admin.site.register(Country, CNoteHistoryAdmin)
admin.site.register(State, CNoteHistoryAdmin)
admin.site.register(District, CNoteHistoryAdmin)
admin.site.register(Pincode, CNoteHistoryAdmin)
admin.site.register(Accounts, CNoteHistoryAdmin)
admin.site.register(CNoteMaseter, CNoteMaseterAdmin)
admin.site.register(BookingType, CNoteHistoryAdmin)
admin.site.register(RefrenceCourier, CNoteHistoryAdmin)
admin.site.register(ReturnReason, CNoteHistoryAdmin)
admin.site.register(CNoteHistory, CNoteHistoryAdmin)


