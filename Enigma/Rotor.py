from pyEmitter.emitter import EventEmitter
from Enigma.Rotor_Types import *

class Rotor(EventEmitter):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];

    def __init__(self , ring_setting=0 , type="IC" , wiring=None , turnover=25):
        EventEmitter.__init__(self);
        self.position = ring_setting;
        self.turnover = turnover;
        self.type = type;
        if(wiring is None):
            self.letters = list(rotors.get(type));
        else:
            self.type = "Custom";
            self.letters = wiring[:];
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
        if(self.position == self.turnover):
            self.emit("Sidereal");
        elif(self.position == 25):
            self.position = 0;