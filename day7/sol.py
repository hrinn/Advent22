class Node:
    def __init__(self, name, parent, size = None):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def create_directory_tree(filename):
    f = open(filename, "r")

    root = Node("/", None)
    current = None

    for line in f.readlines():
        data = line.strip().split()
        if data[0] == "$":
            # execute command
            if data[1] == "cd":
                if data[2] == "..":
                    current = current.parent
                elif data[2] == "/":
                    current = root
                else:
                    for child in current.children:
                        if child.name == data[2]:
                            current = child
                            break

            elif data[1] == "ls":
                pass
            else:
                raise Exception(f"unknown command {data[1]}")
        else:
            # add directory item to graph
            if data[0] == "dir":
                # directory
                current.add_child(Node(data[1], current))
            else:
                # file
                current.add_child(Node(data[1], current, int(data[0])))

    return root

def set_dir_sizes(node, dir_sizes):
    if node.size is not None:
        return node.size

    # directory, calculate size
    node.size = 0
    for child in node.children:
        node.size = node.size + set_dir_sizes(child)

    # add directory sizes to list
    dir_sizes.append(node.size)

    return node.size

def part1(dir_sizes):
    total = 0

    for size in dir_sizes:
        if size <= 100000:
            total = total + size
        else:
            return total

def part2(dir_sizes):
    delete_needed = root.size - 40000000

    for size in dir_sizes:
        if size >= delete_needed:
            return size

def sol(filename):
    root = create_directory_tree(filename)
    dir_sizes = []
    set_dir_sizes(root, dir_sizes)
    dir_sizes.sort()
    
    print("sum of dirs at most 100k:", part1(dir_sizes))
    print("smallest directory of size >= needed space", part2(dir_sizes))


# sol("example")
sol("input")