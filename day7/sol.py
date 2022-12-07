class Node:
    def __init__(self, name, parent, fs_type, size = None):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []
        self.type = fs_type

    def add_child(self, child):
        self.children.append(child)

def create_directory_tree(filename):
    f = open(filename, "r")

    root = Node("/", "dir", None)
    current = None

    for line in f.readlines():
        data = line.strip().split()
        if data[0] == "$":
            # command
            if data[1] == "cd":
                if data[2] == "..":
                    # change level up
                    current = current.parent
                elif data[2] == "/":
                    # change to /
                    current = root
                else:
                    # change to existing dir
                    for child in current.children:
                        if child.name == data[2]:
                            current = child
                            break

            elif data[1] == "ls":
                pass

            else:
                raise Exception(f"unknown command {data[1]}")

        else:
            # directory item
            # add node
            if data[0] == "dir":
                # directory
                current.add_child(Node(data[1], current, "dir"))
            else:
                # file
                current.add_child(Node(data[1], current, "file", int(data[0])))

    return root

def set_dir_sizes(node):
    if node.size is not None:
        return node.size

    # directory
    node.size = 0
    for child in node.children:
        node.size = node.size + set_dir_sizes(child)

    return node.size

def part1(node):
    if node.type == "file":
        return 0

    s = 0

    if node.size <= 100000:
        s = node.size

    for child in node.children:
        s = s + part1(child)

    return s

        
def get_dir_sizes(node, l):
    if node.type == "file":
        return

    l.append(node.size)
    for child in node.children:
        get_dir_sizes(child, l)
    

def part2(root):
    # part 2
    total_disk = 70000000
    space_needed = 30000000
    unused_disk = total_disk - root.size
    delete_needed = space_needed - unused_disk

    print("needed space:", delete_needed)

    # find smallest directory of that has size >= delete_needed
    dir_sizes = []
    get_dir_sizes(root, dir_sizes)
    dir_sizes.sort()

    for size in dir_sizes:
        if size >= delete_needed:
            return size

def sol(filename):
    root = create_directory_tree(filename)
    set_dir_sizes(root)
    
    print("sum of dirs at most 100k:", part1(root))
    print("smallest directory of size >= needed space", part2(root))


# sol("example")
sol("input")