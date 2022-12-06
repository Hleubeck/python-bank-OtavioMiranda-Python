import account
import client


class Bank:
    def __init__(self, agencies: list[int] | None = None,
                 clients: list[client.Person] | None = None,
                 accounts: list[account.Account] | None = None) -> None:
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []

    def _agency_auth(self, account):
        if account.Account.agency in self.agencies:
            return True
        return False

    def _client_auth(self, client: client.Person):
        if client in self.clients:
            return True
        return False

    def _account_auth(self, account: account.Account):
        if account in self.accounts:
            return True
        return False

    def validation_account(self, client: client.BankClient,
                           account: account.Account):
        if account is client.account:
            print(f"Olá, {client.name}")
            return True
        print("Validação de Conta Negada!")
        return False

    def _global_auth(self, clients: client.BankClient,
                     accounts: account.Account):
        if self._agency_auth is False:
            print("Falha na autenticação, AGENCIA NÃO ENCONTRADA!")
        elif self._client_auth is False:
            print("Falha na autenticação, CLIENTE INVÁLIDO OU NÃO CADASTRADO!")
        elif self._account_auth is False:
            print("Falha na autenticação, CONTA NÃO ENCONTRADA!")
        elif self.validation_account is False:
            print("Conta não encontrada.")
            return False
        return True

    def __repr__(self):
        class_name = type(self).__name__
        attribs = f"({self.agencies!r}, {self.accounts!r}, {self.clients!r})"
        return f"{class_name} \n{attribs}"


if __name__ == "__main__":
    c1 = client.BankClient("Lorem", 29)
    cacc1 = account.CurrentAccount(123, 456, 100)
    c1.account = cacc1
    c2 = client.BankClient("Ipsum", 27)
    cacc2 = account.CurrentAccount(557, 362, 5000)
    c2.account = cacc2
    python_bank = Bank()
    python_bank.clients.extend([c1, c2])
    python_bank.accounts.extend([cacc1, cacc2])
    python_bank.agencies.extend([123, 310])
    if Bank._global_auth(python_bank, c1, cacc1):
        cacc1.cash_in(1500)
        c1.account.cash_out(600)
        print(c1.account)
    if Bank._global_auth(python_bank, c2, cacc2):
        cacc2.cash_out(100)
        c2.account.cash_in(1200)
        print(c2.account)
