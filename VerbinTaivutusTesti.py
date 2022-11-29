import VerbinTaivutus as VT

class T:
    def __init__(self, sana, luokka):
        self.sana = sana
        self.luokka = luokka

Testattavat = [
    T("helpottua",52),
    T("rikkoa", 52),
    T("yöpyä", 52),
    T("säilöä", 52),
    
    
    T("laskea", 58),
    T("kylpeä", 58),
    
    
    T("lähteä", 60),
    
    T("hankkia",61),
    T("möyriä",61),
    
    T("ideoida",61),
    T("liisteröidä",61),
    
    T("jäädä",63),
    T("myydä",63),
    T("saada",63),
    T("aikaansaada",63),
    
    T("juoda",64),
    T("lyödä",64),
    T("viedä",64),
    
    T("käydä",65),
    
    T("juosta",66),
    T("piestä",66),
    
    T("jahkailla",67),
    T("irvistellä",67),
    
    T("haravoida",68),
    T("ikävöidä",68),
    
    T("palkita",69),
    T("merkitä",69),
    
    T("TTTTTT",68),
    ]

for i in range(len(Testattavat)):
    if str(Testattavat[i].luokka) != str(VT.EtsiTaivutusTyyppi(Testattavat[i].sana)):
        print("Wanted:" + str(Testattavat[i].luokka) + ", Got: " + str(VT.EtsiTaivutusTyyppi(Testattavat[i].sana)) + ", Sana: " + Testattavat[i].sana)
