size = 9
bias = 4


def proceed(number, w):
    # Рассчитываем взвешенную сумму
    net = 0
    for i in range(size):
        net += int(number[i])*w[i]
    return net >= bias


true_weights = []
with open('true_weights.txt', 'r') as tw:
    for line in tw:
        true_weights.append(int(line))


def check(item):
    return proceed(item, true_weights)


with open('field.txt', 'r') as f:
    with open('not_crosses.txt', 'w') as nc:
        with open('all_crosses.txt', 'w') as cr:
            for line in f:
                l = line[:-1]
                if check(l):
                    cr.write(l+'\n')
                else:
                    nc.write(l+'\n')
