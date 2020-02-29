applications = [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

def membership(data: list) -> list:
    assignment = []
    for x in data:
        if x[0] >= 55 and x[1] > 7:
            x = "Senior"
            assignment.append(x)
        else:
            x = "Open"
            assignment.append(x)
    print(assignment)

membership(applications)
