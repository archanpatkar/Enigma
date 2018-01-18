class RotorFlow:
    def __init__(self,rotors=[],reflector=None):
        self.flow = rotors;
        self.reflector = reflector;
        counter = 0;
        while(counter < len(self.flow)):
            self.flow[counter].on("Sidereal", lambda *x: self.flow[counter + 1].step());
            counter += 1;

    def scramble(self,char):
        print("input -> ",char);
        self.flow[0].step();
        for rotor in self.flow:
            char = rotor.scramble(char);
        char = self.reflector.get(char);
        for rotor in self.flow.__reversed__():
            char = rotor.scramble(char);
        print("output  -> ",char);
        return char;
            
    def unscramble(self,char):
        self.flow[0].step();
        for rotor in self.flow:
            char = rotor.unscramble(char);
        char = self.reflector.get(char);
        for rotor in self.flow.__reversed__():
            char = rotor.unscramble(char);
        return char;