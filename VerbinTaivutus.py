## -------------------- Verbin Taivutus -------------------- ##
#Written by: Aarni Junkkala

# https://fi.wiktionary.org/wiki/Liite:Verbitaivutus/suomi/juoda

class Muoto:
    def __init__(self,persoona):
        self.persoona = persoona # 1= minä, 2= sinä, 3= hän, 4= me, 5= te, 6= he, 7= passiivi
        self.myönteinen = []
        self.kielteinen = []

class Joukko:
    def __init__(self,nimi):
        self.nimi = nimi
        self.Muodot = []
        for i in range(7):
            self.Muodot.append(Muoto(i + 1))
            
class PersoonaMuoto:
    def __init__(self,nimi,nimet):
        Joukot = []
        for i in range(len(nimet)):
            Joukot.append(Joukko(nimet[i]))

class Taivutus:
    def __init__(self,sana):
        self.sana = sana
    
    PersoonaMuodot = []
    PersoonaMuodot.append(PersoonaMuoto("indikatiivi",["preesens","perfekti", "imperfekti", "pluskvamperfekti"]))
    PersoonaMuodot.append(PersoonaMuoto("konditionaali",["preesens","perfekti"]))
    PersoonaMuodot.append(PersoonaMuoto("potentiaali",["preesens", "perfekti"]))
    PersoonaMuodot.append(PersoonaMuoto("imperatiivi",["preesens","perfekti"]))

#Sanasto = Taivutus("juoda")
#print(Sanasto.sana)


# https://kaino.kotus.fi/visk/sisallys.php?p=75
def EtsiTaivutusTyyppi(sana):
    sana = sana.lower()
    
    #Taivutus tyyppejä löytyy väliltä 52-78.

    #52
    # -(u,o) + a / -(y,ö) + ä
    # helpottua,  rikkoa,  yöpyä, säilöä
    if sana[-1] == "a":
        if sana[-2] == "u" or sana[-2] == "o":
            return 52
    if sana[-1] == "ä":
        if sana[-2] == "y" or sana[-2] == "ö":
            return 52

    ## ----------- MYSTERY GROUP of  -(konsonantti) + aa/ää -------- ##
    #53

    #54

    #55


    #56
    # -(konsonantit) + aa
    # ajaa, haastaa, 
    # HUOM versus 57 ja 76

    #57
    #-taa / ?-tää?
    #saartaa
    #HUOM. versus 56 ja 76?

    ## ----------- END OF MYSTERY -------- ##
    
    
    ## ----------- MYSTERY GROUP  -------- ##
    
    #58
    #-kea/keä
    #laskea, kylpeä
    if sana[-3:] == "kea" or sana[-3:] == "keä":
        return 58
    
    #59     
    #-tea
    #tuntea
    #Ainukainen, ei kavereita
    #HUOM. VS 58 ????
    
    ## ----------- END OF MYSTERY -------- ##

    #60
    #-hteä
    #lähteä
    #Ainukainen, ei kavereita
    if sana[-4:] == "hteä":
        return 60
    
    #61
    #-ia, -iä
    #hankkia, möyriä
    if sana[-2:] == "ia" or sana[-2:] == "iä":
        return 61

    #62
    #-oida/-öidä
    #ideoida, liisteröidä
    if sana[-4:] == "oida" or sana[-4:] == "öidä":
        return 62
    #HUOM VS 68!!!!
    
    #63
    # -(vokaali 2x) + da/dä
    #jäädä, myydä, saada, aikaansaada
    if sana[-4] == "a" or sana[-4] == "ä" or sana[-4] == "o" or sana[-4] == "ö" or sana[-4] == "u" or sana[-4] == "y" or sana[-4] == "i" or sana[-4] == "e":
        if sana[-4] == sana[-3]: #Jos samat vokaalit
            if sana[-2] == "d":
                if sana[-1] == "a" or sana[-1] == "ä":
                    return 63

    #64?
    #oda/ödä/edä
    #juoda, lyödä, viedä
    if sana[-3] == "o" or sana[-3] == "ö" or sana[-3] == "e":
        if sana[-2] == "d":
            if sana[-1] == "a" or sana[-1] == "ä":
                return 64
        

    #65?
    #ydä, ?-uda?
    #käydä
    #HUOM. -uda:lle ei löydy sanaa, mutta uskoakseni kuuluu tänne.
    if sana[-3] == "y" or sana[-3] == "u":
        if sana[-2] == "d":
            if sana[-1] == "a" or sana[-1] == "ä":
                return 65
    
    #66
    #-sta
    # rohkaista
    #Huom vs 70
    if sana[-3:-1] == "st":
        if sana[-1] == "a" or sana[-1] == "ä":
            return 70
        
    #67
    #-lla/-llä
    #jahkailla, irvistellä 
    if sana[-3:-1] == "ll":
        if sana[-1] == "a" or sana[-1] == "ä":
            return 67
    #68?
    #ida/-idä
    # haravoida, ikävöidä
    if sana[-3:-1] == "id":
        if sana[-1] == "a" or sana[-1] == "ä":
            return 68

    #69
    #-ita/-itä
    # palkita, merkitä
    if sana[-3:-1] == "it":
        if sana[-1] == "a" or sana[-1] == "ä":
            return 69
    #70
    # -sta/-stä
    # juosta, piestä, syöstä
    if sana[-3:-1] == "st":
        if sana[-1] == "a" or sana[-1] == "ä":
            return 70
    #HUOM VS 66
    
    #71
    #-hdä/-hda
    # nähdä, tehdä
    if sana[-3:-1] == "hd":
        if sana[-1] == "a" or sana[-1] == "ä":
            return 71
    
    #72
    #-eta/-etä
    #ilmetä, rohjeta
    if sana[-3:-1] == "et":
        if sana[-1] == "a" or sana[-1] == "ä":
            return 72

    #73
    # -ata/-ätä
    # avata, hertätä
    if sana[-3:] == "ata" or sana[-3:] == "ätä":
        return 73
        
    ## ------- MYSTERY ZONE -------- ##
    #Etsi ero

    #74
    #-(e,o,u,ö,y)ta/tä

    #75
    # -(e,i,o,u,y,ö)-ta/tä
    # aallota, myrkytä

    ## -------- END ZONE ---------- ##

    ## ------- MYSTERY ZONE II -------- ##

    #76
    # -taa/tää
    # tietää, taitaa

    

    #77
    # -jaa/jää
    # heläjää

    #78
    # -kaa/-kää pääte
    # kaikaa
    # Huom. Jutaa?    
    ## -------- END ZONE ---------- ##
print(EtsiTaivutusTyyppi("juosta"))