from __future__ import division
grades1 = [68, 71, 81, 90, 92]
grades2 = [78, 83, 85, 85, 87]

all_students = grades2 + grades1
mean = sum(all_students) / len(all_students)

differences_total = []
def find_diff(all_students):
    for x in all_students:
        diff = x - mean
        differences_total.append(diff)
find_diff(all_students)

differences_total_sq = []
def sq_diff(differences_total):
    for x in differences_total:
        sq = lambda x: x ** 2
        differences_total_sq.append(sq(x))
sq_diff(differences_total)

variance = (sum(differences_total_sq) / len(differences_total_sq))
print("The variance for the entire class is " + str(variance))
standard_dev = variance / len(all_students)
print("The standard deviation for the entire class is " + str(standard_dev))
