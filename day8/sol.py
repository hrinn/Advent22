def get_up(hmap, x, y):
    return [hmap[i][x] for i in range(y - 1, -1, -1)]

def get_down(hmap, x, y):
    return [hmap[i][x] for i in range(y + 1, len(hmap))]

def get_left(hmap, x, y):
    return [hmap[y][i] for i in range(x - 1, -1, -1)]

def get_right(hmap, x, y):
    return [hmap[y][i] for i in range(x + 1, len(hmap[0]))]

def is_vis(hmap, x, y):
    if x == 0 or x == len(hmap[0]) - 1 or y == 0 or y == len(hmap) - 1:
        return True

    h = hmap[y][x]

    if h > max(get_up(hmap, x, y)):
        return True

    if h > max(get_down(hmap, x, y)):
        return True

    if h > max(get_left(hmap, x, y)):
        return True

    return h > max(get_right(hmap, x, y))

def count_until_ge(n, l):
    count = 0
    for x in l:
        count += 1
        if x >= n:
            break
    return count 

def get_scenic_score(hmap, x, y):
    h = hmap[y][x]
    score = 1
    score *= count_until_ge(h, get_up(hmap, x, y))
    score *= count_until_ge(h, get_down(hmap, x, y))
    score *= count_until_ge(h, get_left(hmap, x, y))
    score *= count_until_ge(h, get_right(hmap, x, y))
    return score


def main(filename):
    f = open(filename, "r")

    hmap = []

    for line in f.readlines():
        hmap.append([int(x) for x in line.strip()])

    # Part 1
    vis_count = 0
    for y in range(len(hmap)):
        for x in range(len(hmap[y])):
            if is_vis(hmap, x, y):
                vis_count += 1

    print("Visible:", vis_count)

    # Part 2
    scenic_scores = []

    for y in range(len(hmap)):
        for x in range(len(hmap[y])):
            scenic_scores.append(get_scenic_score(hmap, x, y))

    print("Best scenic score:", max(scenic_scores))

main("example")
main("input")