## -------------------- Numeraali Muunnin -------------------- ## 
#Written by: Veeti Junkkala

#listataan taikalistat, joista löytyy tarpeellinen data numeraalimuunnoksiinn. googol ja googolplex jätetty pois koska ovat käytännössä liian isoja ollakseen hyödyllisiä.
#Listassa numero on joko kymmenen potenssi tai raaka numero, listasta riippuen. Ensimmäinen teksti on perusmuoto, toinen partitiivi ja kolmas järjestysnumero.

PotenssiNumeraalit = \
    [
        [0, "nolla", "nollaa", "nollannes"],
        [1, "kymmenen", "kymmentä", "kymmenes"],
        [2, "sata", "sataa", "sadas"],
        [3, "tuhat", "tuhatta", "tuhannes"],
        [6, "miljoona", "miljoonaa", "miljoonas"],
        [9, "miljardi", "miljardia", "miljardis"],
        [12, "biljoona", "biljoonaa", "biljoonas"],
        [18, "triljoona", "triljoonaa", "triljoonas"],
        [24, "kvardriljoona", "kvardriljoonaa", "kvardriljoonas"],
        [30, "kvintiljoona", "kvintiljoonaa", "kvintiljoonas"],
        [36, "sekstiljoona", "sekstiljoonaa", "sekstiljoonas"],
        [42, "septiljoona", "septiljoonaa", "septiljoonas"],
        [48, "oktiljoona", "oktiljoonaa", "oktiljoonas"],
        [54, "noniljoona", "noniljoonaa", "noniljoonas"],
        [54, "noviljoona", "noviljoonaa", "noviljoonas"],
        [60, "dekiljoona", "dekiljoonaa", "dekiljoonas"]
    ]
MuutNumeraalit = \
    [
        [1, "yksi", "yhtä", "yhdes"],
        [2, "kaksi", "kahta", "kahdes"],
        [3, "kolme", "kolmea", "kolmas"],
        [4, "neljä", "neljää", "neljäs"],
        [5, "viisi", "viittä", "viides"],
        [6, "kuusi", "kuutta", "kuudes"],
        [7, "seitsemän", "seitsemää", "seitsemäs"],
        [8, "kahdenksan", "kahdeksaa", "kahdeksas"],
        [9, "yhdeksän", "yhdeksää", "yhdeksäs"],
    ]
PoikkeusNumeraalit = \
    [
        [11, "yksitoista", "yhtätoistaa", "yhdestoistas"],
        [12, "kaksitoista", "kahtatoistaa", "kahdestoistas"],
        [13, "kolmetoista", "kolmeatoistaa", "kolmastoistas"],
        [14, "neljätoista", "neljäätoistaa", "neljästoistas"],
        [15, "viisitoista", "viittätoistaa", "viidestoistas"],
        [16, "kuusitoista", "kuuttatoistaa", "kuudestoistas"],
        [17, "seitsemäntoista", "seitsemäätoistaa", "seitsemästoistas"],
        [18, "kahdenksantoista", "kahdeksaatoistaa", "kahdeksastoistas"],
        [19, "yhdeksäntoista", "yhdeksäätoistaa", "yhdeksästoistas"],
    ]
PoikkeusJarjestysNumerot = \
    [
        [1, "ensimmäinen"],
        [2, "toinen"],
    ]
 
 #Testaa, onko annettu luku kelvollinen luku. Oikeastaan tarpeellinen vain, jos luku annetaan stringinä.
def onkoLuku(luku):
    luku = str(luku)

    if len(luku) == 0:
        return False

    if(luku[0] == "#"):
        luku = luku[1:]
        if len(luku) == 0:
            return False
        
    if(luku[-1] == "."):
        luku = luku[:-1]
        if len(luku) == 0:
            return False
        
    if(luku[0] == "-"):
        luku = luku[1:]
        if len(luku) == 0:
            return False

    desimaaliErotinLoydetty = False
    for merkki in luku:
        if(merkki not in "1234567890.,"):
            return False
        elif merkki in ".,":
            if desimaaliErotinLoydetty:
                return False
            desimaaliErotinLoydetty = True
    
    return True

#Sisäinen funktio, jota käytetää desimaalilukujen "jakajien" numeraalien muodostamiseen
def DesimaaliNumeraali(desimaalienmaara):

    for i in range(len(PotenssiNumeraalit)-1, -1, -1):
        if PotenssiNumeraalit[i][0] == desimaalienmaara:
            return PotenssiNumeraalit[i][3] 
        if(PotenssiNumeraalit[i][0] < desimaalienmaara):
            return DesimaaliNumeraali(desimaalienmaara - PotenssiNumeraalit[i][0]) + PotenssiNumeraalit[i][3]

