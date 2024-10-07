class BankAccount:
    def __init__(self, pin):
        """Initial account balance is 0 and pin is 'pin'."""
        self._pin = pin
        self._balance = 0.0

    def deposit(self, pin, amount):
        """Increment account balance by amount and return new balance."""
        self.check_pin(pin)
        self._balance += amount
        return self._balance

    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount
        withdrawn."""
        self.check_pin(pin)
        if amount > self._balance:
            raise ValueError('Cannot withdraw more than your balance.')
        self._balance -= amount
        return self._balance

    def get_balance(self, pin):
        """Return account balance."""
        self.check_pin(pin)
        return self._balance

    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin."""
        self.check_pin(oldpin)
        self._pin = newpin

    def check_pin(self, pin):
        """Check if pin is valid."""
        if pin != self._pin:
            raise ValueError('Pin is not valid.')


class SavingsAccount(BankAccount):
    def __init__(self, pin, interest_rate):
        super().__init__(pin)
        self.interest_rate = interest_rate

    def add_interest(self, pin):
        super().deposit(pin, (self.interest_rate / 100 *
                              super().get_balance(pin)))


class FeeSavingsAccount(SavingsAccount):
    def __init__(self, pin, interest_rate, fee):
        super().__init__(pin, interest_rate)
        self.fee = fee

    def withdraw(self, pin, amount):
        if (0 < super().get_balance(pin) <=
                super().get_balance(pin) + self.fee):
            super().withdraw(pin, amount)
            self._balance -= self.fee


def main():
    account1 = BankAccount('a')
    account2 = SavingsAccount('b', 7)
    account3 = FeeSavingsAccount('c', 10, 2)
    print('Depositing')
    account1.deposit('a', 100.50)
    account2.deposit('b', 200.00)
    account3.deposit('c', 300.25)
    print(account1.get_balance('a'))
    print(account2.get_balance('b'))
    print(account3.get_balance('c'))
    print('Withdrawing')
    account1.withdraw('a', 100.00)
    account2.withdraw('b', 100.00)
    account3.withdraw('c', 200.00)
    print(account1.get_balance('a'))
    print(account2.get_balance('b'))
    print(account3.get_balance('c'))
    print('Changing pin')
    account1.change_pin('a', 'x')
    account2.change_pin('b', 'y')
    account3.change_pin('c', 'z')
    print('Adding interest')
    account2.add_interest('y')
    print(account2.get_balance('y'))
    account3.add_interest('z')
    print(account3.get_balance('z'))


if __name__ == '__main__':
    main()
