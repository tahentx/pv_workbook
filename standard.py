from __future__ import division
grades1 = [68, 71, 81, 90, 92]
grades2 = [78, 83, 85, 85, 87]

all_students = grades2 + grades1
mean = sum(all_students) / len(all_students)
differences_total = []

for x in all_students:
    diff = x - mean
    differences_total.append(diff)

print(differences_total)
