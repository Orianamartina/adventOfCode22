with open("day14/14input.txt", "r") as file:
    file_contents = file.read()


contents = file_contents.split('\n')


min_item = 500
max_item = 0
min_height = 100
max_height = 0
x = 0

formatted_contents = []

for line in contents:
    content_line = []
    for inst in line.split(" -> "):
        inst = inst.split(",")
        if int(inst[0]) < min_item:
            min_item = int(inst[0])
        if int(inst[0]) > max_item:
            max_item = int(inst[0])
        if int(inst[1]) < min_height:
            min_height = int(inst[1])
        if int(inst[1]) > max_height:
            max_height = int(inst[1])
        inst = [int(inst[0]), int(inst[1])]
        content_line.append(inst)
    formatted_contents.append(content_line)


def get_map():

    map = [[" " for _ in range(0, max_item + 3 - min_item)]
           for _ in range(max_height + 3)]
    map.append(["#" for _ in range(0, max_item + 3 - min_item)])

    for line in formatted_contents:
        for i, inst in enumerate(line[:-1]):
            if inst[0] == line[i+1][0]:
                s = min(inst[1], line[i+1][1])
                b = max(inst[1], line[i+1][1])
                for j in range(b-s+1):
                    map[j + s + 1][inst[0] - min_item + 1] = "#"
            if inst[1] == line[i+1][1]:
                s = min(inst[0], line[i+1][0])
                b = max(inst[0], line[i+1][0])
                for j in range(b-s+1):
                    map[inst[1]+1][j + (s-min_item)+1] = "#"
    return map


def throw_sand(map):
    y = 0
    x = 501 - min_item
    in_rest = False
    while not in_rest:
        if y == len(map)-2:
            return True
        # Check underneath
        elif map[y+1][x] == " ":
            y += 1
        else:
            # Check left
            if map[y+1][x-1] == " ":
                y += 1
                x -= 1
            # Check right
            elif map[y+1][x+1] == " ":
                y += 1
                x += 1
            # Set to rest
            else:
                map[y][x] = "º"
                in_rest = True
    return False


map = get_map()
is_finished = False
counter = 0
while not is_finished:
    is_finished = throw_sand(map)
    counter += 1

print("14.1", counter - 1)
lines = []
for item in map[:-1]:
    line = ""
    for i in item:
        line += i
    lines.append(line)

for i in lines:
    print(i)


def throw_sand_with_infinite_floor(map, fp):
    y = 0
    x = fp - min_item
    in_rest = False
    while not in_rest:
        # Check underneath
        if map[y+1][x] == " ":
            y += 1
        else:
            if x == len(map[0]) - 1:
                for i, line in enumerate(map):
                    if i == len(map)-1:
                        line.append("#")
                    else:
                        line.append(" ")
            if x == 0:
                for i, line in enumerate(map):
                    if i == len(map)-1:
                        line.insert(0, "#")
                    else:
                        line.insert(0, " ")
                fp += 1
                x = 1
            # Check left
            if map[y+1][x-1] == " ":
                y += 1
                x -= 1
            # Check right
            elif map[y+1][x+1] == " ":
                y += 1
                x += 1
            # Set to rest
            else:
                map[y][x] = "º"
                in_rest = True

    return fp


counter = 0


map = get_map()
fp = 501
while map[1][fp - min_item] != "º":
    counter += 1
    fp = throw_sand_with_infinite_floor(map, fp)
lines = []
for item in map[:-1]:
    line = ""
    for i in item:
        line += i
    lines.append(line)

for i in lines:
    print(i[60:-60])
print(counter)
