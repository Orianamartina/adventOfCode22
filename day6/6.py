with open("day6/6input.txt", "r") as file:
    file_contents = file.read()

class Device():

    def __init__(self):
        self._data_stream = ""
        self._possible_characters = "abcdefghijklmnopqrstuvwxyz"

    def receive_data(self, character):
        self._data_stream += character
    
    def start_of_packet_marker(self):

        if len(self._data_stream) >= 4:

            for i in range(4, len(self._data_stream) + 1):

                comparable_characters = self._data_stream[(i-4): i]

                if (len(set(comparable_characters)) == 4):
                    return (self._data_stream)
            
    def start_of_message_marker(self):
        
        if len(self._data_stream) >= 14:

            for i in range(14, len(self._data_stream) + 1):

                comparable_characters = self._data_stream[(i-14): i]

                if (len(set(comparable_characters)) == 14):
                    return (self._data_stream)


    def lock_onto_signal(self, signal):

        start_of_packet_marker = 0
        start_of_message_marker = 0
        
        for character in signal:
            self.receive_data(character)
            
            if self.start_of_packet_marker():
                start_of_packet_marker = len(self.start_of_packet_marker())-1
                
            if self.start_of_message_marker():
                start_of_message_marker=  len(self.start_of_message_marker())

            if start_of_message_marker and start_of_packet_marker:
                print(start_of_packet_marker)
                print(start_of_message_marker)
                break



broken_device = Device()
broken_device.lock_onto_signal(file_contents)
""""

    qfmfhmhjmjggwbbvdvwvlvrrtsrsccwsslvlffjrrtprpr

"""
