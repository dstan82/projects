
cost = float(input('How much the product costs: '))
money_paid = float(input('How much did you paid: '))

numismatics = {100: '$100', 50: '$50', 20: '$20', 10: '$10', 5: '5$', 1: '1$',
               0.25: '25¢', 0.10: '10¢', 0.05: '5¢', 0.01: '1¢'}


def calculate_change(cost, money):
    actual_change = []
    if money < cost:
        return 'not enough money !'
    elif money == cost:
        return 'No change!'
    else:
        change = money - cost
        for denomination in numismatics.keys():
            while change >= denomination:
                actual_change.append(numismatics[denomination])
                change -= denomination
    return f'\nYour change in bills and coins: {actual_change}'


print(calculate_change(cost, money_paid))
