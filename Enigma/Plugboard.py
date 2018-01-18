class Plugboard:
    def __init__(self,remap=[]):
        self.mapping = {
            "A":"A",
            "B":"B",
            "C":"C",
            "D":"D",
            "E":"E",
            "F":"F",
            "G":"G",
            "H":"H",
            "I":"I",
            "J":"J",
            "K":"K",
            "L":"L",
            "M":"M",
            "N":"N",
            "O":"O",
            "P":"P",
            "Q":"Q",
            "R":"R",
            "S":"S",
            "T":"T",
            "U":"U",
            "V":"V",
            "W":"W",
            "X":"X",
            "Y":"Y",
            "Z":"Z"
        }

        for c1,c2 in remap:
            temp = self.get(c1);
            self.mapping.update({ c1:c2 });
            self.mapping.update({ c2:temp });
    
    def get(self,char):
        return self.mapping.get(char);