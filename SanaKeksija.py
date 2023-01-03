# -------------------- Sana keksijä -------------------- #
#Tehnyt: Aarni Junkkala

#Suomalaisissa sanoissa on kuvioita, jonka vuoksi sana keksijän luominen on mahdollista
#Sana keksijä ei ole täydellinen, joskus keksii sanan, joka on jo olemassa suomen kielessä.
#Olisin voinut asettaa sana keksijän muotoilemaan sanat, johonkin suomen kieliseen muotoon,
#mutta mielestäni se on huijjaamista. Esim: yivö -> yivöön tai yivössä

#Pohdintaa: koodin olisi voinut rakentaa niin, että koodi generoisi tavun kerrallaan,
#jolloin koodin kirjoittaminen ja lukeminen olisi helpompaa.
#En ole myöskään tyytyväinen koodiin, sillä jotkin kohdat saattavat hajota.

import random
import SuomiKieliKirjasto as kirjasto #Muuntaa sanan kirjain tyypeiksi. Vokaali, konsonantti. Ja antaa listan diftongeista
import Tavuttaja # Auttaa sanan tulkkauksessa -> valmiiksi tavutettu sana on helpompi sanoa

pituus = random.randint(5,7) #Randomisoi sanan pituuden etu käteen

def LisaaVokaali():
    global sananKirjaintyyppi
    global sana
    global jaljella
    global vokaalipaino
    Liikavokaalit =[] #Lista vokaaleista jotka ovat esiintyneet jo kaksi kertaa.
    for i in range(len(sana)):
        for k in range(i): #Toistaa niin pitkälle kuin on sananssa päästy
            if sana[i] == sana[k]:
                Liikavokaalit.append(sana[i])
    edellinenVokaali = ""
    lisattavaKirjain = ""
    #Onko edellinen vokaali, jos on niin tupla vokaali tai konsonantti
    if len(sana) > 0:
        if sananKirjaintyyppi[len(sananKirjaintyyppi) - 1] == "v":
            edellinenVokaali = sana[len(sana) - 1]
    
    #Jos edellinen oli vokaali
    if edellinenVokaali != "":
        if random.randint(0,2): #Tupla vokaali
            lisattavaKirjain = edellinenVokaali
        else: #Diftongi
            lisattavaKirjain = ""
            loopBreaker = 50 #rikkoo loopin, jos sattuu vahinko. TODO: tee koodi niin että ei tarvita
            #Hakee randomisoidun seuraavan kirjaimen, jolla diftongi saadaan aikaan.
            while lisattavaKirjain == "":
                kokeiluKirjain = kirjasto.suomenkielisetVokaalit[random.randint(0,len(kirjasto.suomenkielisetVokaalit) - 1)]
                if edellinenVokaali + kokeiluKirjain in kirjasto.diftongit:
                    lisattavaKirjain == kokeiluKirjain
                    for i in range(len(Liikavokaalit)):
                        if lisattavaKirjain == Liikavokaalit[i]:
                            lisattavaKirjain = ""
                            break
                    
                loopBreaker -= 1
                if loopBreaker == 0:
                    #print("Loopbreaker, difongi")
                    break
    
    #Tilanteet joissa edellinen kirjain on konsonantti
    if edellinenVokaali == "" and lisattavaKirjain == "":
        if vokaalipaino == "":
            #Randomisoi vokaalin
            lisattavaKirjain = kirjasto.suomenkielisetVokaalit[random.randint(0, len(kirjasto.suomenkielisetVokaalit) - 1)]
        elif vokaalipaino == "etu": #Randomisoi etu vokaalin
            lisattavaKirjain = kirjasto.etuVokaalit[random.randint(0,len(kirjasto.etuVokaalit) - 1)]
        elif vokaalipaino == "taka": #Randomisoi taka vokaalin
            lisattavaKirjain = kirjasto.takaVokaalit[random.randint(0,len(kirjasto.takaVokaalit) - 1)]
    
    #print(vokaalipaino)
    #Lisää kirjaimen lopussa
    sana += lisattavaKirjain
    sananKirjaintyyppi += "v"
    jaljella -= 1
    
