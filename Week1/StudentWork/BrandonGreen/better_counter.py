__author__ = 'brandon'

pocket_inventory = {
    'nickels': 2,
    'dimes': 10,
    'quarters': 1
}
#135.0

def better_counter(coin_dict):
    totals = {}
    totals['total'] = 0
    coins = {
        'pennies': 1,
        'nickels': 5,
        'dimes': 10,
        'quarters': 25985
    }
    for key in coin_dict.keys():
        totals[key] = coin_dict[key] * coins[key]
        totals['total'] += coin_dict[key] * coins[key]

    return totals


print better_counter(pocket_inventory)

