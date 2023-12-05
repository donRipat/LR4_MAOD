import math
import random

crosses = []
with open('all_crosses.txt', 'r') as f:
    for line in f:
        crosses.append(line[:-1])

not_crosses = []
with open('not_crosses.txt', 'r') as f:
    for line in f:
        not_crosses.append(line[:-1])


def pick_from(ds):
    position = random.randint(0, len(ds) - 1)
    return ds[position] + '\n'


with open('dataset.txt', 'w') as ds:
    for i in range(math.floor(.9*2**9)):
        if random.randint(0, 1):
            ds.write(pick_from(crosses))
        else:
            ds.write(pick_from(not_crosses))
