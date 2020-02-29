def number(lines):
  output = []
  for index, value in list(enumerate(lines, 1)):
      output.append('{}: {}'.format(index, value))
  return output
number(["ab","cd","ef"])
