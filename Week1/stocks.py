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

# appl = []
# msft = []
#

# result example

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

print
appl
print
msft

# result example

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

# Example Output to eliminate redundant data

stocks = {
    "appl": [
        ["2014-06-01", "APPL", 100.11],
        ["2014-06-02", "APPL", 110.61],
        ["2014-06-03", "APPL", 120.22],
        ["2014-06-04", "APPL", 100.54],
    ],
    "msft": [
        ["2014-06-01", "MSFT", 20.46],
        ["2014-06-02", "MSFT", 21.25],
        ["2014-06-03", "MSFT", 32.53],
        ["2014-06-04", "MSFT", 40.71],
    ]
}



#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?
