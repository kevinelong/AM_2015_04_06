__author__ = 'kevin'

app = {
    "users": [
        {
            "name": "Kevin",
            "id": 0
        },
        {
            "name": "Asha",
            "id": 1
        },
    ],
    "categories": [
        {
            "id": 0,
            "name": "groceries",
        },
        {
            "id": 1,
            "name": "office",
        },
    ],
    "transactions": [
        {
            "id": 0,
            "cid": 0,
            "uid": 123,
            "note": "",
            "amount": 111.11
        }
    ],

}

app["transactions"].append({"uid": 123, "cid": 1, "amount": 999.99})
app["transactions"].append({"uid": 123, "cid": 0, "amount": 222.22})
app["transactions"].append({"uid": 123, "cid": 0, "amount": 222.22})
app["transactions"].append({"uid": 123, "cid": 0, "amount": 222.22})

current_category_name = ""
totals = {}
# print app["transactions"]

for t in app["transactions"]:
    cid = t["cid"]
    categories = app["categories"]
    tc = categories[cid]
    name = tc["name"]
    if name not in totals:
        totals[name] = 0
    totals[name] = totals[name] + t["amount"]

#TODO print totals dictionary fancy or make pie chart
print(totals)

print(app)