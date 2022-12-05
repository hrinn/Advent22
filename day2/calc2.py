# rock - A
# paper - B
# scissors - C

rock_moves = {
    'X' : 'C',  # lose
    'Y' : 'A',  # draw
    'Z' : 'B',  # win
}

paper_moves = {
    'X' : 'A',  # lose
    'Y' : 'B',  # draw
    'Z' : 'C',  # win
}

scissors_moves = {
    'X' : 'B',  # lose
    'Y' : 'C',  # draw
    'Z' : 'A',  # win
}

def result_to_score(result):
    if result == 'X':
        return 0
    if result == 'Y':
        return 3
    if result == 'Z':
        return 6

def move_to_score(move):
    return ord(move) - ord('A') + 1

def calculate_score(other_move, result):
    if other_move == 'A':
        return result_to_score(result) + move_to_score(rock_moves.get(result))
    if other_move == 'B':
        return result_to_score(result) + move_to_score(paper_moves.get(result))
    if other_move == 'C':
        return result_to_score(result) + move_to_score(scissors_moves.get(result))

    raise Exception(f'invalid other move: {other_move}')

def main(filename):
    f = open(filename, "r")
    total_score = 0

    for line in f.readlines():
        actions = line.strip().split()
        total_score = total_score + calculate_score(actions[0], actions[1])

    print(total_score)

main('input')

# print(calculate_score('A', 'Y'))
# print(calculate_score('B', 'X'))
# print(calculate_score('C', 'Z'))