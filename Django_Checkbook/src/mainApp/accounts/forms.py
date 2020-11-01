from django.forms import ModelForm
from .models import Account, Transaction

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ["account", "type", "description", "amount",]

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'