def convert_section(section):
    numbers = list(map(lambda num: int(num), section.split('-')))
    return numbers

def sections_overlap(sections):
    sec1 = convert_section(sections[0])
    sec2 = convert_section(sections[1])

    return sec1[1] >= sec2[0] and sec1[0] <= sec2[1] or sec1[0] >= sec2[1] and sec1[1] <= sec2[0]


def main(filename):
    f = open(filename, "r")

    overlap_count = 0

    for line in f.readlines():
        sections = line.strip().split(',')
        if sections_overlap(sections):
            overlap_count = overlap_count + 1
            print(sections, "overlap")
        else:
            print(sections, "no")

    print(overlap_count)

main('input')