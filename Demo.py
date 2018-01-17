from Enigma.Enigma import Enigma
from Enigma.Rotor import Rotor
from Enigma.Reflector import Reflector

e1 = Enigma(
            rotors = [
                        Rotor(  
                                ring_setting = 0,
                                type = "IC"
                             ),
                        Rotor(  
                                ring_setting = 0,
                                type = "IIC"
                             ),
                        Rotor(  
                                ring_setting = 0,
                                type = "IIIC"
                             )
                     ],
            reflector = Reflector("B"),
            plugboard = [
                                ("A","X"),
                                ("B","R"),
                                ("V","S"),
                                ("Y","Q")
                        ]
        );

encrypted_string = e1.encrypt("Hello")
print(encrypted_string);

e2 = Enigma(
            rotors = [
                        Rotor(  
                                ring_setting = 0,
                                type = "IC"
                             ),
                        Rotor(  
                                ring_setting = 0,
                                type = "IIC"
                             ),
                        Rotor(  
                                ring_setting = 0,
                                type = "IIIC"
                             )
                     ],
            reflector = Reflector("B"),
            plugboard = [
                                ("A","X"),
                                ("B","R"),
                                ("V","S"),
                                ("Y","Q")
                        ]
        );

print(e2.decrypt(encrypted_string));