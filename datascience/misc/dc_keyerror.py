ages = {
    "Bob": 40,
    "Bill": 43,
    "Joe": 23 
    }

person = input("Get age for: ")

try:
    print("{} is {} years old.".format(person, ages[person]))
except KeyError:
    print("{}'s age is unknown.".format(person))