from Rotor import Rotor
from Reflector import B

class Enigma:
    
    def __init__(self , rotor_config = { "I":(0,"1"), "II":(0,"1"), "III":(0,"1") } , plugboard = None , reflector = B): 
        self.I = Rotor(*rotor_config.get("I"));
        self.II = Rotor(*rotor_config.get("II"));
        self.III = Rotor(*rotor_config.get("III"));
        self.I.on("Sidereal", lambda *args: self.II.step())
        self.II.on("Sidereal", lambda *args: self.III.step())
        self.PlugBoard = plugboard;
        self.Reflector = reflector;
    

    def process(self,data):
        string = "";
        for char in data:
            scrambled = self.each(char);
            string += self.Reflector[scrambled];
        return string;

    def encrypt(self,data):
        return self.process(data);

    def decrypt(self,data):
        return self.process(data);

    def each(self,char):
        I = self.I;
        II = self.II;
        III = self.III;
        output = III.scramble(II.scramble(I.scramble("a")));
        I.step();
        return output;