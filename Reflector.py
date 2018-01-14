# class Reflector():
#     def __init__(self):
#         pass;

rf_types = {
    "A" : {
            "A":"E",
            "B":"J",
            "C":"M",
            "D":"Z",
            "E":"A",
            "F":"L",
            "G":"Y",
            "H":"X",
            "I":"V",
            "J":"B",
            "K":"W",
            "L":"F",
            "M":"C",
            "N":"R",
            "O":"Q",
            "P":"U",
            "Q":"O",
            "R":"N",
            "S":"T",
            "T":"S",
            "U":"P",
            "V":"I",
            "W":"K",
            "X":"H",
            "Y":"G",
            "Z":"D"
        },

        "B" : {
            "A":"Y",
            "B":"R",
            "C":"U",
            "D":"H",
            "E":"Q",
            "F":"S",
            "G":"L",
            "H":"D",
            "I":"P",
            "J":"X",
            "K":"N",
            "L":"G",
            "M":"O",
            "N":"K",
            "O":"M",
            "P":"I",
            "Q":"E",
            "R":"B",
            "S":"F",
            "T":"Z",
            "U":"C",
            "V":"W",
            "W":"V",
            "X":"J",
            "Y":"A",
            "Z":"T"
        },

        "C" : {
            "A":"Y",
            "B":"R",
            "C":"U",
            "D":"H",
            "E":"Q",
            "F":"S",
            "G":"L",
            "H":"D",
            "I":"P",
            "J":"X",
            "K":"N",
            "L":"G",
            "M":"O",
            "N":"K",
            "O":"M",
            "P":"I",
            "Q":"E",
            "R":"B",
            "S":"F",
            "T":"Z",
            "U":"C",
            "V":"W",
            "W":"V",
            "X":"J",
            "Y":"A",
            "Z":"T"
        }
}




def reflector(type):
    return rf_types.get(type);