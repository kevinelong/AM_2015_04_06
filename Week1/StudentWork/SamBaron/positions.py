from math import sqrt

X_POSITION_INDEX = 0
Y_POSITION_INDEX = 1
LOCATION_ID_INDEX = 2

data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'],
        [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'],
        [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'],
        [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'],
        [117, 546, 'Y'], [507, 127, 'Z']]
square_size = 600


def return_nearest_neighbors(all_locations, selected_location, neighbor_count):

    selected_x_position = 0
    selected_y_position = 0
    neighbor_distances = []
    nearest_neighbors = []

    # Set selected location X/Y coordinates
    for location in all_locations:
        if location[LOCATION_ID_INDEX] == selected_location:
            selected_x_position = location[X_POSITION_INDEX]
            selected_y_position = location[Y_POSITION_INDEX]

    # Loop through each location
    for location in all_locations:

        if location[LOCATION_ID_INDEX] != selected_location:
            neighbor_id = location[LOCATION_ID_INDEX]

            x_position = location[X_POSITION_INDEX]
            x_difference = x_position - selected_x_position

            y_position = location[Y_POSITION_INDEX]
            y_difference = y_position - selected_y_position

            distance = sqrt((x_difference**2) + (y_difference**2))
            neighbor_distances.append([distance, neighbor_id])

    neighbor_distances.sort()
    for i in range(neighbor_count):
        nearest_neighbors.append(neighbor_distances[i][1])

    return nearest_neighbors


selected_position = "T"
neighbor_count = 5
nearest_neighbor_list = return_nearest_neighbors(data, selected_position, neighbor_count)

style = """
<style>
    #box { background:blue; position:relative; }
    #box span { color:white; position:absolute; }
    #box .nearest { color:red; }
    #box .selected { background:yellow; color:green; }
</style>
"""

f = open("positions.html", "w")
f.write(style)
f.write('<div id="box" style="width:{0}px;height:{0}px;">\n'.format(square_size))
for item in data:
    position_id = item[LOCATION_ID_INDEX]
    position_html_class = ""
    if position_id is selected_position:
        position_html_class = "class='selected'"
    if position_id in nearest_neighbor_list:
        position_html_class = "class='nearest'"
    f.write('<span {html_class} style="left:{x}px; top:{y}px;"> {v} </span>'.format(x=item[0], y=item[1], v=item[2], html_class=position_html_class))
f.write("</div>\n")
f.close()

# TODO NEAREST "STARBUCKS"
# 1. Define a function that for arbitrary value e.g. "J" find the nearest N items e.g. 5
#   a. calculate the distance to each neighbor
#   b. sort the list by that distance
#   c. return the top N from the sorted list
# 2. Modify the draw code to highlight "top" items
#   a. add a style property for color
#   b. determine if this item is in the top 5
#   c. conditionally set the color bases on if its the top 5
#   d. also indicate the selected position e.g. "J" with another color

# OUTPUT html for "J" and 5 would show R D N U and T highlighted.
