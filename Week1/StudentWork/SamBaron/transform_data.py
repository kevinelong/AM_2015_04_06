""" Convert list of dictionary objects to
        dictionary of objects
        where the key=id and values=property list
"""


# Original dictionary
orig_dict = [
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


def transform1_prop_hardcode(input_list):
    """
        Convert List of Dictionaries to
            Dictionary of Lists

        Loop through Objects
        Hard code properties
    """
    output_dict = dict()

    # Loop through objects in list
    for obj in input_list:
        # Set object key
        object_key = obj["id"]

        # Set value list
        value_list = [obj["name"], obj["role"]]

        # Append new object to output dictionary
        output_dict[object_key] = value_list

    return output_dict


def transform2_prop_loop(input_list):
    """
        Convert List of Dictionaries to
            Dictionary of Lists

        Loop through Objects AND
        Loop though Properties
    """
    output_dict = dict()

    # Loop through objects in list
    for obj in input_list:

        # Set object key
        object_key = obj["id"]

        # Loop through properties to build value list
        value_list = []
        for prop in obj:
            # Ignore 'id' property
            if prop != "id":
                # Append to value list
                value_list.append(obj[prop])

        # Append new object to output dictionary
        output_dict[object_key] = value_list

    return output_dict


def transform3_abstract_id(input_list, id_field):
    """
        Convert List of Dictionaries to
            Dictionary of Lists

        Loop through Objects AND
        Loop though Properties AND
        Abstract ID
    """
    output_dict = dict()

    # Loop through objects in list
    for obj in input_list:

        # Set object key
        object_key = obj[id_field]

        # Loop through properties to build value list
        value_list = []
        for prop in obj:
            # Ignore 'id' property
            if prop != id_field:
                # Append to value list
                value_list.append(obj[prop])

        # Append new object to output dictionary
        output_dict[object_key] = value_list

    return output_dict


if __name__ == "__main__":
    # Set property index constants
    NAME = 0
    ROLE = 1
    # Convert list to dictionary
    new_dict = transform3_abstract_id(orig_dict, "id")
    # Test new dictionary object
    print(new_dict)
    print(new_dict[73][NAME], new_dict[73][ROLE])
