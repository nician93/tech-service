from django.db import models
from django.contrib.auth.models import User

class refundInfo(models.Model):
    refund_user=models.ForeignKey(User,on_delete=models.CASCADE)
    circle_name=models.CharField(max_length=20)
    refund_date=models.DateField()
    refund_amount=models.DecimalField(max_digits=50, decimal_places=2)

    @property
    def name(self):
        return self.refund_user.username
# Create your models here.