def LisaaKonsonantti():
    global sananKirjaintyyppi
    global sana
    global jaljella
    lisattavaKirjain = ""
    #Jos edellinen on konsonantti -> konsonantti yhdentymä
    if len(sana) > 1: #Tarvitsee olla jo kaksi kirjainta valmiiksi
        if sananKirjaintyyppi[len(sananKirjaintyyppi) - 1] == "k" and sananKirjaintyyppi[len(sananKirjaintyyppi) - 2] == "k":
            #Kolmenkonsonantin yhtymä
            #voi hajota, koska edeltävät konsonantit eivät välttämättä sovi kolmen yhtymään.
            #esim: rj kar|ja, ei voi olla rjj -> karjja
            
            loopbreaker = 50 #Pelastaa perseeni
            edellisetKirjaimet = sana[len(sana) - 2] + sana[len(sana) - 1]
            #Hakee random konsonantin seuraavaan kirjaimene, jolla yhtymä saadaan aikaan.
            while lisattavaKirjain == "":
                kokeiluKirjain = kirjasto.suomenkielisetKonsonantit[random.randint(0,len(kirjasto.suomenkielisetKonsonantit) - 1)]
                if edellisetKirjaimet + kokeiluKirjain in kirjasto.kahdenKonsonantinYhtymat:
                    lisattavaKirjain == kokeiluKirjain
                loopbreaker -= 1
                if loopbreaker == 0:
                    #print("Loopbreaker, 3KY")
                    break
            
        elif sananKirjaintyyppi[len(sananKirjaintyyppi) - 1] == "k":
            #Kahden konsonantin yhtymä
            loopbreaker = 50
            edellinenKirjain = sana[len(sana) - 1]
            #Hakee random konsonantin seuraavaan kirjaimene, jolla yhtymä saadaan aikaan.
            while lisattavaKirjain == "":
                kokeiluKirjain = kirjasto.suomenkielisetKonsonantit[random.randint(0,len(kirjasto.suomenkielisetKonsonantit) - 1)]
                if edellinenKirjain + kokeiluKirjain in kirjasto.kahdenKonsonantinYhtymat:
                    lisattavaKirjain == kokeiluKirjain
                loopbreaker -= 1
                if loopbreaker == 0:
                    #print("Loopbreaker, 2KY")
                    break
    #Edellinen oli vokaali -> random konsonantti    
    if lisattavaKirjain == "":
        lisattavaKirjain = kirjasto.suomenkielisetKonsonantit[random.randint(0,len(kirjasto.suomenkielisetKonsonantit) - 1)]
    
    sana += lisattavaKirjain
    sananKirjaintyyppi += "k"
    jaljella -= 1


sana = ""
sananKirjaintyyppi = ""
jaljella = 0
# "etu" tai "taka"
vokaalipaino = ""

