from Rotor import Rotor
from Reflector import reflector as r

class Enigma:
    
    def __init__(self , rotors = [ (20,"IC"), (13,"IIC"), (5,"IIIC") ] , plugboard = None , reflector = "A"): 
        self.I = Rotor(*rotors[0]);
        self.II = Rotor(*rotors[1]);
        self.III = Rotor(*rotors[2]);
        self.I.on("Sidereal", lambda *args: self.II.step())
        self.II.on("Sidereal", lambda *args: self.III.step())
        self.PlugBoard = plugboard;
        self.Reflector = r(reflector);
     
    def process(self,data):
        string = "";
        for char in data:
            string += self.each(char);
        return string;

    def processinv(self,data):
        string = "";
        for char in data:
            string += self.eachinv(char);
        return string;

    def encrypt(self,data):
        return self.process(data.upper().replace(" ",""));

    def decrypt(self,data):
        return self.processinv(data.upper());

    def each(self,char):
        I = self.I;
        II = self.II;
        III = self.III;
        I.step();        
        output = III.scramble(II.scramble(I.scramble(char)));
        output = I.scramble(II.scramble(III.scramble(self.Reflector.get(output))));
        return output;

    def eachinv(self,char):
        I = self.I;
        II = self.II;
        III = self.III;
        I.step();
        output = III.unscramble(II.unscramble(I.unscramble(char)));
        output = I.unscramble(II.unscramble(III.unscramble(self.Reflector.get(output))));
        return output;