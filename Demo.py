from Enigma import Enigma

e1 = Enigma(
            rotors = [
                        (21,"IC"),
                        (9,"IIC"),
                        (13,"IIIC")
            ],
            reflector = "B"
        );

encrypted_string = e1.encrypt("HELLO")
print(encrypted_string);


e2 = Enigma(
            rotors = [
                        (21,"IC"),
                        (9,"IIC"),
                        (13,"IIIC")
            ],
            reflector = "B"
        );

print(e2.decrypt(encrypted_string));