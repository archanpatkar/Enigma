from Rotor import Rotor
from Reflector import reflector as r

class Enigma:
    
    def __init__(self , rotors = [ (20,"I"), (13,"II"), (5,"III") ] , plugboard = None , reflector = "A"): 
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
            scrambled = self.each(char);
            reflected = self.reflect(scrambled);
            print("Converting {} -> {}".format(char,reflected));
            string += reflected;
        return string;

    def encrypt(self,data):
        return self.process(data.upper().replace(" ",""));

    def decrypt(self,data):
        return self.process(data.upper());

    def each(self,char):
        print("each")
        I = self.I;
        II = self.II;
        III = self.III;
        print("I -> {}".format(I.rotor));
        print("II -> {}".format(II.rotor));
        print("III -> {}".format(III.rotor));
        output = III.scramble(II.scramble(I.scramble(char)));
        I.step();
        return output;

    def reflect(self,char):
        print("reflect")
        I = self.I;
        II = self.II;
        III = self.III;
        print("I -> {}".format(I.rotor));
        print("II -> {}".format(II.rotor));
        print("III -> {}".format(III.rotor));
        return I.scramble(II.scramble(III.scramble(char)));