# Enigma
### An Enigma Machine written in Python

## Example Usage

``` python 
from Enigma.Enigma import Enigma
from Enigma.Rotor import Rotor
from Enigma.Reflector import Reflector
from Enigma.Plugboard import Plugboard

e1 = Enigma(
            rotors = [
                        Rotor(  
                                ring_setting = 5,
                                type = "IC"
                             ),
                        Rotor(  
                                ring_setting = 7,
                                type = "IIC"
                             ),
                        Rotor(  
                                ring_setting = 10,
                                type = "IIIC"
                             )
                     ],
            reflector = Reflector("B"),
            plugboard = Plugboard([
                                        ("A","X"),
                                        ("H","Z"),
                                        ("B","R"),
                                        ("V","S"),
                                        ("Y","Q")
                                ])
        );

encrypted_string = e1.encrypt("Hello")
print(encrypted_string);

e2 = Enigma(
            rotors = [
                        Rotor(  
                                ring_setting = 5,
                                type = "IC"
                             ),
                        Rotor(  
                                ring_setting = 7,
                                type = "IIC"
                             ),
                        Rotor(  
                                ring_setting = 10,
                                type = "IIIC"
                             )
                     ],
            reflector = Reflector("B"),
            plugboard = Plugboard([
                                        ("A","X"),
                                        ("H","Z"),
                                        ("B","R"),
                                        ("V","S"),
                                        ("Y","Q")
                                ])
        );

print(e2.decrypt(encrypted_string));
```
