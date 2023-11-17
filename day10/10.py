with open("day10/10input.txt", "r") as file:
    file_contents = file.readlines()


def get_sum_of_signal_strengths():
    signal_strengths = 0
    cicle = 0
    x = 1
    execution_ammount = 0
    searched_cicles = [20, 60, 100, 140, 180, 220]

    for line in file_contents:
        x += execution_ammount
        execution_ammount = 0

        if line[0] == "n":
            cicle += 1
            if cicle in searched_cicles:
                signal_strengths += cicle * x
        else:
            for i in range(2):
                cicle += 1
                if cicle in searched_cicles:
                    signal_strengths += cicle * x

                ammount = int(line.split()[1])
                execution_ammount = ammount

    print(signal_strengths)


def draw_crt():
    crt = [(["." for i in range(40)]) for _ in range(6)]

    tick = 0
    sprite_position = 1

    def tick_is_under_sprite(tick, sprite_position, row):
        row = 40 * row
        return tick in [(sprite_position - 1 + row), (sprite_position + row), (sprite_position + 1 + row)]

    for line in file_contents:
        if line[0] == "n":
            row = tick // 40
            column = tick % 40
            if tick_is_under_sprite(tick, sprite_position, row):
                crt[row][column] = "#"
            tick += 1
        else:
            for i in range(2):

                row = tick // 40
                column = tick % 40
                if tick_is_under_sprite(tick, sprite_position, row):
                    crt[row][column] = "#"
                tick += 1

            ammount = int(line.split()[1])
            sprite_position += ammount

    for i in range(6):
        print(crt[i]
              )


get_sum_of_signal_strengths()

draw_crt()
