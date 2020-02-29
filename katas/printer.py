# Codewars kata: https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
  errors = []
  colors = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  get_errors = [errors.append(x) for x in s if x not in colors]
  count = 0
  for y in s:
      if y in colors:
          count = count + 1
  total = len(errors) + count
  print("Error rate: " + str(count) + "/" + str(total))
printer_error("boo")
