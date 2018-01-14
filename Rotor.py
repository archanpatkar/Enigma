from pyEmitter.emitter import EventEmitter
from Rotor_Types import *

class Rotor(EventEmitter):
    letters = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z"
    ];

    def __init__(self,initial=0,rtype="I"):
        EventEmitter.__init__(self);
        self.rotor = initial;
        letters = rotors.get(rtype);
    
    def rotate(key):
        if key < 26 and key >= 0:
            self.rotor = key;

    def scramble(self,data):
        index = Rotor.letters.index(data);
        derived = ((index + self.rotor) % 26);
        output = self.letters[derived];
        return output;

    def step(self):
        if(self.rotor < 25):
            self.rotor += 1;
        else:
            self.rotor = 0;
            self.emit("Sidereal");
        