import AsteVaihtelu as av

class p:
    def __init__ (self,sana,paatteet,haluttu):
        self.sana = sana
        self.paatteet = paatteet
        self.haluttu = haluttu

sanoja = [
    p("takki",[],"takki"),
    p("takki",["n"],"taki"),
    p("takki",["in"],"takki"),
    p("takki",["nne"],"takki"),
    p("takki",["sta"], "taki"),
    p("takki",["lta","nne"], "taki"),
    p("takki",["sta","nne"], "taki"),
    p("mäki",["n"], "mäi"),
    ]

#sanoja = ["takki","takkin","takkiin","takkinne","takkistanne","nappi","nappin","matti","mattin","rampa","ranta","ranka","omppu"]


count = 0
for i in range(len(sanoja)):
    print("---------------------------------")
    tulos = av.AsteVaihtelu(sanoja[i].sana,sanoja[i].paatteet)
    if tulos != sanoja[i].haluttu:
        count += 1

        print("input: " + sanoja[i].sana + " " + str(sanoja[i].paatteet) + ", wanted: " + sanoja[i].haluttu + ", got: " + tulos)
if count == 0:
    print("No flaws, yay")