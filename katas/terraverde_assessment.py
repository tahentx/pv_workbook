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
def lineFromPoints(P,Q) -> list:

    # The first step is to calculate the slope of the line
    a = P[1] - Q[1]
    b = P[0] - Q[0]
    slope = a/b
    # Next step is to create the slope of a perpendicular line
    inverse_slope = -1/slope
    # Create empty list to store the three distinct perpendicular lines that cross the input set
    intercept = []

    # Create first line
    x_0 = 0
    x_1 = Q[0]
    y_0 = 0

    for i in range(3):
        y_1 = inverse_slope * (x_1 - x_0) + y_0
        point = [x_1,y_1]
        intercept.append(point)
        y_0 = y_0 + 1

    test = [[1,1],[1,1],[1,1]]
    mapped = zip(intercept,test)
    print(tuple(mapped))

    # coordinates = list(map(lambda y : y + 5, ))
    #


if __name__=='__main__':
    P = [3, 2]
    Q = [2, 6]
    lineFromPoints(P,Q)
