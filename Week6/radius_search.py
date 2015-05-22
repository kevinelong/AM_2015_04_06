from math import sqrt

data = [[-531, 408, 'A'], [-225, 52, 'B'], [-594, 242, 'C'], [-351, 102, 'D'], [-371, 15, 'E'], [-569, 353, 'F'],
        [-342, 39, 'G'], [-218, 304, 'H'], [-428, 260, 'I'], [-329, 158, 'J'], [-585, 530, 'K'], [-71, 114, 'L'],
        [-587, 88, 'M'], [-347, 180, 'N'], [-180, 332, 'O'], [-250, 522, 'P'], [-88, 475, 'Q'], [-260, 128, 'R'],
        [-328, 505, 'S'], [-381, 201, 'T'], [-360, 192, 'U'], [-414, 313, 'V'], [-525, 293, 'W'], [-240, 563, 'X'],
        [-117, 546, 'Y'], [-507, 127, 'Z']]


def filter_by_distance(all_locations, lat, long, radius_limit):
    output_list = []
    for location in all_locations:
        distance = sqrt(((location[0] - lat) ** 2) + ((location[1] - long) ** 2))
        if distance < radius_limit:
            output_list.append(location)
    return output_list


results = filter_by_distance(data, -200, 200, 140)
print(data)
print(results)
