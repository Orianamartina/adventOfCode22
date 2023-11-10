with open("day8/8input.txt", "r") as file:
    file_contents = file.read()

contents = file_contents.split('\n')

def set_up_matrix(content):
    matrix = []

    for i in range(len(content)):
        matrix.append([])
    
    return matrix


def format_content(content):
    
    matrix = set_up_matrix(content)

    for i in range (len(content[0])):
    
        for j,line in enumerate(content):
            matrix[i].append(line[j])

    return matrix


print(format_content(contents))