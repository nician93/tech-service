from django.db import models
class StudReg(models.Model):
    uname=models.CharField(max_length=20,default='addNew')
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    p_address=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    pincode=models.CharField(max_length=20)
    course=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    last_login=models.DateTimeField()
    
# Create your models here.
