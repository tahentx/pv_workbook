def queue_time(customers: list, stations: int) -> int:
    if stations == 1:
        print(sum(customers))

queue_time([5,5], 1)
