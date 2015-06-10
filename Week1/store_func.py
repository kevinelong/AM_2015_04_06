receipts = [
    {
        "id": 1,
        "datetime": "1/1/2011 12:11 pm"
    },
    {
        "id": 2,
        "datetime": "2/2/2011 12:22 pm"
    }
]
# print the datetime of the second receipt: (list/array index starts at 0)
print(receipts[1]["datetime"])

# print the datetime of the receipt with id == 2: (list/array index starts at 0)
for r in receipts:
    if r["id"] == 2:
        print(r["datetime"])

receipt_dictionary_of_ids = {
    "1": {
        "datetime": "1/1/2011 12:11 pm"
    },
    "2": {
        "datetime": "2/2/2011 12:22 pm"
    }
}
# print the datetime of the receipt where id == 2: (list/array index starts at 0)
print(receipt_dictionary_of_ids["2"]["datetime"])

items = [
    {
        "id": 1,
        "name": "widget",
        "price": 111.11
    },
    {
        "id": 2,
        "name": "gadget",
        "price": 222.22
    }
]

lines = [
    {
        "id": 1,
        "qty": 3,
        "item_id": 1,
        "receipt_id": 1
    },
    {
        "id": 1,
        "qty": 2,
        "item_id": 1,
        "receipt_id": 2
    },
    {
        "id": 1,
        "qty": 2,
        "item_id": 1,
        "receipt_id": 2
    }
]

# nested
hierarchical_receipts = [
    {
        "id": 1,
        "datetime": "1/1/2011 12:11 pm",
        "lines": [
            {
                "id": 1,
                "qty": 3,
                "item_id": 1,
                "receipt_id": 1,
                "item": {
                    "id": 1,
                    "name": "widget",
                    "price": 111.11
                }

            }
        ]
    },
    {
        "id": 2,
        "datetime": "2/2/2011 12:22 pm",
        "lines": [
            {
                "id": 1,
                "qty": 2,
                "item_id": 1,
                "receipt_id": 2,
                "item": {
                    "id": 1,
                    "name": "widget",
                    "price": 111.11
                }
            },
            {
                "id": 1,
                "qty": 2,
                "item_id": 1,
                "receipt_id": 2,
                "item": {
                    "id": 2,
                    "name": "gadget",
                    "price": 222.22
                }

            }
        ]

    }
]


def print_all_receipt_totals():
    for r in receipts:
        total = 0
        for line in lines:
            # does this line belong to this receipt?
            if line["receipt_id"] == r["id"]:

                # item = get_item(line["item_id"])

                # find item that this line 'points' to
                for i in items:
                    print(i)
                    # is this the item this line points to via item_id
                    if i["id"] == line["item_id"]:
                        # its a match!
                        item = i
                        # stop the for i in items loop
                        break

                total += line["qty"] * item["price"]
        print(r["id"], r["datetime"], total)


def hierarchical_print_all_receipt_totals():
    for r in hierarchical_receipts:
        total = 0
        for line in r["lines"]:
            item = line["item"]
            total += line["qty"] * item["price"]
        print(r["id"], r["datetime"], total)


# def get_item(item_id):
# for i in items:
# if i["id"] == item_id:
# return i
# return None

print_all_receipt_totals()
hierarchical_print_all_receipt_totals()
# prints: 1 1/1/2011 12:34 pm 370.35

teas = [
    {
        "name": "black",
        "subtypes": [
            "oolong",
            "earl grey"
        ]
    },
    {
        "name": "herbal",
        "subtypes": [
            "peppermint",
            "chamomile"
        ]
    }
]

