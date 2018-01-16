from Enigma import Enigma

e1 = Enigma(
            rotors = [
                        (0,"IC"),
                        (0,"IIC"),
                        (0,"IIIC"),
                     ],
            reflector = "B"
        );

encrypted_string = e1.encrypt("Hello")
print(encrypted_string);


e2 = Enigma(
            rotors = [
                        (0,"IC"),
                        (0,"IIC"),
                        (0,"IIIC"),
                     ],
            reflector = "B"
        );

print(e2.decrypt(encrypted_string));