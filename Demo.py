from Enigma import Enigma

e1 = Enigma(
            rotors = [
                        (5,"IC"),
                        (7,"IIC"),
                        (10,"IIIC"),
                     ],
            reflector = "B"
        );

encrypted_string = e1.encrypt("Hello")
print(encrypted_string);


e2 = Enigma(
            rotors = [
                        (5,"IC"),
                        (7,"IIC"),
                        (10,"IIIC"),
                     ],
            reflector = "B"
        );

print(e2.decrypt(encrypted_string));