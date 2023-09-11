from django.contrib import admin
from moduleinformation.models import refundInfo

class RefundAdmin(admin.ModelAdmin):
    list_display=('refund_user','circle_name','refund_date','refund_amount')

admin.site.register(refundInfo,RefundAdmin) 
# Register your models here.
