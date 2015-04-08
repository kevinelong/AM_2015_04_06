pocket_change = {
    "pennies": 13,
    "nickels": 3,
    "dimes": 2,
    "quarters": 4
}

def q("quarters"):


def add_up(pocket_change):
    totals = {}
    # ... DO YOUR WORK HERE

def main():
    cost = input("Enter the Purchase cost of all items:")
    tendered = input("Enter the Tendered amount:")
    change = tendered - cost
    change = int(change * 100)
    a = change / 200

    return totals

if __name__ == "__main__":
    print(add_up(pocket_change))

#Sample output
#{'dimes': 20, 'nickels': 15, 'all_totaled': 148, 'pennies': 13, 'quarters': 100}
