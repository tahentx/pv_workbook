avengers_ticket = 25
people = [100,50,25]

def tickets(people):
    vasya_cash_available = 0
    for x in people:
        if x % 25:
            print("test")
        else:
            print("not feasible")

tickets(people)
