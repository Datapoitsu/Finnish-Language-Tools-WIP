#Eng. Consonant gradation

#Ei tue yhdyssanoja.
#Sanat tulee syöttää muodossa, perusmuoto+päätet
#Esim: takki+n -> takkin, takki+mme -> takkimme, takki+sta+mme+ko -> takistammeko

#Kaikki astevaihtelu jaetaan kahteen ryhmään, vahva ja heikko aste.
#Pohja sääntö on se,


import Tavuttaja
import SuomiKieliKirjasto as SKK

class AstePari:
    def __init__ (self,vahva,heikko):
        self.vahva = vahva
        self.heikko = heikko

AsteParit = [
    #Kvantitatiivinen astevaihtelu
    AstePari("kk","k"), #Takki -> Takin
    AstePari("pp","p"), #Nappi -> Napin
    AstePari("tt","t"), #Matti -> Matin
    #Kvalitatiivinen astevaihtelu
    AstePari("mp","mm"),#Kampa -> Kamman
    AstePari("nt","nn"),#Kanta -> Kannan
    AstePari("nk","ng"),#Ranka -> Rangan

    AstePari("p","v"),  #Lupa -> Luvan
    AstePari("t","d"),  #Lato -> Ladon

    AstePari("lt","ll"),#pelto -> Pellon
    AstePari("rt","rr"),#Parta -> Parran

    AstePari("k",""),   #Joki -> Joi   (Joen)

    AstePari("lke","lje"),
    AstePari("rke","rje"),
    AstePari("hke","hje"),
]

def SisaltaaDiftongin(tavu):
    for i in SKK.diftongit:
        if i in tavu:
            print("Diftongi")
            return True
    for i in SKK.valjenevatdiftongit:
        if i in tavu:
            print("Diftongi")
            return True
    return False

def SisaltaaTuplaVokaalin(tavu):
    tuplaVokaalit = ["aa","ee","ii","oo","uu","yy","öö","ää","åå"]
    for i in tuplaVokaalit:
        if i in tavu:
            print("Tuplavokaali")
            return True
    return False

#Huom omistusliitteen tulee olla heti astevaihtelun jälkeen
#takki + mme -> takkimme, takki + sta + mme -> takistamme
#Aina saman tavun viimeisestä.
OmistusLiitteet = ["ni","si","nsa","nsä","mme","nne"]
def SisaltaaOmistusLiitteen(sana,tavuIndex, tavut):
    sana = ''.join(str(e) for e in tavut)
    index = -1
    for i in range(tavuIndex + 1):
        index += len(tavut[i])

    for i in OmistusLiitteet:
        if sana.find(i) == index or sana.find(i) == index + 1:
            print("Omistusliite")
            return True
    return False

#Jos is astevaihtelun jälkeen. index kertoo missä astevaihtelu on
#henki -> henkistä, vertailuna henki -> hengen
def isLoppuinen(sana,index):
    if "is" in sana:
        if sana.rfind("is") > index:
            print("is-mi")
            return True
    return False

#Palauttaa astevaihtelullisen pohja sanan.
#Esimerkki: AsteVaihtelu("hattu", ["sta","ni"]) -> "hatu"
#Esimerkki: AsteVaihtelu("laki", ["n"]) -> "lai"
#Esimerkki: AsteVaihtelu("huoli", ["stä"]) -> "huoli"
def AsteVaihtelu(sana,paatteet):

    #Jos ei ole päätettä
    if len(paatteet) == 0:
        print("Ei päätteitä")
        return sana

    #Etsii oikean asteparin tapausta varten.
    AstePariIndex = -1
    AsteKohta = -1 #Kohta jossa astevaihtelu on
    for i in range(len(AsteParit)):
        for k in range(1,len(sana)):
            if sana[k - 1] in SKK.Soinnilliset and sana.rfind(AsteParit[i].vahva) == k:
                AstePariIndex = i
                AsteKohta = k
                break

    #Asteparia ei löytynyt, joten palautetaan sana
    if AstePariIndex == -1:
        print("Ei astevaihtelua")
        return sana

    print("AsteKohta: " + str(AsteKohta))

    #Rakennetaan kokosana päätteineen
    kokoSana = sana
    for i in range(len(paatteet)):
        kokoSana += paatteet[i]
    tavutettu = Tavuttaja.Tavuta(kokoSana)

    # -- Tuplavokaali tai diftongi -- #
    #Etsii tavun, jossa astevaihtelu on
    AsteTavu = ""
    kohta = -1
    print("tavutettu: " + str(tavutettu))
    for i in range(len(tavutettu)):
        if kohta + len(tavutettu[i]) > AsteKohta:
            kohta += len(tavutettu[i])
        else:
            AsteTavu = i + 1
            break

    print("AsteTavu: " + tavutettu[AsteTavu])

    if(SisaltaaDiftongin(tavutettu[AsteTavu]) == True or SisaltaaTuplaVokaalin(tavutettu[AsteTavu])):
        return sana

    #Omistusliite
    #Jos sanassa on omistusliite samassa tavussa kuin astevaihtelu, niin vahva vaihtelu
    if(SisaltaaOmistusLiitteen(sana,AsteTavu,tavutettu)):
        return sana

    #Avotavuinen tai -is-minen,
    if Tavuttaja.Umpitavu(tavutettu[AsteTavu]) not in SKK.konsonantit or isLoppuinen(kokoSana,AsteKohta) == True:
        #return heikko
        print("heikko")
        return sana[:AsteKohta] + AsteParit[AstePariIndex].heikko + sana[AsteKohta + len(AsteParit[AstePariIndex].vahva):]
    print("Vahva")
    return sana

if __name__ == "__main__":
   while True:
       sana = input("Syötä sana, josta testa astevaihtelu: ")
       paatteet = [input("Syötä päätteet: ")]
       print(AsteVaihtelu(sana, paatteet))
       print("--------------------")