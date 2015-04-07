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

#loopless solution
# result = {
#     data[0]["id"]: [data[0]["name"], data[0]["role"]],
#     data[1]["id"]: [data[1]["name"], data[1]["role"]],
# }


def transform(input_list, key_field):
    output = {}

    for item in input_list:
        values = []
        output_key = ""

        #hardcoded inner rather than inner loop solution
        # output["id"] = [item["name"], item["role"]]

        for k in item.keys():
            if k == key_field:
                output_key = item[k]
            else:
                values.append(item[k])
        output[output_key] = values
    return output


if __name__ == '__main__':
    # run tests if invoked as a script rather than a module
    result = transform(data, "id")
    print(result)

    NAME = 0
    ROLE = 1
    item = result[123]
    print(item[NAME], item[ROLE])

