import random
bus_stops = 5
start = [random.randint(0, 10),0]
while bus_stops >= 0:
    x = lambda a, b, c : a + b - c
    flow = x(sum(start), random.randint(0, 5), random.randint(2, 5))
    return flow
    bus_stops = bus_stops - 1
