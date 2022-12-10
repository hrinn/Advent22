import sys


def sol(filename):
    f = open(filename, "r")
    
    cycle = 0
    x = 1
    x_histogram = [x]
            
    for line in f.readlines():
        data = line.strip().split()
        
        if data[0] == 'addx':
            for _ in range(2):
                cycle += 1
                x_histogram.append(x)
            x += int(data[1])
        else: # noop
            cycle += 1
            x_histogram.append(x)
            
    cycles = [20, 60, 100, 140, 180, 220]
    sum = 0
    for c in cycles:
        sum += c * x_histogram[c]
    print(sum) 

    i = 0    
    for y in range(6):
        for x in range(40):
            i += 1
            if x_histogram[i] == x or x_histogram[i] == x - 1 or x_histogram[i] == x + 1:
                print("#", end="")
            else:
                print(".", end="")
        print()

sol(sys.argv[1])