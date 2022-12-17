import decimal
from dataclasses import dataclass
from typing import List

from account.model import Account
from bank_account.exceptions import BankAccountExists, BankAccountNotFound
from bank_account.model import BankAccount
from bank_account.repositories import BankRepositories


@dataclass
class BankAccountService:
    repositories: BankRepositories
    def create_bank_account(self, search_id: int, name: str, surname: str, initial_sum: decimal.Decimal, account: Account):
        if self.repositories.check_existence_of_account(search_id):
            raise BankAccountExists
        self.repositories.add_account(search_id, name, surname, initial_sum, account)
    def delete_bank_account(self, search_id:int):
        if not self.repositories.check_existence_of_account(search_id):
            raise BankAccountNotFound
        self.repositories.delete_account(search_id)
    def add_money_by_id(self, search_id: int, amount_of_money: decimal.Decimal):
        if not self.repositories.check_existence_of_account(search_id):
            raise BankAccountNotFound
        self.repositories.add_money_by_id(search_id, amount_of_money)

    def subtract_money_by_id(self, search_id: int, amount_of_money: decimal.Decimal):
        if not self.repositories.check_existence_of_account(search_id):
            raise BankAccountNotFound
        self.repositories.subtract_money_by_id(search_id, amount_of_money)
    def get_all_bank_accounts(self)->List[BankAccount]:
        return self.repositories.bank_accounts
