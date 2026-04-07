from django.db import models

# Create your models here.

# Model of bank account
class Account(models.Model):
    #  User identity char fields
    first_name = models.CharField(max_length=60, default="", null=False)
    last_name = models.CharField(max_length=60, default="", null=False)
    # Set initial starting money value
    initial_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=False)

    # Renames the objects manager to Accounts
    Accounts = models.Manager()

    # Sets how the accounts are displayed in the Django Admin and shell
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        verbose_name_plural = "Accounts"
    

# Tuple providing the dropdown choices for the Transactions
transaction_types_list = (("Deposit", "Deposit"), ("Withdrawal", "Withdrawal"))

# Transactions for activity of specific accounts
class Transaction(models.Model):

    # Date field to track when the transaction occurred
    date = models.DateField()
    # Use the transaction_types_list to fill a dropdown menu
    type = models.CharField(max_length=10, choices=transaction_types_list)
    # Monitary value of transaction amounts
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    
    # Optional field for description of the transaction blank=True allows this to be empty in forms
    description = models.CharField(max_length=100, default="", blank=True)
    
    # Establishes a many to one relationship; if Account is deleted, then all of the related Transactions are also deleted (CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    # Renames the default manager to 'Transactions'
    Transactions = models.Manager()

    class Meta:
        verbose_name_plural = "Transactions"