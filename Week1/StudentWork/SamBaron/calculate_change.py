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

    return total_change


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

    return total_change


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
            output_dict[coin_name] = "${}".format(round(coin_amount,2))
            total_change += coin_amount

    output_dict["Total"] = total_change

    return output_dict

if __name__ == "__main__":
    dict_result = calculate_change1_dict(change_dict)
    list_result = calculate_change2_list(change_list, change_lookup)
    full_lookup_result = calculate_change3_list_names(change_list, coin_lookup)
    print("Dictionary Result - {}".format(dict_result))
    print("List Result - {}".format(list_result))
    print("Full Result - {}".format(full_lookup_result))