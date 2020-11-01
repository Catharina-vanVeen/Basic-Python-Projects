from django.db import models
from django.db.models import DateField
from django.core.validators import MinValueValidator
from decimal import Decimal
import datetime

# Create your models here.
class Account(models.Model):
    firstName = models.CharField(max_length=60, blank=False, null=False)
    lastName = models.CharField(max_length=60, blank=False, null=False)
    startingBalance = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False, default=0.00)

    objects = models.Manager()

    def __str__(self):
        return "{:09}\t{}, {}".format(self.pk, self.lastName, self.firstName)

TYPE_CHOICES = {
    ('Deposit', 'deposit'),
    ('Withdrawl', 'withdrawl'),
}

class Transaction(models.Model):
    date = DateField(auto_now=False, auto_now_add=False, blank=False, null=False, default=datetime.date.today)
    type =  models.CharField(max_length=20, blank=False, null=False, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False, validators=[MinValueValidator(Decimal('0.01'))])
    description = models.CharField(max_length=255, blank=True, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return "{} {} {}".format(self.date, self.type, self.account)
