from django.shortcuts import render, redirect
from django.db.models import Sum

from decimal import Decimal

from .models import Account
from .models import Transaction

from .forms import TransactionForm
from .forms import AccountForm
# Create your views here.

def home(request):
    if request.method=='POST':
        accountNumber = request.POST['accountNumber']
        account = Account.objects.get(id=accountNumber)
        transactions = Transaction.objects.all().filter(account=accountNumber).order_by('-date')
        withdrawls = Transaction.objects.all().filter(account=accountNumber, type = 'Withdrawl').aggregate(Sum('amount'))['amount__sum']
        if withdrawls == None:
            withdrawls = Decimal(0.00)
        deposits = Transaction.objects.all().filter(account=accountNumber, type='Deposit').aggregate(Sum('amount'))['amount__sum']
        if deposits == None:
            deposits = Decimal(0.00)
        endBalance = account.startingBalance + deposits - withdrawls
        balance = endBalance
        for t in transactions:
            if t.type == 'Deposit':
                t.balance = balance
                balance -= t.amount
            else:
                t.balance = balance
                balance += t.amount
        context = {'accountHolder': "{}, {}".format(account.lastName, account.firstName), 'transactions': transactions, 'endBalance': endBalance}
        return render(request, "accounts/BalanceSheet.html", context)
    accounts = Account.objects.all()
    return render(request, "accounts/index.html", {'accounts': accounts})

def createAccount(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "accounts/CreateNewAccount.html", {'form': form})

def addTransaction(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "accounts/AddTransaction.html", {'form': form})
