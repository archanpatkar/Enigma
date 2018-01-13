from Enigma import Enigma


e1 = Enigma(
            {
                "I":(4,"1"),
                "II":(10,"1"),
                "III":(0,"1")
            }
        );


print(e1.encrypt("Hello World!"));