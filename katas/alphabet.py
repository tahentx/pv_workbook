# codewars kata alphabet replacement: https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
submission = input("Provide text input: ")
copy = list(submission)
output = []
for x in copy:
    if x in letter:
        output.append(letter.index(x))

print(output)
