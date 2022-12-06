def all_differ(part):
    return len(set(part)) == len(part)

def start_of_packet(filename):
    f = open(filename, "r")

    line = f.readlines()[0]

    for i in range(4, len(line)):
        sub = line[i-4:i]
        if all_differ(sub):
            return i

def start_of_message(filename):
    f = open(filename, "r")

    line = f.readlines()[0]

    for i in range(14, len(line)):
        sub = line[i-14:i]
        if all_differ(sub):
            return i

print(start_of_packet('example'))
print(start_of_packet('input'))

print(start_of_message('example'))
print(start_of_message('input'))