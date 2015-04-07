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


def transform(input_list):
    key_field = "id"
    output = {}

    for item in input_list:
        values = []
        output_key = ""

        for k in item.keys():
            if k == key_field:
                output_key = item[k]
            else:
                values.append(item[k])
        output[output_key] = values
    return output


result = transform(data)
print(result)

NAME = 0
ROLE = 1
print(result[123][NAME], result[123][ROLE])