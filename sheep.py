# Codewars kata: https://www.codewars.com/kata/if-you-cant-sleep-just-count-sheep/train/python

def count_sheep(n):
    loop_counter = n
    sheep_counter = 1
    while loop_counter > 0:
        print(str(sheep_counter) + " sheep..." * sheep_counter)
        sheep_counter + 1
        if loop_counter == 1:
            break
        loop_counter - 1
