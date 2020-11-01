import django_tables2 as tables
from .models import Transaction

class TransactionTable(tables.Table):
    class Meta:
        model = Transaction
        sequence = ("date", "type", "description", "amount",)
        exclude = ("account", "id")