#indikoitoistalukua tarkoittaa sitä, miten esimerkiksi "kaksikymmentäkolme":ssa "kaksi" indikoi kymmeniä.
def MuunnaNumeraaliksi(numero, jarjestysnumero = False, indikoitoistalukua = False):
    #Ensin varmistetaan, että numero on kelpoisessa muodossa
    numero = str(numero)
    if not onkoLuku(numero):
        return False

    #Sen jälkeen erotellaan numero osiin desimaalierottimesta ja käsitellään miinus ja järjestys merkit
    ennenDesimaaliErotinta = JalkeenDesimaaliErottimen = ""
    tulos = ""
    
    jarjestysnumero = numero[0] == "#" or numero[-1:] == "." or jarjestysnumero
    if numero[0] == "#":
        numero = numero[1:]
    if numero[-1] == "#":
        numero = numero[:-1]
    

    if numero[0] == "-":
        tulos = "miinus "
        numero = numero[1:]

    desimaaliErotinLoydetty = False
    while len(numero) != 0:
        if numero[0] in ",.":
            desimaaliErotinLoydetty = True
            numero = numero[1:]
            continue

        if not desimaaliErotinLoydetty:
            ennenDesimaaliErotinta += numero[0]
        else:
            JalkeenDesimaaliErottimen += numero[0]

        numero = numero[1:]

    if ennenDesimaaliErotinta == "":
        ennenDesimaaliErotinta = 0
    ennenDesimaaliErotinta = int(ennenDesimaaliErotinta)
    
    if JalkeenDesimaaliErottimen == "":
        JalkeenDesimaaliErottimen = "0"
    DecimalPlace = len(JalkeenDesimaaliErottimen)
    JalkeenDesimaaliErottimen = int(JalkeenDesimaaliErottimen)

    #Sitten lähtee käsittely
    if(jarjestysnumero and not indikoitoistalukua and ennenDesimaaliErotinta in [1, 2]): # #1 ja #2 => Poikkeus
                tulos += PoikkeusJarjestysNumerot[ennenDesimaaliErotinta-1][1]
    elif(ennenDesimaaliErotinta != 0 and ennenDesimaaliErotinta < 10):
        if(not jarjestysnumero):
            tulos += MuutNumeraalit[ennenDesimaaliErotinta-1][1]
        else:
            tulos += MuutNumeraalit[ennenDesimaaliErotinta-1][3]
    elif(ennenDesimaaliErotinta > 10 and ennenDesimaaliErotinta < 20): # 10-20 => poikkeus
    
        if(not jarjestysnumero):
            tulos += PoikkeusNumeraalit[ennenDesimaaliErotinta-11][1]
        else:
            tulos += PoikkeusNumeraalit[ennenDesimaaliErotinta-11][3]
    else:
        for i in range(len(PotenssiNumeraalit)-1, -1, -1):
            if(i == 0):
                #Seuraava jos estää nollan ilmaantuumisen desimaalien, joissa ei ole kokonaista numeroa ollenkaan, alussa
                if JalkeenDesimaaliErottimen == 0:
                    if(not jarjestysnumero):
                        tulos += "nolla"
                    else:
                        tulos += "nollas"
                break
            if(10 ** PotenssiNumeraalit[i][0] * 2 <= ennenDesimaaliErotinta):
                #Huomaa rekursio; Tässä tilanteessa, on numerosta erotettu isoin kokonainen nimetty numero, joka siihen mahtuu. Täytyy kuitenkin nimetä luku, joka osoittaa montako näitä on, ja mahdolliset luvut tämän jälkeen.
                if (not jarjestysnumero):
                    tulos += MuunnaNumeraaliksi(str(ennenDesimaaliErotinta)[:len(str(ennenDesimaaliErotinta))-len(str(10 ** PotenssiNumeraalit[i][0]))+1], jarjestysnumero, True) + PotenssiNumeraalit[i][2]
                else:
                    tulos += MuunnaNumeraaliksi(str(ennenDesimaaliErotinta)[:len(str(ennenDesimaaliErotinta))-len(str(10 ** PotenssiNumeraalit[i][0]))+1], jarjestysnumero, True) + PotenssiNumeraalit[i][3]
                #Jos jäljelle jää vain nolla, ei sitä tarvitse nimetä
                if(ennenDesimaaliErotinta % 10 ** PotenssiNumeraalit[i][0] != 0):
                    tulos += MuunnaNumeraaliksi(ennenDesimaaliErotinta % 10 ** PotenssiNumeraalit[i][0], jarjestysnumero, indikoitoistalukua)
                break
            if(10 ** PotenssiNumeraalit[i][0] <= ennenDesimaaliErotinta):
                #Tänne päädytään, jos isointa sopivaa nimettyä lukua on vain yksi kappale.
                if (not jarjestysnumero):
                    tulos += PotenssiNumeraalit[i][1]
                else:
                    tulos += PotenssiNumeraalit[i][3]
                if(ennenDesimaaliErotinta % 10 ** PotenssiNumeraalit[i][0] != 0):
                    tulos += MuunnaNumeraaliksi(ennenDesimaaliErotinta % 10 ** PotenssiNumeraalit[i][0], jarjestysnumero, indikoitoistalukua)
                break

    if(JalkeenDesimaaliErottimen > 0):
        if(ennenDesimaaliErotinta > 0):
            tulos += " ja "
        tulos += MuunnaNumeraaliksi(JalkeenDesimaaliErottimen) + " " + DesimaaliNumeraali(DecimalPlace) + "osaa"

    return tulos

