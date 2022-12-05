def findCommonCharacter(group):
    return set(group[0]).intersection(group[1], group[2]).pop()

def getPriority(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27

def priority_sum(filename):
    f = open(filename, "r")

    priority_sum = 0
    lines = f.readlines()

    for i in range(0, len(lines), 3):
        group = list(map(lambda line: line.strip(), lines[i:i + 3]))
        char = findCommonCharacter(group)
        priority = getPriority(char)
        priority_sum = priority_sum + priority

        print(group, char, priority)

    return priority_sum

print(priority_sum("test"))