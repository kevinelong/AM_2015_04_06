data = [
    {
        "id": 123,
        "name": "Kevin",
        "role": "Instructor"
    },
    {
        "id": 73,
        "name": "Bob",
        "role": "Student"
    }
]

key_field = "id"
output = {}

for item in data:
    values = []
    output_key = ""

    for k in item.keys():
        if k == key_field:
            output_key = item[k]
        else:
            values.append(item[k])
    output[output_key] = values

print(output)