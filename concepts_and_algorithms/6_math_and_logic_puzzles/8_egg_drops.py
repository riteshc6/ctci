# Simulation of problem

breaking_point = 89   # suppose
count_drops = 0

def drop(floor: int):
    return floor >= breaking_point


def find_breaking_point(floors):
    interval = 14
    previous_floor = 0
    egg1 = interval

    while (not drop(egg1)) and egg1 <= floors:
        interval -= 1
        previous_floor = egg1
        egg1 += interval

    egg2 = previous_floor + 1
    while (egg2 < egg1) and (egg2 <= floors) and (not drop(egg2)):
        egg2 += 1

    return -1 if egg2 > floors else egg2

print(find_breaking_point(100))

