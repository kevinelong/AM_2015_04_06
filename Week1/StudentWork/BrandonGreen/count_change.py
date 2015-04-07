__author__ = 'brandon'

pocket_inventory = {
    'nickels': 2,
    'dimes': 10,
    'quarters': 1
}

def count_coins(coin_dict):
    total = 0.0
    for key in coin_dict.keys():
        if key == 'pennies':
            total += (coin_dict[key] * 1)
        elif key == 'nickels':
            total += (coin_dict[key] * 5)
        elif key == 'dimes':
            total += (coin_dict[key] * 10)
        elif key == 'quarters':
            total += (coin_dict[key] * 25)
    return total

print count_coins(pocket_inventory)
