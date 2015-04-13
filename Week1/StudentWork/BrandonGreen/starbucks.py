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


def nearest_starbucks(input_data, selected_point):

    distances_list = []
    x_coord = selected_point[0]
    y_coord = selected_point[1]
    selected_key = selected_point[2]

    for data_point in input_data:
        x_test = data_point[0]
        y_test = data_point[1]
        distance_key = data_point[2]
        distance = math.sqrt((abs(x_coord - x_test) ** 2) + (abs(y_coord - y_test) ** 2))
        if selected_key not in data_point:
            distances_list.append([distance, distance_key])

    sorted_distances = sorted(distances_list, key=lambda l: l[0])
    result = sorted_distances[0:5]
    result_keys = []

    for data_point in result:
        result_key = data_point[1]
        result_keys.append(result_key)

    f = open("positions.html", "w")
    f.write(style)
    f.write('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))

    for item in data:
        item_key = item[2]
        if item_key in result_keys:
            f.write('<span style="left:{x}px; top:{y}px; background-color: yellow; color: black"> {v} </span>'.format(x=item[0], y=item[1], v=item[2]))
        elif item_key in selected_key:
            f.write('<span style="left:{x}px; top:{y}px; background-color: green"> {v} </span>'.format(x=item[0], y=item[1], v=item[2]))
        else:
            f.write('<span style="left:{x}px; top:{y}px;"> {v} </span>'.format(x=item[0], y=item[1], v=item[2]))

    f.write("</div>\n")
    f.close()


nearest_starbucks(data, data[7])