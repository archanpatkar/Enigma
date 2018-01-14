from Rotor import Rotor
from Reflector import B

class Enigma:
    
    def __init__(self , rotor_config = [ (20,"I"), (13,"II"), (5,"III") ] , plugboard = None , reflector = B): 
        self.I = Rotor(*rotor_config[0]);
        self.II = Rotor(*rotor_config[1]);
        self.III = Rotor(*rotor_config[2]);
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
        return self.process(data.upper());

    def decrypt(self,data):
        return self.process(data.upper());

    def each(self,char):
        I = self.I;
        II = self.II;
        III = self.III;
        output = III.scramble(II.scramble(I.scramble("a")));
        I.step();
        return output;