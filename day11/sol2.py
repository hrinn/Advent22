import sys
import operator

ops = {
    '*': operator.mul,
    '+': operator.add,
}

modulo_map = {}

# calculate (x ^ y % p)
def fast_mod_exp(x, y, p):
    prod = pow(x, y, p)
    modulo_map[x ** y] = prod
    return prod

def fast_mod_mul(a, b, p):
    r = 2 ** 32
    r2 = r * r % p
    pinv = pow(-p, -1, r)

    def m_reduce(ab):
        m = ab * pinv % r
        return (ab + m * p) // r

    def m_transform(a):
        return m_reduce(a * r2)

    a_prim = m_transform(a)
    b_prim = m_transform(b)
    prod_prim = m_reduce(a_prim * b_prim)
    prod = m_reduce(prod_prim)

    modulo_map[a * b] = prod

    return prod


# based on (a + b) % p = ((a % p) + (b % p)) % p
# b is small and we have already calculated a % p
def fast_mod_add(a, b, p):
    if modulo_map.get(a) is None:
        modulo_map[a] = a % p

    modulo_map[a + b] = (modulo_map[a] + (b % p)) % p

    return modulo_map[a + b]
    

class Monkey:
    def __init__(self):
        self.inspect_counter = 0

    def parse(self, slice):
        self.num = int(slice[0][-3])
        
        self.items = [int(x) for x in slice[1].strip()[16:].split(", ")]

        operation = slice[2].strip()[11:].split()
        self.operator = operation[3]
        if operation[3] == '*' and operation[4] == 'old':
            self.op_func = operator.pow
            self.op_val = 2
            self.operator = "**"
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

            res = False

            if (self.operator == "**"):
                res = fast_mod_exp(item, 2, self.test_val) == 0
            elif (self.operator == "**"):
                res = fast_mod_mul(item, self.op_val, self.test_val) == 0
            else:
                res = fast_mod_add(item, self.op_val, self.test_val) == 0

            if res:
                monkeys[self.true_monkey].receive(self.op_lambda(item))
            else:
                monkeys[self.false_monkey].receive(self.op_lambda(item))

            self.inspect_counter += 1

    def __str__(self):
        return f"Monkey {self.num}: inspected {self.inspect_counter}"

print_rounds = [1, 20, 1000, 2000, 3000]

def rounds(monkeys, num_rounds):
    for r in range(num_rounds):
        for i in range(len(monkeys)):
            monkeys[i].make_round(monkeys)

        print(r)
        # if r + 1 in print_rounds:
        #     print(f"After Round {r + 1}")
        #     for i in range(len(monkeys)):
        #         print(monkeys[i])


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
    rounds(monkeys, 10000)
    monkey_business(monkeys)

main(sys.argv[1])