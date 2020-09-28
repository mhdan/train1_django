from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)
    balance = models.BigIntegerField("sum of all money in the bank",
                                     default=1000000)


class Bank_Account(models.Model):
    TYPES = (
        ('C', 'Credit'),
        ('I', 'Investment')
    )
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_number = models.BigAutoField(primary_key=True)
    sum_balance = models.BigIntegerField("sum of saving and checking balance",
                                         default=10000)
    type_selection = models.CharField(max_length=1, choices=TYPES)

    def checking_balance(self):
        # returning the balance of Checking_Account ???
        pass

    def saving_balance(self):
        # returning the balance of Saving_Account ???
        pass


class Saving_Account(models.Model):
    bank_account = models.OneToOneField(Bank_Account, on_delete=models.CASCADE)
    balance = models.BigIntegerField("balance for saving account",
                                     default=10000)
    date_created = models.DateField(auto_now_add=True)

    def deposit(self, money):
        self.balance += money

    def check_balance(self):
        return self.balance


class Checking_Account(models.Model):
    bank_account = models.OneToOneField(Bank_Account, on_delete=models.CASCADE)
    balance = models.BigIntegerField("balance for checking account",
                                     default=0)
    date_created = models.DateField(auto_now_add=True)
    last_transaction = models.DateTimeField(auto_now=True)

    def deposit(self, money):
        self.balance += money

    def withdrawal(self, money):
        self.balance -= money

    def check_balance(self):
        return self.balance
