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

# RESULT EXAMPLE
appl = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
]
msft = [
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]
# CREATE TWO NEW LISTS ONE FOR EACH STOCK TICKER SYMBOL e.g. APPL and MSFT

appl = []
msft = []
SYMBOL_INDEX = 1

for s in test_data:
    symbol = s[SYMBOL_INDEX]

    if symbol == "APPL":
        appl.append(s)
    elif symbol == "MSFT":
        msft.append(s)

print(appl)
print(msft)

# ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?
stocks = {}
SYMBOL_INDEX = 1
DATE_INDEX = 0
VALUE_INDEX = 2

for s in test_data:
    symbol = s[SYMBOL_INDEX]
    if symbol not in stocks.keys():
        stocks[symbol] = []
    day = s[DATE_INDEX]
    value = s[VALUE_INDEX]
    stock = [day, value]
    stocks[symbol].append(stock)

print(stocks["MSFT"])

#EXAMPLE OUTPUT
stocks = {
    "APPL": [
        ["2014-06-01", 100.11],
        ["2014-06-02", 110.61],
        ["2014-06-03", 120.22],
        ["2014-06-04", 100.54],
    ],
    "MSFT": [
        ["2014-06-01", 20.46],
        ["2014-06-02", 21.25],
        ["2014-06-03", 32.53],
        ["2014-06-04", 40.71],
    ]
}

