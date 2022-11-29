## -------------------- Numeraali muunnin -------------------- ##
#Tehnyt: Aarni Junkkala

#Tarkoituksena on muuttaa luku numero numeraaliksi, esim: 1 -> "yksi", 25.14 -> "kaksikymmentäviisi ja neljätoistasadasosaa".
#Numeraalin desimaalit ilmoitetaan murtolukuna.
#TODO: Murto osat ei toimi, miljoonasosa sanoo tuhannnes osa. Must KORJATA.
#Tarkoituksena on myös, että emme kirjoita kaikkia numeraali lukuja, vaan koodaamme tarvittavien pohjalta.
#Ohjelma jakaa luvun desimaalin kohdalta, koska desimaalin kummaltakin puolen numerot sanotaan samalla tavalla.

#TODO: saman voi kääntää toisin päin, esim: "kaksi" -> 2, "sata" -> 100.

#Suomalaisessa numeraali säännöissä, numero jaetaan 3 luvun setteihin, esim: 23000000 -> 23 000 000.
#Lausunnassa setit käyttävät arvo-osoitinta väliltä 999-2, esim 73 000 -> (seitsemänkymmentäkolme)tuhatta.
#Kolmen setin sääntö ei pädä esim, englannin kielessä, jossa 1200 -> tweleve hundred -> kaksitoistasataa

Perusluvut = ["nolla","yksi", "kaksi", "kolme", "neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän"]
#pienien kertomayksiköiden nimet -> toistuvat isojen kertomayksikköjen osoittimissa
PienetKertomatYksikko = ["kymmenen", "sata"] 
PienetKertomatMonikot = ["kymmenentä", "sataa"]
#Isojen kertomayksiköiden nimet.
IsotKertomatYksikko = ["tuhat", "miljoona", "milrjardi", "biljoona", "triljoona"] 
IsotKertomatMonikko = ["tuhatta", "miljoonaa", "milrjardia", "biljoonaa", "triljoonaa"]
PienetMurtoOsaNimet = ["kymmenes", "sadas"] #Saa olla oikein päin
#Näiden kaikkien jälkee tulee "osa" -> tuhannesosa
IsotMurtoOsaNimet = ["tuhannes", "miljoonas", "miljardis", "biljoonas", "triljoonas"]

