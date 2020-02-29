# codewars kata: https://www.codewars.com/kata/get-the-middle-character/train/python

def get_middle(s):
  word = list(s)
  if len(word) % 2 == 0:
      while len(word) > 2:
          del word[0]
          del word[-1]
      x = ''.join(word)
      return x
  else:
      while len(word) > 1:
          del word[0]
          del word[-1]
      return word[0]

get_middle("Plan")
