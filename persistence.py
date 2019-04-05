n = 38941
value = [int(x) for x in str(n)]
persist = value[0] * value[1]
next_value = [int(x) for x in str(persist)]
persist_again = next_value[0] * next_value[1]
print(str(persist_again)
