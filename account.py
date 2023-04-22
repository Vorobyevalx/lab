class Account:
    def __init__(self, name: str):
        """
        constructor method that initializes account name and balance
        """
        self.__name = name
        self.__balance = 0

    def deposit(self, amount: float) -> bool:
        """
        method to deposit money to the account.
        returns True if successful and False if unsuccessful
        """
        if amount <= 0:
            return False

        self.__balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        """
        method to withdraw money from the account
        returns True if successful and False if unsuccessful.
        """
        if amount <= 0 or amount > self.__balance:
            return False

        self.__balance -= amount
        return True

    def get_balance(self) -> float:
        """
        method to get the current account balance
        """
        return self.__balance

    def get_name(self) -> str:
        """
        method to get the account name.
        """
        return self.__name
