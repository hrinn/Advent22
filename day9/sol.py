import sys

dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


def distance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def vector(head, tail):
    return (head[0] - tail[0], head[1] - tail[1])


def clamp(n):
    return sorted((-1, n, 1))[1]


def clamp_vector(v):
    return (
        clamp(v[0]),
        clamp(v[1])
    )


def sol(filename, rope_length):
    f = open(filename, "r")

    head = (0, 0)
    tail = (0, 0)

    positions = set((0, 0))

    for line in f.readlines():
        op, num = (line.strip().split())
        num = int(num)

        for _ in range(num):
            head = add(head, dirs.get(op))

            if distance(head, tail) > rope_length:
                v = clamp_vector(vector(head, tail))
                tail = add(tail, v)
                positions.add(tail)

    print(len(positions))


sol(sys.argv[1], 1)
sol(sys.argv[1], 10)
