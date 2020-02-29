# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(string: str, ending: str) -> str:
    if string[-2:] == ending[-2:]:
        return True
    elif ending[-2:] == '':
        return True
    else:
        return False

solution("Ball","Wall")
