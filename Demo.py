from Enigma import Enigma

e1 = Enigma(
            rotors = [
                        (0,"IC"),
                        (13,"IIC"),
                        (5,"IIIC")
            ],
            reflector = "B"
        );

# encrypted_string = e1.encrypt("Hello")
# print(encrypted_string);

print("out ->",e1.each("H"))



e2 = Enigma(
            rotors = [
                        (0,"IC"),
                        (13,"IIC"),
                        (5,"IIIC")
            ],
            reflector = "B"
        );

# print(e2.decrypt(encrypted_string));

print("out ->",e2.each("U"))