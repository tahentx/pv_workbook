# codewars kata: https://www.codewars.com/kata/sort-the-odd/train/python
def sort_array(source_array):
  odd_array = []
  for i in source_array:
      if i % 2 > 0:
          odd_array.append(i)
  odd_array.sort()
  print(odd_array)
sort_array([4,2,9,17,3,1])
