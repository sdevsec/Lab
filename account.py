class Account:
    def __init__(self, name:str) -> None:
        """
        Function to initialize an Account object with a name
        and a balance of 0.
        :param name: The name of the account holder.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount:float) -> bool:
        """
        Function to increment the acount balance by the specified amount.
        :param amount: Amount to deposit. Must be positive.
        :return: True if the deposit transaction is successful, False otherwise
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to decrement the account balance by the specified amount.
        :param amount: Amount to withdraw. Must be positive and not exceed
        the current account balance.
        :return: True if the withdrawal is successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function to return the account balance
        :return: Return the current account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to return the account name
        :return: Return the account name
        """
        return self.__account_name
