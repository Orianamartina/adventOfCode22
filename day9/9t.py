with open("day9/9input.txt", "r") as file:
    file_contents = file.readlines()

def move(f):
    x = y = 0 
    for line in f:
        direction, distance = line.split()
        for _ in range(int(distance)):
            x += (direction == 'R') - (direction == 'L')
            y += (direction == 'U') - (direction == 'D')
            yield x, y

def follow(head):
    x = y = 0 
    i = 0
    for hx, hy in head:
        if abs(hx - x) > 1 or abs(hy - y) > 1:
            y += (hy > y) - (hy < y)
            x += (hx > x) - (hx < x)
        i += 1
        yield x, y

tenth = second = list(follow(move(file_contents)))
for _ in range(8):
    tenth = follow(tenth)
print(len(set(second)))
print(len(set(tenth)))

