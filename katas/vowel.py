def getCount(inputStr):
    string = input("Enter your string: ")
    num_vowels = 0
    y = ["a","e","i","o","u"]
    if y[0] in string:
        num_vowels = num_vowels + 1
    elif y[1] in string:
        num_vowels = num_vowels + 1
    elif y[2] in string:
        num_vowels = num_vowels + 1
    elif y[3] in string:
        num_vowels = num_vowels + 1
    elif y[4] in string:
        num_vowels = num_vowels + 1
    print(num_vowels)


getCount("Blood")
