import decimal
from typing import List

from account.model import Account
from bank_account.model import BankAccount


class BankRepositories:
    # print('2')
    _bank_accounts: List[BankAccount] = [
        BankAccount(2, 'B', 'Z', decimal.Decimal(10000), Account.KZT),
        BankAccount(3, 'B', 'Z', decimal.Decimal(10000), Account.KZT),
        BankAccount(5, 'B', 'Z', decimal.Decimal(10000), Account.KZT),
        BankAccount(1, 'B', 'Z', decimal.Decimal(10000), Account.KZT),
        BankAccount(7, 'B', 'Z', decimal.Decimal(10000), Account.KZT),
    ]

    @property
    def bank_accounts(self) -> List[BankAccount]:
        return self._bank_accounts

    @bank_accounts.setter
    def bank_accounts(self, changed_bank_accounts) -> None:
        self._bank_accounts = changed_bank_accounts

    def add_account(self, search_id: int, name: str, surname: str, initial_sum: decimal.Decimal,
                    account: Account) -> None:
        self.bank_accounts.append(BankAccount(
            search_id,
            name,
            surname,
            initial_sum,
            account
        ))

    def check_existence_of_account(self, search_id: int) -> bool:
        for bank_account in self.bank_accounts:
            if bank_account.id == search_id:
                return True
        return False

    def delete_account(self, search_id: int) -> None:
        bank_account = next((a for a in self.bank_accounts if a.id == search_id), None)
        self.bank_accounts.remove(bank_account)
        del bank_account
        # for i in self.bank_accounts:
        #     print(i)
        # del bank_account

    def add_money_by_id(self, search_id: int, amount_of_money: decimal.Decimal) -> None:
        next((a.add_to_bank_account(amount_of_money) for a in self.bank_accounts if a.id == search_id))

    def subtract_money_by_id(self, search_id: int, amount_of_money: decimal.Decimal) -> None:
        next((a.subtract_from_bank_account(amount_of_money) for a in self.bank_accounts if a.id == search_id))

# b = BankRepositories()
# b.delete_account(1)
# b.add_money_by_id(2, decimal.Decimal(9))
# b.add_account( 1, 's', 'f', decimal.Decimal(100), Account.EUR )
# for i in b.bank_accounts:
#     print(i)
