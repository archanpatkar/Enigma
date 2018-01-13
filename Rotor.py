from pyEmitter.emitter import EventEmitter
from Rotor_Types import *

class Rotor(EventEmitter):
    letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z"
    ];

    def __init__(self,initial=0,rtype="1"):
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
        