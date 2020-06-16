# pocket_change = {
#     "pennies": 13,
#     "nickels": 3,
#     "dimes": 2,
#     "quarters": 4
# }
#
# def q("quarters"):
#
#
# def add_up(pocket_change):
#     totals = {}
    # ... DO YOUR WORK HERE

# a small change

def get_min_coins(amount_rem):
    coin_combinations = [1, 5, 10, 25]
    coin_list = []

    for coin_val in sorted(coin_combinations,reverse=True):
        coin_count = amount_rem/coin_val
        coin_list += [coin_val] * coin_count
        amount_rem -= coin_val * coin_count

    return coin_list
if __name__ == '__main__':

    total_amount = 106  # unit: US cents = $1.06
    print get_min_coins(total_amount)

    #     return totals
#
# if __name__ == "__main__":
#     print(add_up(pocket_change))

#Sample output
#{'dimes': 20, 'nickels': 15, 'all_totaled': 148, 'pennies': 13, 'quarters': 100}
