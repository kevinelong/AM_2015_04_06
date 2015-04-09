__author__ = 'brandon'

#GIVEN THE FOLLOWING LIST OF LIST
test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
    ["2014-06-05", "GOOG", 201.10],
]

#CREATE TWO NEW LISTS ONE FOR EACH STOCK TICKER SYMBOL e.g. APPL and MSFT

#appl = []

#msft = []

#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?

def stock_separator(stocks):
    appl = [stock for stock in stocks if 'APPL' in stock]
    msft = [stock for stock in stocks if 'MSFT' in stock]
    result = {
        'APPL': appl,
        'MSFT': msft
    }
    return result

#print stock_separator(test_data)

def scale_stocker(stocks):
    result = {}
    for stock in stocks:
        key = stock[1]
        result[key] = [stock for stock in stocks if key in stock]
    return result



print scale_stocker(test_data)
