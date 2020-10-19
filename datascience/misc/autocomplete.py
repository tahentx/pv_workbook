def autocomplete(input_, dictionary):
    length = len(input_)
    for x in dictionary:
        if x.isalpha() == True:
            pass
        else:
            x = ''
    answer = [word for word in dictionary if word[:length] == input_]
    print(answer)
# autocomplete('ai', ['airplane','airport','apple','ball'])

def duplicate_sandwich(arr):
    base = range(0, len(arr))
    joined = zip([arr.index(a) for a in arr], base)
    for member in joined:
        if member[0] != member[1]:
            front, back = member[0], member[1]
            print(arr[front])
            print((arr[back]))

duplicate_sandwich(["hi","hey", "hello","howdy","hey"])