# formatoi = sisällytä miinus merkki sekä järjestysnumerolle piste loppuun.
def MuunnaLuvuksi(numeraali):
    Negatiivinen = False
    JarjestysNumero = False
    Kokonaiset = ""
    Osat = ""
    OsienNimittaja = ""

    NumeraalinOsat = numeraali.split(" ")


    if NumeraalinOsat[0].lower() in ("miinus", "negatiivinen"):
        Negatiivinen = True
        NumeraalinOsat = NumeraalinOsat[1:]
        
    if len(NumeraalinOsat) < 1:
        return LuvunMuodostus(Negatiivinen, JarjestysNumero, Kokonaiset, Osat)
    
    if len(NumeraalinOsat) in (1, 4): # 1 == kokonaisluku, 4 == "kokonaisluku" "ja" "osat" "nimittäjä"
        if NumeraalinOsat[0][-1:] == "s":
            JarjestysNumero = True
        Kokonaiset = MuunnaLuvuksiRekursio(NumeraalinOsat[0])
        NumeraalinOsat = NumeraalinOsat[1:]
    
    if len(NumeraalinOsat) < 2: # osat, nimittäjät
        return LuvunMuodostus(Negatiivinen, JarjestysNumero, Kokonaiset, Osat)
    
    Osat = MuunnaLuvuksiRekursio(NumeraalinOsat[0])
    OsienNimittaja = MuunnaLuvuksiRekursio(NumeraalinOsat[1])

    while len(Osat) < len(OsienNimittaja):
        Osat = "0" + Osat

    return LuvunMuodostus(Negatiivinen, JarjestysNumero, Kokonaiset, Osat)

#Rekursiivisesti
def MuunnaLuvuksiRekursio(numeraali):
    if numeraali == "":
        return "1"

    Isoin = 0
    IsoimmanIndeksi = 0
    IsoimmanPituus = 0

    Indeksi = 0
    while Indeksi < len(numeraali) - 1:
        for i in range(len(PotenssiNumeraalit)-1, -1, -1):
            if len(numeraali) + Indeksi >= len(PotenssiNumeraalit[i][1]):
                Numerona = pow(10, PotenssiNumeraalit[i][0])
                Isoin = max(Isoin, Numerona)
                if Isoin == Numerona:
                    IsoimmanIndeksi = Indeksi
                    IsoimmanPituus = len(PotenssiNumeraalit[i][1])
                    Indeksi += IsoimmanPituus
                    if len(numeraali) > Indeksi and numeraali[Indeksi] in ("a", "s"):
                        IsoimmanPituus += 1
                        Indeksi += 1

    return str(MuunnaLuvuksiRekursio(numeraali[:IsoimmanIndeksi]) * Isoin) + MuunnaLuvuksiRekursio(numeraali[IsoimmanIndeksi+IsoimmanPituus:])




#Muunnetaan tiedot luvusta luvuksi
def LuvunMuodostus(Negatiivinen, Jarjestysnumero, Kokonaiset, Osat):
    tulos = ""

    if(Negatiivinen):
        tulos += "-"

    tulos += Kokonaiset
    
    if Osat != "":
        tulos+="."

    tulos += Osat

    if Jarjestysnumero != "":
        tulos+="."
    
    return tulos


#Pieni pätkä, joka antaa testata koodia kun sitä ei käytetä kirjastona
if __name__ == '__main__':
    while True:
        print("Syötä luku jonka haluat muuttaa numeraaleiksi, tai numeraali jonka haluat muuttaa luvuksi, tai q poistuaksesi.")
        numero = input()

        if numero in ["q", "Q"]:
            break

        tulos = MuunnaNumeraaliksi(numero)
        if tulos is False:
            tulos = MuunnaLuvuksi(numero)
            if tulos is False:
                print("Syötäthän luvun tai numeraalin, etkä mitä ikinä tuo olikaan!")
            else:
                print(tulos)
        else:
            print(tulos)