with open("4input.txt", "r") as file:
    file_contents = file.read()

pairs = file_contents.split('\n')


contained_pairs = 0
for assignment in pairs:
    splitted_assignments = assignment.split(",")
    
    first_ranges = splitted_assignments[0].split("-")
    second_ranges = splitted_assignments[1].split("-")

    if (int(first_ranges[0])<=int(second_ranges[0]) and int(first_ranges[1])>=int(second_ranges[1])):
        contained_pairs += 1
    elif (int(first_ranges[0])>=int(second_ranges[0]) and int(first_ranges[1])<=int(second_ranges[1])):
        contained_pairs += 1

print (contained_pairs)

contained_pairs = 0
"""for assignment in pairs:
    splitted_assignments = assignment.split(",")
    first_ranges = splitted_assignments[0].split("-")
    second_ranges = splitted_assignments[1].split("-")

    if (int(first_ranges[0])>= int(second_ranges[1])):
        contained_pairs += 1
    elif (int(second_ranges[0])>= int(first_ranges[1])):
        contained_pairs += 1

print(contained_pairs)"""
