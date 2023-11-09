with open("day7/7input.txt", "r") as file:
    file_contents = file.readlines()

print(file_contents)

total_size_of_directories_above_100000 = 0

for line in file_contents:
    line_contents = line.split(" ")
    print(line_contents)
    if line_contents[0] != "$" and line_contents[0] != "dir":
       if int(line_contents[0]) < 100000:
            total_size_of_directories_above_100000 += int(line_contents[0])


print(total_size_of_directories_above_100000)
       