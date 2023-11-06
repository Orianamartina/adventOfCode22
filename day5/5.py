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


piles_of_boxes = format_boxes()

#Instruction setup
instructions = []
for i in range (10, len(file_contents)):
    inst = file_contents[i].split(" ")
    guide = dict()
    guide[inst[0]] = inst[1]
    guide[inst[2]] = inst[3]
    guide[inst[4]] = inst[5][0]
    instructions.append(guide)


#Box management p1
for instruction in instructions:
    #setup
    quantity_to_move = int(instruction["move"])
    origin = int(instruction["from"]) - 1
    destiny = int(instruction["to"]) - 1


    for i in range (quantity_to_move):
        moving_box = piles_of_boxes[origin].pop(0)
        piles_of_boxes[destiny].insert(0, moving_box)



#answer
answer = ""

for line in piles_of_boxes:
    answer += line[0]

print(f' answer to puzzle 5.1: {answer}')




#part 2

piles_of_boxes = format_boxes()

for instruction in instructions:
    #setup
    quantity_to_move = int(instruction["move"])
    origin = int(instruction["from"]) - 1
    destiny = int(instruction["to"]) - 1


    moving_boxes = piles_of_boxes[origin][0:quantity_to_move]
    piles_of_boxes[origin] = piles_of_boxes[origin][quantity_to_move:]
    piles_of_boxes[destiny] = moving_boxes  + piles_of_boxes[destiny] 




#answer
answer2 = ""

for line in piles_of_boxes:
    answer2 += line[0]

print(f' answer to puzzle 5.2: {answer2}')