def muunnaNumeraaliksi(Luku):
    if Luku == "":
        return
    
    numeraali = "" #palautetaan lopuksi
    
    if Luku[0] == "-": #Miinus
        numeraali += "miinus "
        Luku = Luku[1:] #Poistaa symbolin, jotta lopun datan käsittely helpompaa
        
    Pilkkujako = Luku.split(".") #Jakaa pilkun kohtaa poikki, jotta helpompi käsitellä
    if len(Pilkkujako) > 1:  #Jos desimaalin jälkeen vain nolla, niin poistetaan
        if Pilkkujako[1] == "0": 
            Pilkkujako.pop(1)
    
    # -- Pilkkujaon rikonta arvo-osoittimiin -- #
    #Rikkoo pilkkujaon kolmen numeron Arvo osoittimiin, esim: 12345678.4321 -> [[12,345,678][4,321]].
    #Kolmen setit aloitetaan oikealta vasemmalle, jolloin vajaaksi jäänyt on vasemmalla.
    
    ArvoOsoittimet = []
    for i in range(len(Pilkkujako)):
        LukuHolder = Pilkkujako[i]
        holder = []
        var = ""
        laskuri = 0
        for k in range(len(LukuHolder)):
            var = LukuHolder[-(k + 1)] + var
            laskuri += 1
            if laskuri == 3 or k == len(LukuHolder) - 1:
                laskuri = 0
                holder.insert(0,var)
                var = ""
        ArvoOsoittimet.append(holder)
    
    # -- Desimaaliluvun päätteet -- #
    #Päättelee päätteen yksiköllisyyden tai monikollisuuden
    paate = ""
    if len(ArvoOsoittimet) > 1: #Vain jos on desimaali lukuja
        #Etsii, päätteen yksikön tai monikon
        Yksikko = True
        for x in range(len(Pilkkujako[1])):
            if x < len(Pilkkujako[1]) - 1:
                if Pilkkujako[1][x] != "0":
                    Yksikko = False
                    break
            else:
                if Pilkkujako[1][x] == "1":
                    Yksikko = True
                else:
                    Yksikko = False
        
        #Etsii osan päätteen
        pituus = 0
        for k in range(len(ArvoOsoittimet[1])):
            for n in range(len(ArvoOsoittimet[1][k])):
                pituus += 1
        PieniOsa = ((pituus + 2) % 3) #kymmens/sadas-osa -> kymmenestuhannes jne. 
        if PieniOsa != 2: #yksien isojen murtosa nimiin ei tule pientäosaa eteen
            paate += PienetMurtoOsaNimet[PieniOsa]
        if pituus > 2:
            IsoOsa = int(((pituus - (pituus % 3))/3) -1)
            paate += IsotMurtoOsaNimet[IsoOsa]
        paate += "osa" #kaikissa murtoluvuissa, jos yksittäinen niin "osa", jos monta niin "osaa"
        if Yksikko == False:
            paate += "a"
            
    # ----- Nollien leikkaus arvo-osoittimien alkupäästä ----- #
    #jotta PienKertomaMuutos funktio osaa toimia annettujen lukujen kanssa
    #Paitsi kokonaislukujen ykkösistä, jos kokonais luku on vain nolla, esimerkit: 1000 -> ['1', ''] tai 3.2 [['3']['2']]
    
    if len(ArvoOsoittimet) == 1 and len(ArvoOsoittimet[0]) == 1 and ArvoOsoittimet[0][0] == "0":
        numeraali += PienKertomaMuutos(ArvoOsoittimet[0][0])
        return numeraali
    # 0.001 -> ei sanota nollaa ennen desimaalia, poistetaan arvo-osoittimesta
    if len(ArvoOsoittimet) == 2 and len(ArvoOsoittimet[0]) == 1 and ArvoOsoittimet[0][0] == "0":
        ArvoOsoittimet[0] = [] 
    for l in range(len(ArvoOsoittimet)):
        for i in range(len(ArvoOsoittimet[l])):
            poistettavat = 0
            for k in range(len(ArvoOsoittimet[l][i])):
                if ArvoOsoittimet[l][i][k] == "0":
                    poistettavat += 1
                else:
                    break
            ArvoOsoittimet[l][i] = ArvoOsoittimet[l][i][poistettavat:]
    
    ## -- Päättelee kirjaimet perustuen arvo-osoittimien mukaan -- ##
    for i in range(len(ArvoOsoittimet)):
        if i == 1 and ArvoOsoittimet[0] != [] : #Asettaa desimaalin kohdalle sanan "ja"
            numeraali += "ja "
            
        for k in range(len(ArvoOsoittimet[i])):
            if len(ArvoOsoittimet[i][k]) == 0 and len(ArvoOsoittimet[i]) > 0:
                continue
            if  k + 1 < len(ArvoOsoittimet[i]) and ArvoOsoittimet[i][k] == "1": #yksittäinen isoKertoma
                #Esim: 1001 -> "(tuhat)yksi" tai 1 002 000 -> (miljoona)kaksituhatta
                numeraali += IsotKertomatYksikko[len(ArvoOsoittimet[i]) - k - 2]
            else:
                numeraali += PienKertomaMuutos(ArvoOsoittimet[i][k])
                if k < len(ArvoOsoittimet[i]) - 1:
                    numeraali += IsotKertomatMonikko[k]
            if i == 0:
                numeraali += " "
    numeraali += paate
    return numeraali
    
def PienKertomaMuutos(Luku):
    #Muuttaa luvun tekstiksi
    #Esim. 123 -> satakaksikymmentäkolme
    #Esim. 52 -> Viisikymmentäkaksi
    #Esim. 4 -> neljä
    if Luku == "": #Tyhjä palautetaan
        return ""
    
    Luku = str(Luku)
    pituus = len(Luku)
    if pituus > 3:#Luku saa olla maximissaan vain kolme merkkiä pitkä
        print("Error: PienKertomaMuutos luvussa enemmän kuin kolme symbolia, korjaa koodisi")
        return ""
    
    numeraali = ""
    if pituus == 3:
        if int(Luku[pituus - 3]) == 1: #Yksittäinen sata
            numeraali += PienetKertomatYksikko[1]
        elif int(Luku[pituus - 3]) != 1: #Useat sadat
            numeraali += Perusluvut[int(Luku[pituus - 3])] + PienetKertomatMonikot[1]
    if pituus >= 2:
        if int(Luku[pituus - 2]) == 1 and int(Luku[pituus - 3]) == 0: #kymmenen
            numeraali += PienetKertomatYksikko[0]
        elif int(Luku[pituus - 2]) == 1: #11-19
            numeraali += Perusluvut[int(Luku[pituus - 1])] + "toista"
        elif int(Luku[pituus - 1]) != 0: #Nollaa ei sanota
            numeraali += Perusluvut[int(Luku[pituus - 2])] + PienetKertomatMonikot[0] #20-90
            if int(Luku[pituus - 1]) != 0: #Nollaa ei sanota
                numeraali += Perusluvut[int(Luku[pituus - 1])] #0-9
    if pituus == 1: #Vain yksikkö
        numeraali += Perusluvut[int(Luku[pituus - 1])] # 0-9
    return numeraali

if __name__ == "__main__":
    while True:
        i = input("Syötä numero: ")
        i = i.replace(" ","") #poistaa välit, matikkaa varten
        i = i.replace(",",".") #korvaa pilkun pisteellä, matikkaa varten
        try:
            print("Numeraalina: " + str(muunnaNumeraaliksi(i)))
            print("--------------------")
        except ValueError:
            print("Error: syötetty arvo ei ole numero")
            print("--------------------")