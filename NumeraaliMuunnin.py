## -------------------- Numeraali Muunnin -------------------- ## 
#Written by: Veeti Junkkala

#listataan taikalistat, joista löytyy tarpeellinen data numeraalimuunnoksiinn. googol ja googolplex jätetty pois koska ovat käytännössä liian isoja ollakseen hyödyllisiä.
#Listassa numero on joko kymmenen potenssi tai raaka numero, listasta riippuen. Ensimmäinen teksti on perusmuoto ja toinen partitiivi.

PotenssiNumeraalit = \
    [
        [0, "nolla", "nollaa"],
        [1, "kymmenen", "kymmentä"],
        [2, "sata", "sataa"],
        [3, "tuhat", "tuhatta"],
        [6, "miljoona", "miljoonaa"],
        [9, "miljardi", "miljardia"],
        [12, "biljoona", "biljoonaa"],
        [18, "triljoona", "triljoonaa"],
        [24, "kvardriljoona", "kvardriljoonaa"],
        [30, "kvintiljoona", "kvintiljoonaa"],
        [36, "sekstiljoona", "sekstiljoonaa"],
        [42, "septiljoona", "septiljoonaa"],
        [48, "oktiljoona", "oktiljoonaa"],
        [54, "noniljoona", "noniljoonaa"],
        [54, "noviljoona", "noviljoonaa"],
        [60, "dekiljoona", "dekiljoonaa"]
    ]
MuutNumeraalit = \
    [
        [1, "yksi", "yhtä"],
        [2, "kaksi", "kahta"],
        [3, "kolme", "kolmea"],
        [4, "neljä", "neljää"],
        [5, "viisi", "viittä"],
        [6, "kuusi", "kuutta"],
        [7, "seitsemän", "seitsemää"],
        [8, "kahdenksan", "kahdeksaa"],
        [9, "yhdeksän", "yhdeksää"],
    ]
PoikkeusNumeraalit = \
    [
        [11, "yksitoista", "yhtätoistaa"],
        [12, "kaksitoista", "kahtatoistaa"],
        [13, "kolmetoista", "kolmeatoistaa"],
        [14, "neljätoista", "neljäätoistaa"],
        [15, "viisitoista", "viittätoistaa"],
        [16, "kuusitoista", "kuuttatoistaa"],
        [17, "seitsemäntoista", "seitsemäätoistaa"],
        [18, "kahdenksantoista", "kahdeksaatoistaa"],
        [19, "yhdeksäntoista", "yhdeksäätoistaa"],
    ]
DesimaaliNumeraalit = \
    [
        [1, "kymmenes"],
        [2, "sadas"],
        [3, "tuhannes"],
        [6, "miljoonas"],
        [9, "miljardis"],
        [12, "biljoonas"],
        [18, "triljoonas"],
        [24, "kvardriljoonas"],
        [30, "kvintiljoonas"],
        [36, "sekstiljoonas"],
        [42, "septiljoonas"],
        [48, "oktiljoonas"],
        [54, "noniljoonas"],
        [60, "dekiljoonas"],
    ]
 
 #Testaa, onko annettu luku kelvollinen luku. Oikeastaan tarpeellinen vain, jos luku annetaan stringinä.
def onkoLuku(luku):
    luku = str(luku)

    if len(luku) == 0:
        return False

    if(luku[0] == "-"):
        luku = luku[1:]

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

    for i in range(len(DesimaaliNumeraalit)-1, -1, -1):
        if DesimaaliNumeraalit[i][0] == desimaalienmaara:
            return DesimaaliNumeraalit[i][1] 
        if(DesimaaliNumeraalit[i][0] < desimaalienmaara):
            return DesimaaliNumeraali(desimaalienmaara - DesimaaliNumeraalit[i][0]) + DesimaaliNumeraalit[i][1]

#Tämä funktio tekee juuri sitä, mitä odotat sen tekevän
def MuunnaNumeraaliksi(numero):
    #Ensin varmistetaan, että numero on kelpoisessa muodossa
    numero = str(numero)
    if not onkoLuku(numero):
        return False

    #Sen jälkeen erotellaan numero osiin desimaalierottimesta ja käsitellään miinus merkki
    ennenDesimaaliErotinta = JalkeenDesimaaliErottimen = ""
    tulos = ""

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
    if(ennenDesimaaliErotinta != 0 and ennenDesimaaliErotinta < 10):
        tulos += MuutNumeraalit[ennenDesimaaliErotinta-1][1]
    elif(ennenDesimaaliErotinta > 10 and ennenDesimaaliErotinta < 20): # 10-20 => poikkeus
        tulos += PoikkeusNumeraalit[ennenDesimaaliErotinta-11][1]
    else:
        for i in range(len(PotenssiNumeraalit)-1, -1, -1):
            if(i == 0):
                #Seuraava jos estää nollan ilmaantuumisen desimaalien, joissa ei ole kokonaista numeroa ollenkaan, alussa
                if JalkeenDesimaaliErottimen == 0:
                    tulos += "nolla"
                break
            if(10 ** PotenssiNumeraalit[i][0] * 2 <= ennenDesimaaliErotinta):
                #Huomaa rekursio; Tässä tilanteessa, on numerosta erotettu isoin kokonainen nimetty numero, joka siihen mahtuu. Täytyy kuitenkin nimetä luku, joka osoittaa montako näitä on, ja mahdolliset luvut tämän jälkeen.
                tulos += MuunnaNumeraaliksi(str(ennenDesimaaliErotinta)[:len(str(ennenDesimaaliErotinta))-len(str(10 ** PotenssiNumeraalit[i][0]))+1]) + PotenssiNumeraalit[i][2]
                #Jos jäljelle jää vain nolla, ei sitä tarvitse nimetä
                if(ennenDesimaaliErotinta % 10 ** PotenssiNumeraalit[i][0] != 0):
                    tulos += MuunnaNumeraaliksi(ennenDesimaaliErotinta % 10 ** PotenssiNumeraalit[i][0])
                break
            if(10 ** PotenssiNumeraalit[i][0] <= ennenDesimaaliErotinta):
                #Tänne päädytään, jos isointa sopivaa nimettyä lukua on vain yksi kappale.
                tulos += PotenssiNumeraalit[i][1]
                if(ennenDesimaaliErotinta % 10 ** PotenssiNumeraalit[i][0] != 0):
                    tulos += MuunnaNumeraaliksi(ennenDesimaaliErotinta % 10 ** PotenssiNumeraalit[i][0])
                break

    if(JalkeenDesimaaliErottimen > 0):
        if(ennenDesimaaliErotinta > 0):
            tulos += " ja "
        tulos += MuunnaNumeraaliksi(JalkeenDesimaaliErottimen) + " " + DesimaaliNumeraali(DecimalPlace) + "osaa"

    return tulos


#Pieni pätkä, joka antaa testata koodia kun sitä ei käytetä kirjastona
if __name__ == '__main__':
    while True:
        print("Syötä luku jonka haluat muuttaa numeraaleiksi, tai q poistuaksesi.")
        numero = input()

        if numero in ["q", "Q"]:
            break

        tulos = MuunnaNumeraaliksi(numero)
        if tulos is False:
            print("Syötäthän luvun, eikä mitä ikinä tuo olikaan!")
            continue
        else:
            print(tulos)
