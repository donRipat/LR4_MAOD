import random

width = 3
height = 3
size = width * height

train = []
with open('dataset.txt', 'r') as f:
    for line in f:
        train.append(line[:-1])

test = [    # first half items are crosses
    '101'
    '010'
    '101',

    '111'
    '010'
    '101',

    '101'
    '000'
    '101',

    '001'
    '010'
    '101',

    # no crosses left

    '111'
    '110'
    '101',

    '011'
    '010'
    '101',

    '111'
    '111'
    '101',

    '100'
    '000'
    '101',

    '100'
    '110'
    '100',

    '111'
    '111'
    '000'
]


# Инициализация весов сети
weights = []
for i in range(size):
    weights.append(0)

# Порог функции активации
bias = 4


# Является ли данное число 5
def proceed(number, w):
    # Рассчитываем взвешенную сумму
    net = 0
    for i in range(size):
        net += int(number[i])*w[i]
    return net >= bias


# Уменьшение значений весов, если сеть ошиблась и выдала 1
def decrease(number):
    for i in range(size):
        weights[i] -= int(number[i])


# Увеличение значений весов, если сеть ошиблась и выдала 0
def increase(number):
    for i in range(size):
        weights[i] += int(number[i])


true_weights = []
with open('true_weights.txt', 'r') as tw:
    for line in tw:
        true_weights.append(int(line))


def check(item):
    return proceed(item, true_weights)


def predict(item):
    return proceed(item, weights)


# Тренировка сети
for i in range(len(train)):
    option = random.randint(0, len(train) - 1)
    item = train[option]
    thinks_that_cross = predict(item)
    in_fact_a_cross = check(item)
    if thinks_that_cross and not in_fact_a_cross:
        decrease(item)
    elif not thinks_that_cross and in_fact_a_cross:
        increase(item)

# Вывод значений весов
print('true weights    =', true_weights)
print('trained weights =', weights)
print('Test dataset results:')

for i in test:
    print(str.ljust(str(proceed(i, true_weights)), 6), proceed(i, weights))

