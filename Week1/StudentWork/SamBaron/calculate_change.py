""" Calculate Change """

# Dictionary with denomination values as keys and quantity as value
change_dict = {
    "0.01": 7,
    "0.05": 3,
    "0.10": 4,
    "0.25": 3,
    "0.50": 0,
    "1.00": 0
}

# List of coin quantities
change_list = [7,3,4,3,0,0]
# Dictionary with list index as key and denomination value as value
change_lookup = {
    0: 0.01,
    1: 0.05,
    2: 0.10,
    3: 0.25,
    4: 0.50,
    5: 1.00
}

# More complete coin dictionary
coin_lookup = {
    0: ["Pennies", 0.01],
    1: ["Nickels", 0.05],
    2: ["Dimes", 0.10],
    3: ["Quarters", 0.25],
    4: ["Half-Dollars", 0.50],
    5: ["Dollars", 1.00]
}

# Two dictionaries with common coin names
coin_quantity_dict = {
    "Pennies": 7,
    "Nickels": 3,
    "Dimes": 4,
    "Quarters": 3,
    "Half-Dollars": 0,
    "Dollars": 0
}
coin_value_dict = {
    "Pennies": 0.01,
    "Nickels": 0.05,
    "Dimes": 0.10,
    "Quarters": 0.25,
    "Half-Dollars": 0.50,
    "Dollars": 1.00
}

def calculate_change1_dict(input_dict):
    """
    Calculate change using dictionary with
        denomination values as keys and quantity as value
    """
    total_change = 0
    for denomination in input_dict:
        coin_quantity = input_dict[denomination]
        if coin_quantity !=0:
            denom_value = float(denomination)
            total_change += denom_value * coin_quantity

    return "${:,.2f}".format(total_change)


def calculate_change2_list(input_list, change_lookup):
    """
    Calculate change using list of quantities and
        lookup dictionary with list positions and values
    """

    total_change = 0
    for i in range(0, len(input_list)):
        coin_quantity = input_list[i]
        if coin_quantity != 0:
            denom_value = change_lookup[i]
            total_change += denom_value * coin_quantity

    return "${:,.2f}".format(total_change)


def calculate_change3_list_names(input_list, coin_lookup):
    """
    Calculate change using list of quantities and
        lookup dictionary with list positions, coin names, and values
    """

    total_change = 0
    output_dict = {}
    for i in range(0, len(input_list)):
        coin_quantity = input_list[i]
        if coin_quantity != 0:
            coin_name = coin_lookup[i][0]
            denom_value = coin_lookup[i][1]
            coin_amount = denom_value * coin_quantity
            output_dict[coin_name] = "${:,.2f}".format(coin_amount)
            total_change += coin_amount

    output_dict["Total Change"] = "${:,.2f}".format(total_change)

    return output_dict


def calculate_change4_two_dicts(quantity_dict, value_dict):
    """
    Calculate change using two dictionaries
        First has coin quantities
        Second has coin values
        Both have common coin names
    """
    total_change = 0
    output_dict = {}
    for coin in quantity_dict:
        coin_quantity = quantity_dict[coin]
        if coin_quantity != 0:
            coin_name = coin
            denom_value = value_dict[coin]
            coin_amount = denom_value * coin_quantity
            output_dict[coin_name] = "${:,.2f}".format(coin_amount)
            total_change += coin_amount

    output_dict["Total Change"] = "${:,.2f}".format(total_change)

    return output_dict

if __name__ == "__main__":
    dict_result = calculate_change1_dict(change_dict)
    list_result = calculate_change2_list(change_list, change_lookup)
    full_lookup_result = calculate_change3_list_names(change_list, coin_lookup)
    two_dict_result = calculate_change4_two_dicts(coin_quantity_dict, coin_value_dict)
    print("Dictionary Result - {}".format(dict_result))
    print("List Result - {}".format(list_result))
    print("Full Result - {}".format(full_lookup_result))
    print("Two Dictionary Result - {}".format(full_lookup_result))