"""
1. Create a new class for a CustomerBankAccount.
2. Create fields for the Account Number, Balance, Customer Name, Email and Phone Number.
3. Create methods to read, write and update each field. Basically, some getters and setters.
4. Create two additional methods:
    i. One to allow the customer to deposit the funds (this should increment the balance field)
    ii. One to allow the customer to withdraw funds (this should deduct from the balance fields but not allow the withdrawal to complete if their founds are insufficient).
5. Create some validation code using your getters and setters to confirm your code is working at each step of the user flow. You should be able to show that a new user can be created and that this user can deposit and withdraw funds.
"""


class CustomerBankAccount:
    def __init__(self, account_number, balance, name, email, phone):
        self.__account_number = int(account_number)
        self.__balance = int(balance)
        self.__name = name
        self.__email = email
        self.__phone = phone

    def __str__(self):
        return f"Account #: {self.__account_number}\nBalance: {self.__balance}\nName: {self.__name}\nE-Mail: {self.__email}\nPhone: {self.__phone}"

    # Getters
    def get_acct_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    # Setters
    def set_acct_number(self, value):
        self.__account_number = value

    def set_balance(self, value):
        self.__balance = value

    def set_name(self, value):
        self.__name = value

    def set_email(self, value):
        self.__email = value

    def set_phone(self, value):
        self.__phone = value

    # Customer deposits, increments balance attribute.
    def deposit(self, amount):
        amount = int(amount)
        self.__balance += amount

    # Customer withdrawal, must have enough in account.
    def withdraw(self, amount):
        amount = int(amount)
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Insufficient funds."


# Tests
if __name__ == "__main__":
    acct1 = CustomerBankAccount(321, 500, "Steve", "email", "123-4567")
    print("Account Info:")
    print("-------------")
    print(acct1)
    print("-------------")
    print("Add a new deposit of $100")
    acct1.deposit(100)
    print(f"New account balance: {acct1.get_balance()}")
    print("Create a withdrawal of $200")
    acct1.withdraw(200)
    print(f"New account balance: {acct1.get_balance()}")
    print("Try to withdraw more than you have available.")
    print(acct1.withdraw(600))
    print(acct1.get_balance())
