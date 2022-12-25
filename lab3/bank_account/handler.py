import decimal
from typing import List

from account.model import Account
from bank_account.exceptions import BankAccountExists, BankAccountNotFound
from bank_account.model import BankAccount
from bank_account.service import BankAccountService


class BankAccountHandler:
    def __init__(self, service: BankAccountService):
        self.service = service

    def create_bank_account(self, search_id: int, name: str, surname: str, initial_sum: decimal.Decimal,
                            account: Account) -> None:
        try:
            self.service.create_bank_account(search_id, name, surname, initial_sum, account)
        except BankAccountExists:
            print(f'Already exist account with {search_id=}')
            raise BankAccountExists

    def delete_bank_account(self, search_id: int) -> None:
        try:
            self.service.delete_bank_account(search_id)
        except BankAccountNotFound:
            print(f'There are no account with {search_id=}')
            raise BankAccountNotFound

    def add_money_by_id(self, search_id: int, amount_of_money: decimal.Decimal) -> None:
        try:
            self.service.add_money_by_id(search_id, amount_of_money)
        except BankAccountNotFound:
            print(f'There are no account with {search_id=}')
            raise BankAccountNotFound

    def subtract_money_by_id(self, search_id: int, amount_of_money: decimal.Decimal) -> None:
        try:
            self.service.subtract_money_by_id(search_id, amount_of_money)
        except BankAccountNotFound:
            print(f'There are no account with {search_id=}')
            raise BankAccountNotFound

    def get_all_bank_accounts(self) -> List[BankAccount]:
        return self.service.get_all_bank_accounts()
