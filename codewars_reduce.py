text = input("Test word:")
def duplicate_count(text):
    upper = text.upper()
    for x in upper:
        if upper.count(x) > 1:
            print(x + " has a duplicate value.")
duplicate_count(text)
