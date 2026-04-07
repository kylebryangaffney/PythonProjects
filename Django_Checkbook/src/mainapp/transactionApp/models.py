from django.db import models

class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DEPOSIT = 'D', 'Deposit'
        WITHDRAWAL = 'W', 'Withdrawal'

    transaction_date = models.DateField()
    transaction_type = models.CharField(
        max_length=1,
        choices=TransactionType.choices,
        default=TransactionType.DEPOSIT
    )
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    transaction_description = models.CharField(max_length=200, default="", blank=True)
    transaction_account = models.ForeignKey('accountApp.Account', on_delete=models.CASCADE, related_name='transactions')
    objects = models.Manager()

    def __str__(self):
        display_transaction = "{0.transaction_type}: {0.transaction_date} - ${0.transaction_amount}"
        return display_transaction.format(self)

    class Meta:
        verbose_name_plural = "Transactions"
