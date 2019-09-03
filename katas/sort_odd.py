# codewars kata: https://www.codewars.com/kata/sort-the-odd/train/python
def sort_array(source_array):
  for i in source_array:
      if i % 2 > 0:
          source_array.insert(0,i)
  print(source_array)
sort_array([4,2,6,3,9])
