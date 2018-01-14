from Enigma import Enigma


e1 = Enigma(
            [
                (20,"I"),
                (13,"II"),
                (5,"III")
            ]
        );
        
print(e1.encrypt("Hello World!"));