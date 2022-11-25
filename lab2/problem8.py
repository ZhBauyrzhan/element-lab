current_sum = 0.0


def add_to_bank_account(sum: float):
    global current_sum
    current_sum += sum


def substract_from_bank_account(sum: float):
    global current_sum
    current_sum -= sum


def money_conversion(sum: float, init, wanted):
    match init, wanted:
        case 'USD' as init, 'KZT' as wanted:
            return current_sum * 470
        case 'KZT' as init, 'USD' as wanted:
            return current_sum / 470
        case _:
            return "We don't do this"


add_to_bank_account(500)
print(current_sum)

substract_from_bank_account(200)
print(current_sum)

print( money_conversion(300, 'KZT', 'USD') )