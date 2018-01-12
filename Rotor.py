
class Rotor:
    letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z"
    ];

    def __init__(self,initial=0):
        self.rotor = initial;
        self.letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z"
        ];


    def scramble(self,data):
        index = Rotor.letters.index(data);
        derived = ((index + self.rotor) % 26);
        output = Rotor.letters[derived];
        self.step();
        return output;

    def step(self):
        if(self.rotor < 25):
            self.rotor += 1;
        