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
            string +=  self.each(char);
        print("Converted {} -> {}".format(data,string));
        return string;

    def encrypt(self,data):
        return self.process(data.upper().replace(" ",""));

    def decrypt(self,data):
        return self.process(data.upper());

    def each(self,char):
        I = self.I;
        II = self.II;
        III = self.III;
        output = III.scramble(II.scramble(I.scramble(char)));
        I.step();
        return output;

    # def reflect(self,char):
    #     I = self.I;
    #     II = self.II;
    #     III = self.III;
    #     return I.scramble(II.scramble(III.scramble(char)));