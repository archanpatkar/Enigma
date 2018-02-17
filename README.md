# Enigma
### An [Enigma Machine](https://en.wikipedia.org/wiki/Enigma_machine) Simulator from WWII written in Python
#### A Complete Modular Design with configurable Rotors and Reflectors through a JSON file 

## Details
> Rotors and Reflectors can be added modifying rotors.json and reflector.json files

### Rotors Supported

| Rotor # 	| ABCDEFGHIJKLMNOPQRSTUVWXYZ 	| Model Name & Number     	|
|:-------:	|----------------------------	|-------------------------	|
| IC      	| DMTWSILRUYQNKFEJCAZBPGXOHV 	| Commercial Enigma A, B  	|
| IIC     	| HQZGPJTMOBLNCIFDYAWVEUSRKX 	| Commercial Enigma A, B  	|
| IIIC    	| UQNTLSZFMREHDPXKIBVYGJCWOA 	| Commercial Enigma A, B  	|
| IR       	| JGDQOXUSCAMIFRVTPNEWKBLZYH 	| German Railway (Rocket) 	|
| IIR      	| NTZPSFBOKMWRCJDIVLAEYUXHGQ 	| German Railway (Rocket) 	|
| IIIR     	| JVIUBHTCDYAKEQZPOSGXNRMWFL 	| German Railway (Rocket) 	|
| UKW     	| QYHOGNECVPUZTFDJAXWMKISRBL 	| German Railway (Rocket) 	|
| ETWR     	| QWERTZUIOASDFGHJKPYXCVBNML 	| German Railway (Rocket) 	|

### Reflectors Supported

| Rotor #     	| ABCDEFGHIJKLMNOPQRSTUVWXYZ 	|
|-------------	|----------------------------	|
| Reflector A 	| EJMZALYXVBWFCRQUONTSPIKHGD 	|
| Reflector B 	| YRUHQSLDPXNGOKMIEBFZCWVJAT 	|
| Reflector C 	| FVPJIAOYEDRZXWGCTKUQSBNMHL 	|
| ETW         	| ABCDEFGHIJKLMNOPQRSTUVWXYZ 	|

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
