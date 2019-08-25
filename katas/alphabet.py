# codewars kata alphabet replacement: https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
place = []
for i in letter:
    place.append(letter.index(i))
assert len(place) == 26
x = dict(zip(letter,place))
print(x)
