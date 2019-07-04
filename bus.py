import random
bus_stops = 5
while bus_stops >= 0:
    total = 10
    x = lambda a, b, c : a + b - c
    print(x(total, random.randint(0, 5), random.randint(2, 5)))
    bus_stops = bus_stops - 1
