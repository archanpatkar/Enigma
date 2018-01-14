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


# e2 = Enigma(
#             rotors = [
#                         (20,"IC"),
#                         (13,"IIC"),
#                         (5,"IIIC")
#             ],
#             reflector = "B"
#         );

# print(e2.decrypt(encrypted_string));

print("Position ->", e1.I.rotor)
out = e1.I.scramble("A");
print(e1.I.letters);
e1.I.step()
print(e1.I.letters);
inv = e1.I.unscramble(out);
print("Output -> ",out);
print("Input -> ",inv);