def Keksi():
    global pituus
    global sana
    global sananKirjaintyyppi
    global jaljella
    global vokaalipaino
    
    jaljella = pituus
    sana = ""
    sananKirjaintyyppi = ""
    
    #Randomisoi vokaalipainon
    if random.randint(0,2):
        vokaalipaino = "etu"
    else:
        vokaalipaino = "taka"
        
    # randomisoidaan ensimmäinen kirjain
    #print("Ensimmäinen kirjain randomisti")
    if random.randint(0,2) == 0: #ensimmäinen konsonantti
        LisaaKonsonantti()
    else:
        LisaaVokaali()
    
    #Loppu sanasta luodaan seuraavalla kaavalla
    while jaljella > 0:
        #print(sana)
        #print("----------")
        if jaljella == 1:
            # Viimeinen on AINA vokaali. Kyllä, on olemassa sanoja suomenkielessä, jotka päättyvät konsonanttiin,
            # mutta luodaksemme luontevia sanoja tulee viimeisen olla vokaali.
            #print("Pakotettu vokaali loppuun")
            LisaaVokaali()
            continue
        elif len(sana) == 1 and sananKirjaintyyppi[0] == "k":
            #Alussa ei saa olla kuin vain yksi konsonantti
            #print("Pakotettu vokaali, koska ensimmäinen on konsonantti")
            LisaaVokaali() 
            continue
        elif jaljella == 2 and sananKirjaintyyppi[len(sananKirjaintyyppi) - 1] == "v":
            # esimerkki: kvkKv -> tilanne johon tarvitaan aitaii -> aittai
            #print("Pakotettu konsonantti, estää kolmois vokaalin lopusta")
            LisaaKonsonantti()
            continue
        elif len(sana) >= 2 and sananKirjaintyyppi[len(sananKirjaintyyppi) - 1] == "v" and sananKirjaintyyppi[len(sananKirjaintyyppi) - 2] == "v":
            #print("Pakotettu konsonantti, koska kaksi vokaalia putkeen")
            #Jos on kaksi vokaalia putkeen, pakottaa konsonantin
            LisaaKonsonantti()
            continue
        elif len(sana) >= 2 and sananKirjaintyyppi[len(sananKirjaintyyppi) - 1] == "k" and sananKirjaintyyppi[len(sananKirjaintyyppi) - 2] == "k":
            #Jos edelliset kaksi on konsonantteja
            
            if sana[len(sana) - 1] == sana[len(sana) - 2]:
                #Edelliset kaksi konsonanttia ovat samat kirjaimet
                #print("Pakko vokaali, koska edelliset kaksi konsonanttia ovat samat kirjaimet")
                LisaaVokaali()
                continue
            
            if random.randint(0,2) == 0: #Vokaali
                #print("Kahden konsonantin jälkeinen vokaali")
                LisaaVokaali()  
                continue    
            else: #Konsonantti
                #Tarkistaa onko kolmenkonsonantin yhtymä mahdollinen
                mahdollista = False
                for i in range(len(kirjasto.kolmenKonsonantinYhtymat)):
                    ekatKirjaimet = kirjasto.kolmenKonsonantinYhtymat[i]
                    ekatKirjaimet = ekatKirjaimet[0] + ekatKirjaimet[1] #Karsii viimeisen kirjaimen pois, jotta voidataan verrata nykyiseen sanaan
                    edeltavatKirjaimet = sana[len(sana) - 2] + sana[len(sana) - 1]
                    if edeltavatKirjaimet == ekatKirjaimet:
                        mahdollista = True
                if mahdollista:
                    #print("Kahden konsonantin jälkeinen konsonanttin jälkeen kolmen konsonantin yhtymä")
                    LisaaKonsonantti()
                    continue
                else:
                    #print("Lisätään vokaali koska kolmenkonsonantin yhtymä ei ole mahdollista")
                    LisaaVokaali()
                    continue
        else:
            #Jos mikään edellisistä skenaariosta ei toteudu, niin lisätään random kirjaimia.
            if random.randint(0,2) == 0: #ensimmäinen konsonantti
                #print("random konsonantti")
                sananKirjaintyyppi += "k"
                sana += kirjasto.suomenkielisetKonsonantit[random.randint(0, len(kirjasto.suomenkielisetKonsonantit) - 1)]
                jaljella -= 1
            else:
                #Jos edellinen on vokaali, niin sama tai diftongiksi
                if len(sana) > 0 and sananKirjaintyyppi[len(sananKirjaintyyppi) - 1] == "v":
                    if random.randint(0,2) == 0: #Sama vokaali uudestaan
                        #print("sama vokaali uudestaan")
                        sananKirjaintyyppi += "v"
                        sana += sana[len(sana) - 1]
                        jaljella -= 1
                    else: #diftongi
                        edellinenKirjain = sana[len(sana) - 1]
                        sopivat = []
                        for d in range(len(kirjasto.diftongit)):
                            if kirjasto.diftongit[d][0] == edellinenKirjain:
                                sopivat.append(kirjasto.diftongit[d][1])
                        if(len(sopivat) > 0):
                            #print("Sopiva diftongi")
                            sananKirjaintyyppi += "v"
                            sana += sopivat[random.randint(0, len(sopivat) - 1)]
                            jaljella -= 1
                            continue
                        elif(len(sopivat) <= 0):
                            #print("ei sopivaa, konsonantilla")
                            sananKirjaintyyppi += "k"
                            sana += kirjasto.suomenkielisetKonsonantit[random.randint(0, len(kirjasto.suomenkielisetKonsonantit) - 1)]
                            jaljella -= 1
                            continue
                else:
                    #print("random vokaali")
                    LisaaVokaali()
                    continue
    return sana   
    
#Pyörittää funktiota toistuvasti, jos ei kutsuta ulkopuolelta
if __name__ == "__main__":
    while True:
        print("------------")
        verratava = Keksi()
        print("Lopullinen sana:")
        print(sananKirjaintyyppi)
        print(pituus)
        # #Tavutus
        print(Tavuttaja.TavutaLause(verratava))
        print(verratava)
        input()