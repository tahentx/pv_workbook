avengers_ticket = 25
people = [25,25,50,50,100]
cash_on_hand = [25,25,50,50]
def tickets(people, cash_on_hand):
    if sum(cash_on_hand) < (people[-1] - 25):
        print("this is not feasible.")
    elif (sum(cash_on_hand)%50==0 and (people[-1]%25==0)):
        print("do not have the right combination of bills")
    else:
        print("this works.")
tickets(people, cash_on_hand)
