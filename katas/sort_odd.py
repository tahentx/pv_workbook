# codewars kata: https://www.codewars.com/kata/sort-the-odd/train/python
def sort_array(source_array):
  even_list = []
  for i in source_array:
      if i % 2 == 0:
          even_list.append(i)
      else:
          print("odd")
  print(even_list)
  print(source_array)

sort_array([4,2,6,3,9])
