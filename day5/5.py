with open("day5/5input.txt", "r") as file:
    file_contents = file.readlines()


boxes = []


#Boxes setup
for i in range (0, 8):
    boxes.append(file_contents[i])

def format_boxes():
    piles_of_boxes = []
    n = 1
    for i in range(9):
        new_line = []
        for line in boxes:
            if(line[n]) != " ":
                new_line.append(line[n])
        n += 4
        piles_of_boxes.append(new_line)
    return piles_of_boxes




#Instructions setup
instructions = []
for i in range (10, len(file_contents)):
    inst = file_contents[i].split(" ")
    guide = dict()
    guide[inst[0]] = int(inst[1])
    guide[inst[2]] = int(inst[3])
    guide[inst[4]] = int(inst[5][0])
    instructions.append(guide)


piles_of_boxes = format_boxes()
piles_of_boxes_p2 = format_boxes()
for instruction in instructions:
    #setup
    quantity_to_move = instruction["move"]
    origin = instruction["from"] - 1
    destiny = instruction["to"] - 1

    #p1

    for i in range (quantity_to_move):
        moving_box = piles_of_boxes[origin].pop(0)
        piles_of_boxes[destiny].insert(0, moving_box)
    
    #p2

    moving_boxes = piles_of_boxes_p2[origin][0:quantity_to_move]
    piles_of_boxes_p2[origin] = piles_of_boxes_p2[origin][quantity_to_move:]
    piles_of_boxes_p2[destiny] = moving_boxes  + piles_of_boxes_p2[destiny] 
    
answer = ""

for line in piles_of_boxes:
    answer += line[0]

print(f'Answer to puzzle 5.1: {answer}')

#part 2

answer = ""

for line in piles_of_boxes_p2:
    answer += line[0]

print(f'Answer to puzzle 5.2: {answer}')
