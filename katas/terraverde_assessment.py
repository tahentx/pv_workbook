# def create_intersection(coordinates: list) -> list:
#
#     line1 = coordinates[0]
#     line2 = coordinates[1]
#
#     # xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
#     # ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
#
#     print(line1)
#
# create_intersection([[5,4],[7,5]])




#
def lineFromPoints(coordinate_set = [], *args):

    # The first step is to calculate the slope of the line
    a = coords1[1] - coords2[1]
    b = coords1[0] - coords2[0]
    slope = a/b

    # Next step is to create the slope of a perpendicular line
    inverse_slope = -1/slope

    intersecting_lines = []

    for i in range(3):
        x_intercept = inverse_slope * (coord1[0] - i)
        i = i + 5
        intersecting_lines.append([x_intercept,coord1[1]])
    print(intersecting_lines)


lineFromPoints()
