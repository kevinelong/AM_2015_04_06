# GIVEN THE FOLLOWING LIST OF LIST
test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

# CREATE TWO NEW LISTS ONE FOR EACH STOCK TICKER SYMBOL e.g. APPL and MSFT
#
# appl = []
#
# msft = []
#
# for data_item in test_data:
#     if data_item[1] == "APPL":
#         appl.append(data_item)
#     elif data_item[1] == "MSFT":
#         msft.append(data_item)
#     else:
#         pass
#
# print appl
# print msft

#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?

stock_symbols = ["APPL", "MSFT"]

sym_key = 0

sorted_data = {}
temp_list = []

for symbol in stock_symbols:
    for data_item in test_data:
        if data_item[1] == symbol:
            temp_list += [data_item[0], data_item[2]]
            new_data = {symbol: temp_list}
        else:
            pass
    sorted_data.update(new_data)

print sorted_data