from Enigma.Rotor import Rotor
from Enigma.Reflector import Reflector
from Enigma.Plugboard import Plugboard
from Enigma.RotorFlow import RotorFlow

class Enigma:
    
    def __init__(self , rotors = [ Rotor(0,"IC") , Rotor(0,"IIC") , Rotor(0,"IIIC") ] , plugboard = Plugboard() , reflector = Reflector("A")): 
        # self.I = rotors[0];
        # self.II = rotors[1];
        # self.III = rotors[2];
        # self.I.on("Sidereal", lambda *args: self.II.step())
        # self.II.on("Sidereal", lambda *args: self.III.step())
        self.Flow = RotorFlow(rotors,reflector)
        self.Plugboard = plugboard;
        # self.Reflector = reflector;

    def encrypt(self,data):
        data = data.upper().replace(" ","");
        string = "";
        for char in data:
            # string += self.each(char);
            string += self.Plugboard.get(self.Flow.scramble(self.Plugboard.get(char)));
        return string;

    def decrypt(self,data):
        data = data.upper();
        string = "";
        for char in data:
            string += self.Plugboard.get(self.Flow.scramble(self.Plugboard.get(char)));
            # string += self.eachinv(char);
        return string;

    # def each(self,char):
    #     I = self.I;
    #     II = self.II;
    #     III = self.III;
    #     I.step();        
    #     output = III.scramble(II.scramble(I.scramble(self.Plugboard.get(char))));
    #     output = I.scramble(II.scramble(III.scramble(self.Reflector.get(output))));
    #     return self.Plugboard.get(output);

    # def eachinv(self,char):
    #     I = self.I;
    #     II = self.II;
    #     III = self.III;
    #     I.step();
    #     output = III.unscramble(II.unscramble(I.unscramble(self.Plugboard.get(char))));
    #     output = I.unscramble(II.unscramble(III.unscramble(self.Reflector.get(output))));
    #     return self.Plugboard.get(output);