def stat(strg):
    separated_times = strg.split(',')
    for time in separated_times:
        time = time.split("|")
        print(time)
stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17")