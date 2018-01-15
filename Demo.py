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

print(e1.I.scramble("A"))
print(e1.I.unscramble("D"))

print(e1.II.scramble("A"))
print(e1.II.unscramble("H"))

print(e1.III.scramble("A"))
print(e1.III.unscramble("U"))

print(e1.each("A"));

# print(e1.each("A"))
# print(e1.eachinv("Z"))
# print(e1.eachinv(""))



e2 = Enigma(
            rotors = [
                        (0,"IC"),
                        (13,"IIC"),
                        (5,"IIIC")
            ],
            reflector = "B"
        );

print(e2.eachinv("Z"))
# print(e2.decrypt(encrypted_string));
# print("out ->",e2.each("U"))