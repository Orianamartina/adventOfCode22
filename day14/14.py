with open("day14/14input.txt", "r") as file:
    file_contents = file.read()


contents = file_contents.split('\n')

path_line = []

min_item = 500
max_item = 0
min_height = 100
max_height = 0

map = [[[] for _ in range(0, 525 - 582)]
       for _ in range(165 - 15)]


# map = {i: set() for i in range(482, 526)}


for line in contents:
    items = line.split(" -> ")
    for i, item in enumerate(items):
        item = item.split(",")
        items[i] = item

    for i, item in enumerate(items[1:], start=1):
        if int(items[i][0]) == int(items[i-1][0]):
            for j in range(int(items[i-1][1]), int(items[i][1])):
                print(int(items[i][0]))
                map[int(items[i][0]) - 482].append(j)
        else:
            for j in range(int(items[i-1][0]), int(items[i][0])+1):
                map[j-482].append(int(items[i][1]))

    for directions in items:

        if int(directions[0]) < min_item:
            min_item = int(directions[0])
        elif int(directions[0]) > max_item:
            max_item = int(directions[0])
        if int(directions[1]) < min_height:
            min_height = int(directions[1])
        elif int(directions[1]) > max_height:
            max_height = int(directions[1])

print(len(map))

# for line in contents:
#     items = line.split(" -> ")
#     for i, item in enumerate(items):
#         item = item.split(",")
#         items[i] = item

#     for i, item in enumerate(items[1:], start=1):
#         if int(items[i][0]) == int(items[i-1][0]):
#             for j in range(int(items[i-1][1]), int(items[i][1])):
#                 map[int(items[i][0])].add(j)
#         else:
#             for j in range(int(items[i-1][0]), int(items[i][0])+1):
#                 map[j].add(int(items[i][1]))

#     for directions in items:

#         if int(directions[0]) < min_item:
#             min_item = int(directions[0])
#         elif int(directions[0]) > max_item:
#             max_item = int(directions[0])
#         if int(directions[1]) < min_height:
#             min_height = int(directions[1])
#         elif int(directions[1]) > max_height:
#             max_height = int(directions[1])


print(map)
print(len(map))


def create_map():
    for line in path_line:
        print(line)


# create_map()
