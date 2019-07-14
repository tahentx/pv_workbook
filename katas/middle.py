# codewars kata: https://www.codewars.com/kata/get-the-middle-character/train/python

def get_middle(s):
  word = list(s)
  if len(word) % 2 == 0:
      del word[0]
      del word[-1]
      print(word)




get_middle("Kombucha")
