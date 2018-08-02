from Enigma.Rotor import Rotor
from Enigma.Reflector import Reflector
from Enigma.Plugboard import Plugboard
from Enigma.RotorFlow import RotorFlow

class Enigma:
    
    def __init__(self , rotors = [ Rotor(0,"IC") , Rotor(0,"IIC") , Rotor(0,"IIIC") ] , plugboard = Plugboard() , reflector = Reflector("A")): 
        self.rotors = rotors
        for i in range(len(rotors)):
            if i + 1 < len(rotors):
                rotors[i].on("Sidereal", lambda *args: rotors[i+1].step())
        self.Plugboard = plugboard;
        self.Reflector = reflector;

    def encrypt(self,data):
        data = data.upper().replace(" ","");
        string = "";
        for char in data:
            string += self.each(char,True);
        return string;

    def decrypt(self,data):
        data = data.upper();
        string = "";
        for char in data:
            string += self.each(char,False);
        return string;

    def each(self,char,flag):
        self.rotors[0].step()
        output = self.Plugboard.get(char)
        for rotor in self.rotors:
            if flag:
                output = rotor.scramble(output)
            else:
                output = rotor.unscramble(output)
        output = self.Reflector.get(output)
        for rotor in self.rotors[::-1]:
            if flag:
                output = rotor.scramble(output)    
            else:
                output = rotor.unscramble(output)  
        return self.Plugboard.get(output);