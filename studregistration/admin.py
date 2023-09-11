from django.contrib import admin
from studregistration.models import StudReg
class StudInfo(admin.ModelAdmin):
    list_display=('first_name','last_name','mother_name','father_name','p_address','gender','state','city','dob','pincode','course','email','password')

admin.site.register(StudReg,StudInfo)    
# Register your models here.
