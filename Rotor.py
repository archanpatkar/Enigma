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

    def __init__(self,ring_setting=0,rtype="I",turnover=25):
        EventEmitter.__init__(self);
        self.position = initial;
        self.letters = list(rotors.get(rtype));
        if(ring_setting > 0):
            for times in range(ring_setting):
                self.letters.append(self.letters.pop(0));

    def ring_setting(ring_setting):
        if(ring_setting > 0):
            for times in range(ring_setting):
                self.letters.append(self.letters.pop(0));

    def scramble(self,data):
        index = Rotor.letters.index(data);
        output = self.letters[index];
        return output;
    
    def unscramble(self,data):
        index = self.letters.index(data);
        output = Rotor.letters[index];
        return output;

    def step(self):
        if(self.position < 25):
            self.position += 1;
            self.letters.append(self.letters.pop(0));
        else:
            self.position = 0;
            self.emit("Sidereal");
        