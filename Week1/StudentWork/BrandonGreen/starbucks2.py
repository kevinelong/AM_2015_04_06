__author__ = 'Brandon'

data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
        [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
        [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
        [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
        [117, 546, 'Y'], [507, 127, 'Z']]

square_size = 600

style = """
<style>
    #box { background:blue; position:relative; }
    #box span { color:white; position:absolute; }
</style>
"""


import math


X_COORD_INDEX = 0
Y_COORD_INDEX = 1
KEY_INDEX = 2


def nearest_starbucks(input_data, selection, nearby_count):

    input_keys = [item[KEY_INDEX] for item in input_data]
# Check if selection is in input_data
    if selection in input_keys:
        selected_point = input_data[input_keys.index(selection)]
# Leave function if selection is not in input_data
    else:
        print("That selection is not in the given list.")
        return

    distances_list = []
    x_coord = selected_point[X_COORD_INDEX]
    y_coord = selected_point[Y_COORD_INDEX]
    selected_key = selected_point[KEY_INDEX]

    for data_point in input_data:
        x_test = data_point[X_COORD_INDEX]
        y_test = data_point[Y_COORD_INDEX]
        distance_key = data_point[KEY_INDEX]
        distance = math.sqrt((abs(x_coord - x_test) ** 2) + (abs(y_coord - y_test) ** 2))
        if selected_key not in data_point:
            distances_list.append([distance, distance_key])

    sorted_distances = sorted(distances_list, key=lambda l: l[0])
    result = sorted_distances[0:int(nearby_count)]
    result_keys = []

    for data_point in result:
        result_key = data_point[1]
        result_keys.append(result_key)

    f = open("positions.html", "width")
    f.write(style)
    f.write('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))

    for item in input_data:
        item_key = item[KEY_INDEX]
        if item_key in result_keys:
            f.write('<span style="left:{x}px; top:{y}px; background-color:yellow; color:black; > {v} </span>'.format(x=item[0], y=item[1], v=item[2]))
            print(item_key, 'result')
        elif item_key in selected_key:
            f.write('<span style="left:{x}px; top:{y}px; background-color:green; > {v} </span>'.format(x=item[0], y=item[1], v=item[2]))
            print(item_key, 'selected')
        else:
            f.write('<span style="left:{x}px; top:{y}px;"> {v} </span>'.format(x=item[0], y=item[1], v=item[2]))
            print(item_key)

    f.write("</div>\n")
    f.close()

    print(result_keys)

<<<<<<< HEAD

nearest_starbucks(data, 'I', 5)
=======
nearest_starbucks(data, 'H', 5)

# Test Pushing
>>>>>>> dce481137a57caaa673b96d37aed0ea34fba61dd
