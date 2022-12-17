import decimal
import string
from dataclasses import dataclass

from account.model import Account

@dataclass
class BankAccount:
    @property
    def current_sum(self)->decimal.Decimal:
        return self._current_sum

    id: int
    name: str
    surname: str
    _current_sum: decimal.Decimal
    _account: Account
    def add_to_bank_account(self, amount_of_money: decimal.Decimal)->None:
         self.current_sum = (self.current_sum + amount_of_money)
    def subtract_from_bank_account(self, amount_of_money: decimal.Decimal)->None:
         self.current_sum = (self.current_sum - amount_of_money)
    @current_sum.setter
    def current_sum(self, amount_of_money)->None:
        self._current_sum = amount_of_money
    @property
    def account(self)->Account:
        return self._account
    @account.setter
    def account(self, account: Account)->None:
        self._account = account
    @staticmethod
    def money_conversion(initial_currency: Account,
                         wanted_currency: Account,
                         amount_of_money: decimal.Decimal)->decimal.Decimal:
        match initial_currency, wanted_currency:
            case Account.KZT, Account.KZT:
                return amount_of_money
            case Account.KZT, Account.USD:
                return amount_of_money/decimal.Decimal(446.04)
            case Account.KZT, Account.EUR:
                return amount_of_money/decimal.Decimal(495.54)
            case Account.KZT, Account.RUB:
                return amount_of_money/decimal.Decimal(7.14)
            case Account.USD, Account.KZT:
                return amount_of_money / decimal.Decimal(0.0021)
            case Account.USD, Account.USD:
                return amount_of_money
            case Account.USD, Account.EUR:
                return amount_of_money / decimal.Decimal(1.06)
            case Account.USD, Account.RUB:
                return amount_of_money / decimal.Decimal(0.015)
            case Account.EUR, Account.KZT:
                return amount_of_money / decimal.Decimal(0.0020)
            case Account.EUR, Account.USD:
                return amount_of_money / decimal.Decimal(0.94)
            case Account.EUR, Account.EUR:
                return amount_of_money
            case Account.EUR, Account.RUB:
                return amount_of_money / decimal.Decimal(0.015)
            case Account.RUB, Account.KZT:
                return amount_of_money / decimal.Decimal(0.14)
            case Account.RUB, Account.USD:
                return amount_of_money / decimal.Decimal(64.92)
            case Account.RUB, Account.EUR:
                return amount_of_money / decimal.Decimal(68.94)
            case Account.RUB, Account.RUB:
                return amount_of_money
            case _:
                ...
    def to_string(self)->string:
        return f'id:{self.id} name:{self.name=} surname:{self.surname=} current sum:{self.current_sum} currency:{self.account.value}'
    def __del__(self)->None:
        print('Bank account was deleted')

# b = BankAccount(1, 'B', 'Z', decimal.Decimal(10000), Account.KZT)
# b.add_to_bank_account(decimal.Decimal(200))
# print(b.to_string())
# b.subtract_from_bank_account(decimal.Decimal(1))
# print(b)
# del b