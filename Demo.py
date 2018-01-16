from Enigma import Enigma
from Rotor import Rotor
from Reflector import Reflector

e1 = Enigma(
            rotors = [
                        Rotor(0,"IC"),
                        Rotor(0,"IIC"),
                        Rotor(0,"IIIC"),
                     ],
            reflector = Reflector("B")
        );

encrypted_string = e1.encrypt("Hello")
print(encrypted_string);

e2 = Enigma(
            rotors = [
                        (0,"IC"),
                        (0,"IIC"),
                        (0,"IIIC"),
                     ],
            reflector = Reflector("B")
        );

print(e2.decrypt(encrypted_string));