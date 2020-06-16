__author__ = 'Sam Baron'

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
]

more_test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-02", "GOOG", 200.25],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-01", "GOOG", 176.80],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-03", "GOOG", 199.99],
    ["2014-06-04", "MSFT", 40.71],
]

DATE = 0
SYMBOL = 1
VALUE = 2

#CREATE TWO NEW LISTS ONE FOR EACH STOCK TICKER SYMBOL e.g. APPL and MSFT
def split_stock_list1(stock_list):
    """
        Manually split stock list
        into "appl" and "msft" lists
    """
    list_by_stock = []
    appl = []
    msft = []
    # Loop through stock list
    for stock_item in stock_list:
        # Identify company
        if stock_item[SYMBOL] == "APPL":
            appl.append(stock_item)
        elif stock_item[SYMBOL] == "MSFT":
            msft.append(stock_item)

    # Append appl and msft to return list
    list_by_stock.append(appl)
    list_by_stock.append(msft)

    return list_by_stock


#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?
def split_stock_list(stock_list):
    """
        Split stock list for any stocks
        into a dictionary with stock name as key and
        list of lists for stock entries
    """
    stocks = {}
    # Loop through stock list
    for stock_item in stock_list:

        # Set stock variables
        stock_date = stock_item[DATE]
        company = stock_item[SYMBOL]
        stock_amt = stock_item[VALUE]

        # Set stock dictionary key
        stock_key = str(company).lower()
        stock_values = [stock_date, stock_amt]

        # Append to stock dictionary
        # Test whether stock exists in dictionary
        if stock_key not in stocks.keys():
            stocks[stock_key] = []
        stocks[stock_key].append(stock_values)

    return stocks

#AVERAGE STOCK PRICE
def avg_stock_price(stocks_dict):
    """
    Calculate average stock price using
    dictionary of stocks with list values
    """

    output_dict = {}

    # Loop through stocks
    for stock, entry_list in stocks_dict.items():
        # Loop through list of stock entries
        price_total = 0
        for entry in entry_list:
            # Sum up stock price total
            price_total += entry[1]

        # Calculate average price
        avg_price = price_total / len(entry_list)

        # Append to output dictionary
        output_dict[stock] = avg_price

    return output_dict


if __name__ == "__main__":
    result_stocks = split_stock_list(more_test_data)
    for k, v in result_stocks.items():
        print(k, v)

    result_avg_price = avg_stock_price(result_stocks)
    for k, v in result_avg_price.items():
        print(k, v)
