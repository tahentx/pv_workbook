text = input("Test word:")
def duplicate_count(text):
    copy = text
    for x in copy:
        if copy.count(x) > 1:
            print(x + " has a duplicate value.")
duplicate_count(text)
