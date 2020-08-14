def autocomplete(input_, dictionary):
    length = len(input_)
    answer = [word for word in dictionary if word[:length] == input_]
    return answer
autocomplete('ai', ['airplane','airport','apple','ball'])
