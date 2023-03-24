## -------------------- Tavuttaja -------------------- ##
#Written by: Aarni Junkkala

import SuomiKieliKirjasto as kirjasto #Sisällyttää listoja suomenkielen rakenteesta.
import SanojenErittelija as erittelija #Jakaa lauseen sanoiksi, jolloin lauseen tavuttaminen on helpompaa

# ----- Tavutuksen säännöt ----- #

#Konsonantteja voi olla tavun alussa vaikka kuinka monta, mutta esiintyy vain ulkomaalaisissa sanoissa. esim: sprint|te|ri
#Erikoismerkit eivät tule tavuihin ja jakaa tavun esim: vaa'assa -> vaa|as|sa
#Yhdyssanat, jonka ensimmäinen päättyy konsonanttiin ja toinen alkaa vokaalilla ei toimi. Mahdoton korjata ilman sanakirjaa. Esim: a|si|an|o|mai|set, näy|tön|oh|jain
#Ei tunnista sanan perusmuotoa. esim: ha|uis|sa VS hau|is|sa, ensimmäinen tarkoittaa hakua ja toinen haukea

# ----- Tavutyyppi funktiot ----- ##
#NOTE: Tarkoitettu taivuttajaa varten, voi olla käyttöä muuallakin

def LyhytTavut(tavu): #Lyhyet tavut päättyvät lyhyeen vokaaliin. Esim. Ki-vi, koi-ra, kis-sa
    if tavu[-1] in kirjasto.vokaalit and tavu[-2] not in kirjasto.vokaalit:
        return True
    return False

def PitkäTavu(tavu): #Kaikki tavut, jotka eivät ole lyhyitä tavuja, ovat pitkiä. Esim. Maa, Kai-vaa, huu-taa, sii-maa
    if LyhytTavut(tavu) == False:
        return True
    return False

def Avotavu(tavu): #Tavu päättyy vokaaliin. Esim. Ka-la, Pe-li, Ki-ta-ra
    if tavu[-1] in kirjasto.vokaalit:
        return True
    return False

def Umpitavu(tavu): #Tavu päättyy konsonanttiin. Esim. Läm-min, kum-man, nal-let
    if tavu[-1] not in kirjasto.vokaalit:
        return True
    return False

# ----- Tavuttajan funktiot ----- #

def HaeKirjainTyypit(sana):
    #HUOM, jos kirjaintyypin hakemiselle tulee tarvetta tämän funktion voi muuttaa omaksi tiedostokseen.
    #Palauttaa sanan kirjain tyypit. v= vokaali, k= konsonantti, e= erikoismerkki.
    #Esim: kissa -> kvkkv, saari -> kvvkv, C-vitamiini -> kekvkvkvvkv
    kirjaintyypit = ""
    for i in range(len(sana)):
        if sana[i] in kirjasto.vokaalit:
            kirjaintyypit += "v"
            continue
        if sana[i] in kirjasto.konsonantit:
            kirjaintyypit += "k"
            continue
        if sana[i] in kirjasto.erikoismerkit:
            kirjaintyypit += "e"
            continue
        if sana[i] in kirjasto.numerot:
            kirjaintyypit += "n"
    return kirjaintyypit

## -- Leikkauksen tarkistukset -- ##
#Jokaiselle kirjain tyypille on oma funktio, joka tarkistaa, että leikataanko tavu.

def TarkistaErikoisMerkki(kirjaintyypit, index):
    if(index + 1 < len(kirjaintyypit)):
        if kirjaintyypit[index + 1] == "e":
            LeikkaaTavu()
            return True
    return False

def TarkistaNumero(kirjaintyypit, index):
    if index + 1 < len(kirjaintyypit):
        if kirjaintyypit[index] != "n" and kirjaintyypit[index + 1] == "n":
            LeikkaaTavu()
            return True
        if kirjaintyypit[index] == "n" and kirjaintyypit[index + 1] != "n":
            LeikkaaTavu()
            return True
    return False

