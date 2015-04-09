pocket_change = {
    "pennies": 13,
    "nickels": 3,
    "dimes": 2,
    "quarters": 4
}

change_values = {
    "pennies": 1,
    "nickels": 5,
    "dimes": 10,
    "quarters": 25
}


def add_up(pocket_change):
    totals = {}
    grand = 0
    # ... DO YOUR WORK HERE
    for k in pocket_change.keys():
        subtotal = pocket_change[k] * change_values[k]
        totals[k] = subtotal
        grand += subtotal
    totals["all_totaled"] = grand
    return totals


if __name__ == "__main__":
    print(add_up(pocket_change))
