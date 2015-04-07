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
        if item.keys() == key_field:
            result_key = item[key_field]
        else:
            result_item.append(item)
        result[result_key] = result_item
    return result

print transform(d, 'id')