def TarkistaKonsonantti(kirjaintyypit, index):
    #Tarkistaa neljän konsonantin ekstran -> eks|tra
    if index >= 2 and index + 2 < len(kirjaintyypit):
        if kirjaintyypit[index - 1] == "k" and kirjaintyypit[index] == "k" and kirjaintyypit[index + 1] == "k" and kirjaintyypit[index + 2] == "k":
           LeikkaaTavu()
           return True
    #Poikkeavana ekstrassa on se että, t ja r kirjaimen välistä ei leikata.
    if index >= 3 and index + 1 < len(kirjaintyypit):
        if kirjaintyypit[index - 2] == "k" and kirjaintyypit[index - 1] == "k" and kirjaintyypit[index] == "k" and kirjaintyypit[index + 1] == "k":
            return False

    #Tavallinen tavutus konsonanteilla eli seuraava konsonantti ja sitä seuraava vokaali #Esim: saa|ri, olemme siis esimerkissä kirjaimessa a ennen r kirjainta
    if(index + 2 < len(kirjaintyypit)): #Jäljellä kaksi kirjainta sanassa
        if kirjaintyypit[index + 1] == "k" and kirjaintyypit[index + 2] == "v":
            for i in range(index + 1): # Tarkistaa että onko kaikki edeltävät kirjaimet konsonantteja
                if kirjaintyypit[i] == "v": #Jos edeltävä on vokaali, niin poikki
                   LeikkaaTavu()
                   return True
    return False

def TarkistaVokaali(sana, kirjaintyypit, index):
    global tavut
    if(index + 1 < len(kirjaintyypit)): #Jäljellä yksi kirjain
        if kirjaintyypit[index] == "v" and kirjaintyypit[index + 1] == "v": #Molemmat vokaaleja
            # väljenevät diftongit
            if len(tavut) == 0:
                if sana[index] + sana[index + 1] in kirjasto.valjenevatdiftongit:
                    return False
            #Perus diftongi
            if sana[index] + sana[index + 1] in kirjasto.diftongit:
                return False
            #Sama vokaali tuplana
            if sana[index] == sana[index + 1]:
                return False
            #Tave leikataan, koska ei ollut diftongeja
            LeikkaaTavu()
            return True
    return False

#Globaalit muuttujat
tavut = []
tavu = ""

def LeikkaaTavu():
    global tavut
    global tavu
    tavut.append(tavu)
    tavu = ""

def Tavuta(sana):
    if sana == "":
        return False

    global tavut
    global tavu
    tavut = []
    tavu = ""

    #Kirjoittaa ylös isot kirjaimet, niin on helpompi verrata
    isot = []
    for i in range(len(sana)):
        isot.append(sana[i].isupper())
    sana = sana.lower() #sana pieneksi

    #Hakee kirjaintyypit
    kirjaintyypit = HaeKirjainTyypit(sana.lower())
    #Jokainen kirjain tavutetaan niin, että kirjain lisätään tavuun, sitten haistellaan, että leikataanko poikki.
    for i in range(len(sana)):
        if kirjaintyypit[i] != "e": #Erikoismerkkiä ei tule tavuihin
            if isot[i] == True:
                tavu += sana[i].upper()
            if isot[i] == False:
                tavu += sana[i]

        if kirjaintyypit[i] == "e": #Ohitetaan
            continue

        if TarkistaErikoisMerkki(kirjaintyypit, i) == True:
            continue
        if TarkistaKonsonantti(kirjaintyypit, i) == True:
            continue
        if TarkistaVokaali(sana, kirjaintyypit, i) == True:
            continue
        if TarkistaNumero(kirjaintyypit, i) == True:
            continue

        if i == len(sana) - 1:
            LeikkaaTavu()
    return tavut

def TavutaLause(lause):
    sanat = erittelija.MuutaSanoiksi(lause) #Muuttaa lauseen listaksi sanoja
    tavutetutSanat = []
    for i in range(len(sanat)):
        tavutetutSanat.append(Tavuta(sanat[i]))
    return tavutetutSanat

if __name__ == "__main__":
   while True:
       print(TavutaLause(input("Syötä sana, jonka haluat tavuttaa: ")))
       print("--------------------")