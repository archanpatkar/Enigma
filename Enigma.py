from Rotor import Rotor

class Enigma:
    
    def __init__(self , rotor_config = { "I":(0,"1"), "II":(0,"1"), "III":(0,"1") } , plugboard = None , reflector = None): 
        self.I = Rotor(*rotor_config.get("I"));
        self.II = Rotor(*rotor_config.get("II"));
        self.III = Rotor(*rotor_config.get("III"));
        self.I.on("Sidereal", lambda *args: self.II.step())
        self.II.on("Sidereal", lambda *args: self.III.step())
        self.PlugBoard = plugboard;
        self.Reflector = reflector;
    
    def encrypt(self):
        pass
    
    def decrypt(self):
        pass

    def each(self,char):
        I = self.I;
        II = self.II;
        III = self.III;
        output = III.scramble(II.scramble(I.scramble("a")));
        I.step();
        return output;

        


# count = 0;

# for i in range(26):
#     for j in range(26):
#         for k in range(26):
#             count += 1;
#             output = III.scramble(II.scramble(I.scramble("a")));
#             print(output);
#             I.step();
#         II.step();
#     III.step();