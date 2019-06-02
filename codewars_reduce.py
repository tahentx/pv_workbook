text = input("Test word:")
dups = []
def duplicate_count(text):
    for x in text:
        if text.count(x) > 1:
            dups.append(x)
            print(x + " has a duplicate value.")
            print(dups)
duplicate_count(text)
