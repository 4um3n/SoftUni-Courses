class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, value):
        if isinstance(value, int):
            self._transactions.append(value)
        elif isinstance(value, list):
            self._transactions.extend(value)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError(f"sorry cannot go in debt!")

        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError(f"please use int for amount")
        self.transactions = amount

    def __len__(self):
        return len(self.transactions)

    def __reversed__(self):
        return reversed(self.transactions)

    def __getitem__(self, item):
        return self.transactions[item]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        new_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_account.transactions = self.transactions + other.transactions
        return new_account

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"
