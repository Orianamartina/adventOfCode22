
with open("day3/3input.txt", "r") as file:
    file_contents = file.read()

contents = file_contents.split('\n')

item_types = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total_priority = 0
for content in contents:
    length = len(content)
    firstHalf = content[:length//2]
    secondHalf = content[length//2:]
    foundItem = list(set(firstHalf).intersection(secondHalf))
    total_priority += (item_types.index(foundItem[0]))

print(f'puzzle 3.1 answer: {total_priority}')


# part 2: divide into groups of three
total_badge_priority = 0

for i in range(0, len(contents), 3):
    group = contents[i:i + 3]
    repeating_char = list(set(group[0]).intersection(*group[1:]))
    total_badge_priority += item_types.index(repeating_char[0])


print(f'puzzle 3.2 answer: {total_badge_priority}')
