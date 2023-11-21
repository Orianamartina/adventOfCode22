with open("day6/6input.txt", "r") as file:
    file_contents = file.read()

possible_characters = "abcdefghijklmnopqrstuvwxyz"


def find_packet_in_signal(length_of_packet, data_stream):
    if len(data_stream) >= length_of_packet:
        for i in range(length_of_packet, len(data_stream) + 1):
            comparable_characters = data_stream[(i - length_of_packet): i]

            if len(set(comparable_characters)) == length_of_packet:
                return data_stream


def process_signal(signal, length_of_packet):
    data_stream = ""

    for character in signal:
        data_stream += character
        found_marker = find_packet_in_signal(length_of_packet, data_stream)
        if found_marker:
            return len(found_marker)


part1 = process_signal(file_contents, 4)
part2 = process_signal(file_contents, 14)

print(f"Answer to puzzle 6.1: {part1}")
print(f"Answer to puzzle 6.2: {part2}")
