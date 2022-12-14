import sys
import operator

ops = {
    '*': operator.mul,
    '+': operator.add,
}

class Monkey:
    def __init__(self):
        self.inspect_counter = 0

    def parse(self, slice):
        self.num = int(slice[0][-3])
        
        self.items = [int(x) for x in slice[1].strip()[16:].split(", ")]

        operation = slice[2].strip()[11:].split()
        if operation[3] == '*' and operation[4] == 'old':
            self.op_func = operator.pow
            self.op_val = 2
        else:
            self.op_func = ops[operation[3]]
            self.op_val = int(operation[4])
        self.op_lambda = lambda old: self.op_func(old, self.op_val)

        self.test_val = int(slice[3].strip().split()[-1])

        self.true_monkey = int(slice[4].strip().split()[-1])

        self.false_monkey = int(slice[5].strip().split()[-1])


    def receive(self, item):
        self.items.append(item)


    def make_round(self, monkeys):
        while len(self.items) > 0:
            item = self.items.pop(0)
            item = self.op_lambda(item)
            item = item // 3

            if item % self.test_val == 0:
                monkeys[self.true_monkey].receive(item)
            else:
                monkeys[self.false_monkey].receive(item)

            self.inspect_counter += 1

    def __str__(self):
        return f"Monkey {self.num}: inspected {self.inspect_counter}"

def rounds(monkeys, num_rounds):
    for r in range(num_rounds):
        for i in range(len(monkeys)):
            monkeys[i].make_round(monkeys)

        print(r)


def parse(filename):
    f = open(filename, "r")
    lines = f.readlines()

    monkeys = {}

    for i in range(0, len(lines), 7):
        monkey = Monkey()
        monkey.parse(lines[i : i+7])
        monkeys[monkey.num] = monkey

    return monkeys

def monkey_business(monkeys):
    inspect_counts = []
    for i in range(len(monkeys)):
        inspect_counts.append(monkeys[i].inspect_counter)

    inspect_counts.sort()
    print(inspect_counts)
    print(inspect_counts[-1] * inspect_counts[-2])

def main(filename):
    monkeys = parse(filename)
    rounds(monkeys, 20)
    monkey_business(monkeys)

main(sys.argv[1])