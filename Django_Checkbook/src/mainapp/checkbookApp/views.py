from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# Create your views here.
def home(request):
    # Initialize the TransactionForm for dropdown choice selector on the home page
    form = TransactionForm(data=request.POST or None)
    
    if request.method == "POST":
        # Get the selected account's primary key from the submitted form
        pk = request.POST["account"]
        # Send the user to the balance sheet for the selected primary key
        return balance(request, pk)
    
    # Set the form to the template so the account dropdown renders
    ctx = {"form": form}
    return render(request, 'checkbook/index.html', ctx)


def create_account(request):
    # Initialize a blank AccountForm
    form = AccountForm(data=request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()  # Save new account to the actual database
            return redirect("index")  # Send user to home page
    
    ctx = {"form": form}
    return render(request, 'checkbook/CreateNewAccount.html', ctx)


def balance(request, pk):
    # Get the account by primary key if it exists, else return 404
    account = get_object_or_404(Account, pk=pk)
    
    # Get all transactions from account
    transactions = Transaction.Transactions.filter(account=pk)
    
    # Set the initial total from the account
    cur_total = account.initial_deposit
    
    # table_contents maps each transaction to the balance we are adding to 
    table_contents = {}
    
    for t in transactions:
        if t.type == "Deposit":
            cur_total += t.amount          # Add deposits to the current total
        else:
            cur_total -= t.amount          # Else subtract withdrawals from the current total
        table_contents.update({t: cur_total})  # Store transaction with its resulting balance
    
    ctx = {
        "account": account,              # Account
        "table_contents": table_contents, # Dict of transactions and the running totals
        "balance": cur_total             # Final balance after all transactions accounted for
    }
    return render(request, 'checkbook/BalanceSheet.html', ctx)


def transaction(request):
    # Initialize a blank TransactionForm
    form = TransactionForm(data=request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            # Get the account primary key before saving so we can link it to its balance entry
            pk = request.POST["account"]
            form.save()  # Save the current transaction to the database
            return balance(request, pk)  # Show user updated balance sheet
    
    ctx = {"form": form}
    return render(request, 'checkbook/AddTransaction.html', ctx)