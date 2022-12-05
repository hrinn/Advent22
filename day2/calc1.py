rock_results = {
    'A' : 3,    # rock
    'B' : 0,    # paper
    'C' : 6,    # scissors
}

paper_results = {
    'A' : 6,    # rock
    'B' : 3,    # paper
    'C' : 0,    # scissors
}

scissors_results = {
    'A' : 0,    # rock
    'B' : 6,    # paper
    'C' : 3,    # scissors
}

def calculate_score(other_move, my_move):
    if my_move == 'X':
        return 1 + rock_results.get(other_move)
    if my_move == 'Y':
        return 2 + paper_results.get(other_move)
    if my_move == 'Z':
        return 3 + scissors_results.get(other_move)

    raise Exception(f"Invalid my_move: {my_move}")

def main(filename):
    f = open(filename, "r")
    total_score = 0

    for line in f.readlines():
        actions = line.strip().split()
        total_score = total_score + calculate_score(actions[0], actions[1])

    print(total_score)

main('input')