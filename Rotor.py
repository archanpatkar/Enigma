
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

    def get(self,data):
        final = [];
        char = data.lower()
        for():
        index = Rotor.letters.index(char)
        derived = (index + self.rotor) % 26
        self.step();
        final.append(Rotor.letters[derived]);


    def step(self):
        self.rotor += 1;
        