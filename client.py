import account


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attributes = f"({self.name!r}, {self.age!r})"
        return f"{class_name} \n{attributes}"


class BankClient(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: account.Account | None


if __name__ == "__main__":
    c1 = BankClient("Lorem", 29)
    c1.account = account.CurrentAccount(123, 456, 100)
    print(c1)
    print(c1.account)
    c2 = BankClient("Ipsum", 27)
    c2.account = account.CurrentAccount(310, 817, 50000)
    print(c2)
    print(c2.account)
