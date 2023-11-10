with open("day8/8input.txt", "r") as file:
    file_contents = file.read()

contents = file_contents.split('\n')
map_heigth = len(contents)
map_width = len(contents[0])

def set_up_matrix(content):
    matrix = []

    for i in range(map_heigth):
        matrix.append([])
    
    return matrix


def format_content(content):
    
    matrix = set_up_matrix(content)

    for i in range(map_width):
        for j,line in enumerate(content):
            matrix[j].append(int(line[i]))

    return matrix


def check_if_visible(y, x, matrix):
   
    return(
        check_if_visible_from_bottom(y,x,matrix)
        or
        check_if_visible_from_top(y,x,matrix)
        or
        check_if_visible_from_left(y,x,matrix)
        or
        check_if_visible_from_right(y,x,matrix)
    )



def check_if_visible_from_left(y, x, matrix):
    for i in range(x):
        if matrix[y][i] >= matrix[y][x]:
            return False
    return True

def check_if_visible_from_right(y, x, matrix):
    for i in range(x + 1, map_width):
        if matrix[y][i] >= matrix[y][x]:
            return False
    return True

def check_if_visible_from_top(y, x, matrix):
    for i in range(y):
        if matrix[i][x]  >= matrix[y][x]:
            return False
    return True
def check_if_visible_from_bottom(y, x, matrix):
    for i in range(y + 1, map_heigth):
        if matrix[i][x]  >= matrix[y][x]:
            return False
    return True


def get_visible_trees(matrix):

    visible_trees = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if check_if_visible(i,j,matrix):
                visible_trees += 1

    return (visible_trees)

matrix = format_content(contents)
print(get_visible_trees(format_content(contents)))
