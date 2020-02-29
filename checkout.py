def queue_time(customers: list, stations: int) -> int:
    if stations == 1:
        return sum(customers)
    for x in customers:
        if x > sum(customers[x:]):
            print("check")
