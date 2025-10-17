from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from .custom_manager import CustomManager

class DebtManager(models.Manager):
    def get_queryset(self):
        super().get_queryset()    

class DebtModel(models.Model):
    id = models.BigAutoField(primary_key = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE, 
                             related_name = 'DebtModel',
                             null = True,
                             blank = True,)
    username = models.CharField(max_length=100, default = "", blank = True)
    debt_amount = models.FloatField(default=0.0, blank = True)
    debt_name = models.CharField(default = "", blank = True)
    debt_payment = models.FloatField(default = 0, blank = True)
    debt_rate = models.CharField(default = "Weekly", blank = True)
    debt_interest = models.FloatField(default = 0, blank = True)
    debt_notes = models.CharField(default = "", blank = True)
    debt_datetime = models.DateTimeField(auto_now = True, blank = True, null=True)

    objects = models.Manager()
    customObject = CustomManager()

    def __str__(self):
        return self.debt_name
