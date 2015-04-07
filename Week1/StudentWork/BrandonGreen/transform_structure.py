d = [
    {
        'id': 123,
        'name': 'kevin',
        'role': 'instructor'
    },
    {
        'id': 456,
        'name': 'brandon',
        'role': 'student'
    }
]

def transform(input_list, key_field):
    result = {}
    for item in input_list:
        result_item = []
        result_key = ''
        for key in item.keys():
            if key == key_field:
                result_key = item[key]
            else:
                result_item.append(item)
        result[result_key] = result_item
        return result


print transform(d, 'id')
