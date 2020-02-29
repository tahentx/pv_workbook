# Codewars kata: https://www.codewars.com/kata/if-you-cant-sleep-just-count-sheep/train/python

def count_sheep(i: int) -> str():
    i = 1
    text = " sheep.."
    while i < 6:
      print(str(i) + text * i)
      i += 1


print(count_sheep(5))
