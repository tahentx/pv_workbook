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

def lineFromPoints(P,Q):

    a = Q[1] - P[1]
    b = P[0] - Q[0]
    c = a*(P[0]) + b*(P[1])

    if(b<0):
        print("The line passing through points P and Q is:",
              a ,"x ",b ,"y = ",c ,"\n")
    else:
        print("The line passing through points P and Q is: ",
              a ,"x + " ,b ,"y = ",c ,"\n")

# Driver code
if __name__=='__main__':
    P = [2, 5]
    Q = [6, 9]
    lineFromPoints(P,Q)
