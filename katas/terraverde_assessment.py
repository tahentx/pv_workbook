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
def lineFromPoints(coord1,coord2):
    # The first step is to calculate the slope of the line
    a = coord1[1] - coord2[1]
    b = coord1[0] - coord2[0]
    c = a/b
    print(c)
    # Next step is to create the slope of a perpendicular line
    # int_vector = -1/c
    #
    # y = (int_vector * (b - 3)) + 2





# Driver code
if __name__=='__main__':
    P = [-3,-3]
    Q = [3,1]
    lineFromPoints(P,Q)
