from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

class MoneyAccount(models.Model):
    user = models.ForeignKey(User, related_name = 'user_accounts', on_delete = models.CASCADE, default = 1,)
    CHECKING = 'CHECKING ACCOUNT'
    SAVINGS = 'SAVINGS ACCOUNT'
    CREDIT = 'CREDIT CARD ACCOUNT'
    
    TYPE_OF_ACCOUNT_CHOICES = [
        (CHECKING, 'CHECKING ACCOUNT'),
        (SAVINGS, 'SAVINGS ACCOUNT'),
        (CREDIT, 'CREDIT CARD ACCOUNT'),
    ]
    account_type = models.CharField(
        max_length = 20,
        choices = TYPE_OF_ACCOUNT_CHOICES,
        default = CHECKING,
    )

    account_name = models.CharField(max_length=100, null=True)
    balance = models.IntegerField(default=0)

    
    def get_absolute_url(self):
        return reverse("thanks")
    
    def __str__(self):
        return "{}'s {}".format(self.user,self.account_name)
    




class MonthlyBillManager(models.Manager):
    def monthly_bills(self, **kwargs):
        return self.filter(Q(bill_type=Bill.MONTHLY))


class Bill(models.Model):
    user = models.ForeignKey(User , related_name = 'user_bills', on_delete = models.CASCADE, default = 1)
    WEEKLY = 'WEEKLY EXPENSE'
    BIWEEKLY = 'BI-WEEKLY EXPENSE'
    MONTHLY = 'MONTHLY EXPENSE'
    SINGLE = 'ONE TIME EXPENSE'
    TYPE_OF_BILL_CHOICES =[
        (WEEKLY, 'WEEKLY EXPENSE'),
        (BIWEEKLY, 'BI-WEEKLY EXPENSE'),
        (MONTHLY, 'MONTHLY EXPSENSE'),
        (SINGLE, 'ONE TIME EXPENSE'),
    ]
    bill_type = models.CharField(
        max_length = 20, choices=TYPE_OF_BILL_CHOICES, default=SINGLE
    )
    bill_name = models.CharField(max_length = 10, default ='Expense')
    bill_amount = models.IntegerField(default = 0,)
    automatic_payment = models.ForeignKey(MoneyAccount, null=True, blank=True, related_name = 'personal_accounts', on_delete=models.CASCADE)

    objects = models.Manager()
    monthly_bill_objects = MonthlyBillManager()


    def get_absolute_url(self):
        return reverse("thanks")
    
    def __str__(self):
        return self.bill_name

