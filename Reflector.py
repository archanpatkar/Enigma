# class Reflector():
#     def __init__(self):
#         pass;

import json

rf_types =  json.load(open("./reflectors.json",mode="r"))

def reflector(type):
    return rf_types.get(type);