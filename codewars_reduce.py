text = input("Test word:")
def duplicate_count(text):
    for x in text:
        if text.count(x) > 1:
            print(x + " has a duplicate value.")
duplicate_count(text)
