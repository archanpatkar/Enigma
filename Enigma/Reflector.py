import json

rf_types =  json.load(open("./Enigma/reflectors.json",mode="r"))

def reflector(type):
    return rf_types.get(type);

class Reflector:
    def __init__(self,type="A"):
        self.reflector = reflector(type);
    
    def get(self,char):
        return self.reflector.get(char);