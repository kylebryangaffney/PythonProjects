from django.db import models

# Create your models here.

from django.db import models

class Account(models.Model):
    account_first_name = models.CharField(max_length=60, default="", null=False)
    account_last_name = models.CharField(max_length=60, default="", null=False)
    account_starting_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=False)
    objects = models.Manager()

    def current_balance(self):
        deposits = sum(t.transaction_amount for t in self.transactions.all() if t.transaction_type == 'D')
        withdrawals = sum(t.transaction_amount for t in self.transactions.all() if t.transaction_type == 'W')
        return self.account_starting_balance + deposits - withdrawals

    def __str__(self):
        display_account = "{0.account_last_name}, {0.account_first_name}"
        return display_account.format(self)

    class Meta:
        verbose_name_plural = "Accounts"
