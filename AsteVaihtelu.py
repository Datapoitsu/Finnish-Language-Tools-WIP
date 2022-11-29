#Eng. Consonant gradation
#Word goes from "tyttö" to "tytön", where consonant is either lost or added

class Vaihtelu:
    def __init__(self, base, bent):
        self.base = base
        self.bent = bent

Vaihtelut = [
Vaihtelu("kk","k"),
Vaihtelu("k","kk"),
Vaihtelu("pp","p"),
Vaihtelu("p","pp"),
Vaihtelu("tt","t"),
Vaihtelu("t","tt"),
Vaihtelu("k",""),
Vaihtelu("","k"),
Vaihtelu("p","v"),
Vaihtelu("v","p"),
Vaihtelu("t","d"),
Vaihtelu("d","t"),
Vaihtelu("nk","ng"),
Vaihtelu("ng","nk"),
Vaihtelu("k","k"),
Vaihtelu("mp","mm"),
Vaihtelu("mm","mp"),
Vaihtelu("lt","ll"),
Vaihtelu("ll","lt"),
Vaihtelu("nt","nn"),
Vaihtelu("nn","nt"),
Vaihtelu("rt","rr"),
Vaihtelu("rr","rt"),
Vaihtelu("k","j"),
Vaihtelu("j","k"),
Vaihtelu("k","v"),
]

for i in range(len(Vaihtelut)):
    print("Ba: " + Vaihtelut[i].base + ", Be: " + Vaihtelut[i].bent)

