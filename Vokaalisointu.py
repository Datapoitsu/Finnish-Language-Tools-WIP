## -------------------- Vokaalisointu -------------------- ##
## Written by: Aarni Junkkala
import SuomiKieliKirjasto as SKK

#Palauttaa tiedon, että onko sana etu- vai takasointuinen
#Ei toimi yhdyssanojen kanssa, joissa jälkimmäinen sana on neutraali ja etummainen on taka vokaali

def OnTakaVokaalinen(sana):
    #Viimeinen ei neutraali vokaali päättää, että kummalla soinnulla sana päättyy
    sana = sana.split("-")
    for i in range(len(sana)):
        if sana[len(sana) - 1 - i] in SKK.takaVokaalit:
            return True
        if sana[len(sana) - 1 - i] in SKK.etuVokaalit:
            return False
        
    return False #Kaikki neutraaleja -> Etusointu

def PalautaSointuinen(sana):
    Taka = OnTakaVokaalinen(sana)
    if Taka == True:
        sana = sana.replace("A","a")
        sana = sana.replace("O","o")
        sana = sana.replace("U","u")
    if Taka == False:
        sana = sana.replace("A","ä")
        sana = sana.replace("O","ö")
        sana = sana.replace("U","y")
    return sana

if __name__ == '__main__':
    print(PalautaSointuinen("talossA")) #taka
    print(PalautaSointuinen("jäässA"))  #etu
    print(PalautaSointuinen("siilissA"))#neutraali
    print(PalautaSointuinen("hyenassA"))#lainasana
    print(PalautaSointuinen("koriste-esineessA")) #Esimerkki väliviivan jaon tärkeydestä
    
    print(PalautaSointuinen("hellaliesistAAn")) #Esimerkki jossa ei toimi, koska yhdyssana