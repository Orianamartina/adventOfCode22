with open("day7/7input.txt", "r") as file:
    file_contents = file.read()


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.size = 0

def parse_input(input_text):
    lines = input_text.split('\n')
    root = TreeNode('/')
    current_node = root
    stack = [root]

    for line in lines:
        if line.startswith('$ cd '):
            directory_name = line[5:]
            new_node = TreeNode(directory_name)
            current_node.children[directory_name] = new_node
            stack.append(new_node)
            current_node = new_node
        elif line.startswith('dir '):
            directory_name = line[4:]
            new_node = TreeNode(directory_name)
            current_node.children[directory_name] = new_node
        elif line and line[0].isdigit():
            size, name = line.split(' ', 1)
            size = int(size)
            current_node.size += size
        elif line == '$ cd ..':
            stack.pop()
            current_node = stack[-1]

    return root


def calculate_total_size(node):
    total_size = 0
    if node.size <= 100000:
        total_size += node.size

    return total_size

input_text = file_contents

root_node = parse_input(input_text)
total_size = calculate_total_size(root_node)
print(f"Total size of root: {total_size} bytes")
