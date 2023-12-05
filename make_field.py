with open('field.txt', 'w') as f:
    size = 2**9
    for i in range(size):
        print(str(bin(i))[2:].rjust(9, '0'))
        f.write(str(bin(i))[2:].rjust(9, '0') + '\n')

    for i in range(49):
        with open('all_crosses.txt', 'r') as crosses:
            for line in crosses:
                f.write(line)
