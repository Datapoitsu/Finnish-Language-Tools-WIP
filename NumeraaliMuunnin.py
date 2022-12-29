## -------------------- Numeraali Muunnin -------------------- ##
#Written by: Veeti Junkkala
 
 #Testaa, onko annettu luku kelvollinen luku. Oikeastaan tarpeellinen vain, jos luku annetaan stringinä.
def onkoLuku(luku):
    luku = str(luku)

    if len(luku) == 0:
        return False

    if(luku[0] == "-"):
        luku = luku[1:]

    desimaaliErotinLoydetty = False
    for char in luku:
        if(char not in "1234567890.,"):
            return False
        elif char in ".,":
            if desimaaliErotinLoydetty:
                return False
            desimaaliErotinLoydetty = True
    
    return True

def DesimaaliNumeraali(desimaalienmaara):
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

    for i in range(len(DesimaaliNumeraalit)-1, -1, -1):
        if DesimaaliNumeraalit[i][0] == desimaalienmaara:
            return DesimaaliNumeraalit[i][1] 
        if(DesimaaliNumeraalit[i][0] < desimaalienmaara):
            return DesimaaliNumeraali(desimaalienmaara - DesimaaliNumeraalit[i][0]) + DesimaaliNumeraalit[i][1]
    

def MuunnaNumeraaliksi(numero):
    inputString = str(numero)
    
    if not isANumber(inputString):
        return False

    beforeDecimalPoint = afterDecimalPoint = ""
    result = ""

    if inputString[0] == "-":
        result = "miinus "
        inputString = inputString[1:]

    desimaaliErotinLoydetty = False
    while len(inputString) != 0:
        if inputString[0] in ",.":
            desimaaliErotinLoydetty = True
            inputString = inputString[1:]
            continue

        if not desimaaliErotinLoydetty:
            beforeDecimalPoint += inputString[0]
        else:
            afterDecimalPoint += inputString[0]

        inputString = inputString[1:]

    if beforeDecimalPoint == "":
        beforeDecimalPoint = 0
    beforeDecimalPoint = int(beforeDecimalPoint)
    
    if afterDecimalPoint == "":
        afterDecimalPoint = "0"
    DecimalPlace = len(afterDecimalPoint)
    afterDecimalPoint = int(afterDecimalPoint)

    #Before Decimal Point
    Numeraalit = \
    [
        [0, "nolla", "nollaa"],
        [1, "yksi", "yhtä"],
        [2, "kaksi", "kahta"],
        [3, "kolme", "kolmea"],
        [4, "neljä", "neljää"],
        [5, "viisi", "viittä"],
        [6, "kuusi", "kuutta"],
        [7, "seitsemän", "seitsemää"],
        [8, "kahdenksan", "kahdeksaa"],
        [9, "yhdeksän", "yhdeksää"],
        [10, "kymmenen", "kymmentä"],
        [100, "sata", "sataa"],
        [1000, "tuhat", "tuhatta"],
        [int(1e6), "miljoona", "miljoonaa"],
        [int(1e9), "miljardi", "miljardia"],
        [int(1e12), "biljoona", "biljoonaa"],
        [int(1e18), "triljoona", "triljoonaa"],
        [int(1e24), "kvardriljoona", "kvardriljoonaa"],
        [int(1e30), "kvintiljoona", "kvintiljoonaa"],
        [int(1e36), "sekstiljoona", "sekstiljoonaa"],
        [int(1e42), "septiljoona", "septiljoonaa"],
        [int(1e48), "oktiljoona", "oktiljoonaa"],
        [int(1e54), "noniljoona", "noniljoonaa"],
        [int(1e60), "dekiljoona", "dekiljoonaa"]
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

    if(beforeDecimalPoint > 10 and beforeDecimalPoint < 20):
        result += PoikkeusNumeraalit[beforeDecimalPoint-11][1]
    else:
        for i in range(len(Numeraalit)-1, -1, -1):
            if(i == 0):
                result += "nolla"
                break
            if(Numeraalit[i][0] * 2 <= beforeDecimalPoint):
                result += MuunnaNumeraaliksi(str(beforeDecimalPoint)[:len(str(beforeDecimalPoint))-len(str(Numeraalit[i][0]))+1]) + Numeraalit[i][2]
                if(beforeDecimalPoint%Numeraalit[i][0] != 0):
                    result += MuunnaNumeraaliksi(beforeDecimalPoint%Numeraalit[i][0])
                break
            if(Numeraalit[i][0] <= beforeDecimalPoint):
                result += Numeraalit[i][1]
                if(beforeDecimalPoint%Numeraalit[i][0] != 0):
                    result += MuunnaNumeraaliksi(beforeDecimalPoint%Numeraalit[i][0])
                break

    if(afterDecimalPoint > 0):
        result += " ja " + MuunnaNumeraaliksi(afterDecimalPoint) + " " + DesimaaliNumeraali(DecimalPlace) + "osaa"
        

    #print(result)
    #print(beforeDecimalPoint)
    #print(".")
    #print(afterDecimalPoint)

    return result

if __name__ == '__main__':
    while True:
        print("Syötä luku jonka haluat muuttaa numeraaleiksi, tai q poistuaksesi.")
        inputString = input()

        if inputString in ["q", "Q"]:
            break

        result = MuunnaNumeraaliksi(inputString)
        if result is False:
            print("Syötäthän luvun, eikä mitä ikinä tuo olikaan!")
            continue
        else:
            print(result)