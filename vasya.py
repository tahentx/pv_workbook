avengers_ticket = 25
people = [25,25,50,50,100]
cash_on_hand = [25,25,50,50]
def tickets(people, cash_on_hand):
    if sum(cash_on_hand) < (people[-1] - 25):
        print("this is not feasible.")
    else:
        print("this works.")
tickets(people, cash_on_hand)
