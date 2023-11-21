with open("day7/7input.txt", "r") as file:
    file_contents = file.read()


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.size = 0


def get_file_system(input_text):
    lines = input_text.split("\n")
    root = TreeNode("/")
    current_node = root
    stack = [root]
    total_size = 0
    for line in lines:
        line_content = line.split(" ")
        indicator = line_content[0]
        if line == "$ cd ..":
            stack.pop()
            current_node = stack[-1]
        elif line.startswith("$ cd"):
            directory_name = line_content[2]
            new_node = TreeNode(directory_name)
            current_node.children.append(new_node)
            stack.append(new_node)
            current_node = new_node
        elif indicator == "dir":
            continue
        elif indicator.isdigit():
            size = int(indicator)
            for node in stack:
                node.size += size
    return root


def print_tree(node, indent=" "):
    print(indent + node.name)
    for child in node.children:
        print_tree(child, indent + "  ")


def calculate_size(node):
    total_size = 0

    if node.size <= 100000:
        total_size += node.size
    for child in node.children:
        total_size += calculate_size(child)
    if len(node.children) == 0 and node.size <= 100000:
        return node.size
    else:
        return total_size


def free_up_space(node, size):
    smallest_size = size
    if node.size < smallest_size and node.size >= space_to_free:
        smallest_size = node.size
    for child in node.children:
        smallest_size = free_up_space(child, smallest_size)
    if len(node.children) == 0 and (node.size < smallest_size and node.size >= space_to_free):
        return node.size
    return smallest_size


input_text = file_contents[1:]

root_node = get_file_system(input_text)
print_tree(root_node)
total_size = calculate_size(root_node)

space_to_free = (30000000 - (70000000 - root_node.size))

print(f"{total_size} bytes")
print(free_up_space(root_node, root_node.size))
