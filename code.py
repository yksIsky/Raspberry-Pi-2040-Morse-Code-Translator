#Python 3.1
from machine import Pin
from time import sleep


class Pic_morse():
    def __init__(self):
        self.MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                               'C': '-.-.', 'D': '-..', 'E': '.',
                               'F': '..-.', 'G': '--.', 'H': '....',
                               'I': '..', 'J': '.---', 'K': '-.-',
                               'L': '.-..', 'M': '--', 'N': '-.',
                               'O': '---', 'P': '.--.', 'Q': '--.-',
                               'R': '.-.', 'S': '...', 'T': '-',
                               'U': '..-', 'V': '...-', 'W': '.--',
                               'X': '-..-', 'Y': '-.--', 'Z': '--..',
                               '1': '.----', '2': '..---', '3': '...--',
                               '4': '....-', '5': '.....', '6': '-....',
                               '7': '--...', '8': '---..', '9': '----.',
                               '0': '-----', ', ': '--..--', '.': '.-.-.-',
                               '?': '..--..', '/': '-..-.', '-': '-....-',
                               '(': '-.--.', ')': '-.--.-'}
     
    def pin_nr(self):
        
        pin_nr = int(input("Pin number from 1-25 default 25: "))
        self.builtin_led = Pin(pin_nr, Pin.OUT)
    
    def morse_name(self):
        name = input("Provide your name: ")
        name = name.replace(" ","")
        morse_name = []
        for i in name:
            morse_name.append(self.MORSE_CODE_DICT.get(i.upper()))
        return "".join([i for i in morse_name])

    def long(self):
        self.builtin_led.value(1)
        sleep(1)
        self.builtin_led.value(0)
        sleep(1)

    def short(self):
        self.builtin_led.value(1)
        sleep(0.2)
        self.builtin_led.value(0)
        sleep(0.2)

    def morse_code(self, ):
        self.pin_nr()
        m_name = self.morse_name()
        for i in m_name:
            if i == "-":
                self.long()
            elif i == ".":
                self.short()
                
           
if __name__ == "__maine__":
  new_name = Pic_morse()
  new_name.morse_code()




