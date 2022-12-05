def print_stacks(stacks):
    for stack in stacks:
        print(stack)

def main(filename):
    f = open(filename, "r")

    stack_lines = 0

    lines = f.readlines()

    # Determine number of stacks
    for line in lines:
        stack_lines = stack_lines + 1
        if line == '\n':
            break

    num_stacks = int(lines[stack_lines - 2][-3])

    print(f"{num_stacks} stacks")

    stacks = [[] for stack in range(num_stacks)]

    # Set initial stack contents
    for i in range(stack_lines - 2):
        stack_selector = 0
        for j in range(1, len(lines[i]), 4):
            if lines[i][j] != ' ':
                stacks[stack_selector].insert(0, lines[i][j])
            stack_selector = stack_selector + 1

    print("Initial")
    print_stacks(stacks)

    # Follow instructions
    for i in range(stack_lines, len(lines)):
        ops = lines[i].strip().split()
        
        num = int(ops[1])
        src = int(ops[3])
        dst = int(ops[5])
    
        stacks[dst - 1].extend(stacks[src - 1][-num:])
        del stacks[src - 1][-num:]
            
    # Print results
    print("Final")
    print_stacks(stacks)
    tops = ""

    for stack in stacks:
        tops = tops + stack.pop()

    print(tops)

main("example")

main("input")