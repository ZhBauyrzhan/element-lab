import decimal
import sys

from account.model import Account
from bank_account.repositories import BankRepositories
from bank_account.service import BankAccountService
from bank_account.handler import BankAccountHandler
from bank_account.exceptions import BankAccountExists, BankAccountNotFound
def init():
    # print('1')
    bank_account_repositories = BankRepositories()
    bank_account_service = BankAccountService(bank_account_repositories)
    bank_account_handler = BankAccountHandler(bank_account_service)
    while True:
        print('Choose action:')
        print('1. Create bank account')
        print('2. Add money to bank account by id')
        print('3. Subtract money from bank account by id')
        print('4. Delete money to bank account by id')
        print('5. Print all existed bank accounts')
        print('Q. quit')
        command = input()
        match command:
            case 'Q':
                sys.exit(0)
            case '1':
                search_id = input('Give me ID:')
                name = input('Now give me your name:')
                surname = input('Now give me your surname:')
                initial_sum = input('Now give me your initial amount of money:')
                account_type = input('Now give me currency:')
                account =  next((a for a in Account if a.value == account_type ),None)
                # print(type(account), account)
                if account is None:
                    print('Wrong currency!')
                    continue
                else:
                    try:
                        bank_account_handler.create_bank_account(int(search_id), name, surname, decimal.Decimal(initial_sum), account)
                    except BankAccountExists:
                        ...
            case '2':
                search_id = int(input('Give me ID:'))
                amount_of_money = decimal.Decimal(input('Now give me amount of money:'))
                try:
                    bank_account_handler.add_money_by_id(search_id, amount_of_money)
                except BankAccountNotFound:
                    ...
            case '3':
                search_id = int(input('Give me ID:'))
                amount_of_money = decimal.Decimal(input('Now give me amount of money:'))
                try:
                    bank_account_handler.subtract_money_by_id(search_id, amount_of_money)
                except BankAccountNotFound:
                    ...
            case '4':
                search_id = int(input('Give me ID:'))
                try:
                    bank_account_handler.delete_bank_account(search_id)
                except BankAccountNotFound:
                    ...
            case '5':
                bank_accounts = bank_account_handler.get_all_bank_accounts()
                for i in bank_accounts:
                    print(i.to_string())
if __name__ == '__main__':
    init()