def findCommonCharacter(a, b):
    for char in a:
        if char in b:
            return char

    return None

def getPriority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27

def priority_sum(filename):
    f = open(filename, "r")

    priority_sum = 0

    for line in f.readlines():
        line = line.strip()
        one, two = line[:len(line)//2], line[len(line)//2:]

        char = findCommonCharacter(one, two)
        priority = getPriority(char)
        priority_sum = priority_sum + priority

        print(one, two, char, priority)

    return priority_sum

print(priority_sum("test"))