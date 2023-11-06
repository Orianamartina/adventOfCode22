with open("day1/1input.txt", "r") as file:
    file_contents = file.read()

number_groups = file_contents.split('\n\n')
number_group_lists = [list(map(int, group.split())) for group in number_groups]


maxCalories = 0
for group in number_group_lists:
    calories = sum(group)
    if calories > maxCalories:
        maxCalories = calories
    

print(f'Answer to puzzle 1.1: {maxCalories}')

top_calories = [0, 0, 0]


for group in number_group_lists:
    calories = sum(group)
    for i in range(3):
        if calories > top_calories[i]:
            top_calories.insert(i, calories)
            top_calories  = top_calories[:3]
            break

print (f'answer to puzzle 1.2: {sum(top_calories)}')


