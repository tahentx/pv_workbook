def solution(number):
    container = []
    counter = 0
    while sum(container) < number:
        container.append(counter+3)
        if sum(container) < number:
            print(sum(container))
        

solution(13)
