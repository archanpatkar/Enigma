class Flow:
    def __init__(self,rotors=[],reflector=None):
        self.flow = rotors;
        self.reflector = reflector;
        for rotor in range(len(self.flow)) :
            self.flow[rotor].on("Sidereal", lambda *x: self.flow[rotor + 1].step());

    def scramble(self,char):
        for rotor in self.flow:
            char = rotor.scramble(char);
        char = self.reflector.get(char);
        for rotor in self.flow.__reversed__():
            char = rotor.scramble(char);
        return char;
            
    def unscramble(self,char):
        for rotor in self.flow:
            char = rotor.unscramble(char);
        char = self.reflector.get(char);
        for rotor in self.flow.__reversed__():
            char = rotor.unscramble(char);
        return char;