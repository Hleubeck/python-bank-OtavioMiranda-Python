from abc import abstractmethod


class Account():
    def __init__(self, agency: int, account: int, cash: float = 0):
        self.agency = agency
        self.account = account
        self.cash = cash

    @abstractmethod
    def cash_out(self, cash_out: float) -> float:
        self.cash -= cash_out
        return self.cash

    def cash_in(self, cashin: float) -> float:
        self.cash += cashin
        self.messages("Deposito efetuado com sucesso! \n")
        return self.cash

    def __repr__(self):
        class_name = type(self).__name__
        attributes = f"({self.agency!r}, {self.account!r}, {self.cash!r})"
        return f"{class_name} \n{attributes}"

    def messages(self, msg: str = "") -> None:
        print(f"{msg} O seu saldo atual é de R${self.cash:.2f}.")


class SavingsAccount(Account):
    def cash_out(self, cash_out):
        self.pre_cashout = self.cash - cash_out
        if self.pre_cashout >= 0:
            self.cash -= cash_out
            self.messages(f"Saque no valor de R${cash_out} autorizado! \n")
            return self.cash
        print("Saque negado, o valor digitado é maior que seu saldo!")
        print(f"O seu saldo atual é de: R${self.cash:.2f}")
        return self.cash

    def cash_in(self, cashin):
        return super().cash_in(cashin)


class CurrentAccount(Account):
    def __init__(self, agency: int, account: int, cash: float = 0,
                 limit: float = 100):
        super().__init__(agency, account, cash)
        self.limit = limit

    def cash_out(self, cash_out):
        self.pre_cashout = self.cash - cash_out
        limit_credit = -self.limit
        print(f"Meu limite: {limit_credit}")
        if self.pre_cashout >= limit_credit:
            self.cash -= cash_out
            self.messages(f"Saque no valor de R${cash_out} Autorizado! \n")
            return self.cash
        print("Saque negado, o valor digitado é maior que seu saldo!")
        print(f"O seu saldo atual é de: R${self.cash:.2f}")
        return self.cash

    def cash_in(self, cashin):
        return super().cash_in(cashin)


if __name__ == "__main__":
    saving_accperson1 = SavingsAccount(111, 222, 5)
    current_accperson2 = CurrentAccount(111, 222, 0)
    current_accperson2.cash_out(1)
    current_accperson2.cash_out(1)
    current_accperson2.cash_out(1)
    current_accperson2.cash_out(1)
    current_accperson2.cash_out(96)
    current_accperson2.cash_out(1)
    current_accperson2.cash_in(96)
    current_accperson2.cash_in(1)
    current_accperson2.cash_out(96)
    current_accperson2.cash_out(1)
