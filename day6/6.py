with open("day6/6input.txt", "r") as file:
    file_contents = file.readlines()[:7]



class Device():

    def __init__(self):
        self._data_stream = ""
        self._possible_characters = "abcdefghijklmnopqrstuvwxyz"
    
    def start_of_packet_marker(self, character):
        
        self._data_stream += character

        if len(self._data_stream) >= 4:

            for i in range(4, len(self._data_stream)):

                comparable_characters = self._data_stream[(i-4): i]
                



    def lock_onto_signal(self, signal):
        
        for character in signal:
            if self.start_of_packet_marker(character):
                return "chi"





broken_device = Device()
broken_device.lock_onto_signal(file_contents)
""""

    qfmfhmhjmjggwbbvdvwvlvrrtsrsccwsslvlffjrrtprpr

"""
