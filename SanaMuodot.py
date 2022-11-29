# -------------------- Taivuttaja ------------------------- #
#Tehnyt: Aarni Junkkala

#Tämän harjoituksen tarkoituksena on tutkia, että onko suomen kielen rakenne, niin loogista,
#että niihin voisi rakentaa säännöt.
#Tarkoituksena on myös, että ohjelma ei tarvitsisi valmista kirjastoa suomen sanastosta.
#Säännöissä on useasti poikkeuksia.
#Esim: Tavutuksessa diftongit vaikuttavat paljon, mutta antavat poikkeus maisen vaikutelman
#Poikkeuksia on useasti vanhoissa suomen kielen sanoissa. Esim: (uusi sana) Lasi -> lasin, (vanha sana) vesi -> veden

#Genetiivi - omistus muoto
#yleensä päättyy lisäämällä "n" kirjaimen loppuun

#POHDINTAA:
#onko tämä edes mahdollista, vaikeuksia: sanat joilla on monta tarkoitusta taivutetaan eritavalla
#esimerkki: vuori -> vuoren (maakohouma) || vuori -> vuorin (vaatteen sisäpuoli)
#Toinen poikkeama on sana suti, jonka taivutus muodot poikkeavat, jotta ei sekottuisi suteen
#Kolmas poikkeama on lainasanat, jolloin kaikki säännöt saattavat (ei aina) lentää ikkunasta
#Esim: kyynel -> kyyneleen (nel -> neleen), kennel -> kennelin !!!


#Konsonantti muuntumat:
#joissain sanoissa konsonantti muuttuu. Logiikkaa en ole vielä löytänyt, mutta kirjaimet ovat usen samoja
#kannel -> kanteleen    #nn -> nt
#seiväs -> seipään      #v -> p
#poljin -> polkimen     #j -> k
#hylje -> hylkeen       #j -> k
#ommel -> ompeleen      #m -> p

#Vokaali parit toimivat suhteellisen usein samoilla säännöillä
#Parit ovat, aä, oö, uy
#setä -> sedän, rata -> radan
#pulu -> pulun, tyly -> tylyn

#Ratkaistut logiikat:
    #Vain lisäys "n" perään, Prioriteetti: LOW
    #harva -> harvan, ainoa -> ainoan, usea -> usean, sama -> saman, muutama -> muutaman,
    #muu -> muun,  
    #itse -> itsen,
    #tuo -> tuon,
    #se -> sen,

#Toistuvia Kuvioita:

    #YHDISTÄÄ MONIKKO -> Ovat poikkeuksia koska ovat pronomineja
    #idän              ONKO POIKKEUKSIA? Onko koska ei voi käyttää esineistä?
    #me -> meidän
    #te -> teidän
    #he -> heidän
    #iden              ONKO POIKKEUKSIA?
    #nämä -> näiden
    #nuo -> noiden
    #ne -> niiden




    
    

# ----- Mysteeri logiikka ----- #

    # is, as, us
    
    # "as" -> "aan" || "äs" -> "ään" || "is" -> "iin"
        #eräs -> erään           
        #seiväs -> seipään         v -> p ????
        #taivas -> Taivaan
        #kaunis -> kauniin
        #sairas -> sairaan
        #värikäs -> värikkään   #Enemmän kuin kaksi tavua -> astevaihtelu

    # "mat" -> "pien"
        #molemmat -> molempien
        #paremmat -> parempien

    
    #kuka -> kenen    Poikkeus pronomini?

    


    #"n" päätteiset päättyvät "en"
    #hän -> hänen
    #EI PÄDE KAIKKIIN "n" KIRJAIMEEN PÄÄTTYVIIN SANOIHIN.
    #Esim. pakastin -> pakastimen / n -> men ??diftongit??? spesifit vokaalit




    #edeltävät "ä" kirjaimet muuttuvat "u" kirjaimeksi: SELVITÄ MILLOIN "u" vaihto ja milloin ei
    #onko "n" kirjain vaikuttaja???  ONKO PRONOMINI POIKKEUS, onko ei pronomini un päätteisiä
    #minä -> minun
    #sinä -> sinun

    #VAIN "n" lisäys ????
    #tämä -> tämän
    #rämä -> rämän
    #kynä -> kynän 
    #kylmä -> kylmän 
    #kylä -> kylän
    #ikävä -> ikävän
    #pesä -> pesän
    #päivä -> päivän
    #ässä -> ässän
    #ämmä -> ämmän
    
    
    


    #mänty -> männyn ???
    #tyly -> tylyn?????
    #Y ei ole kaikissa kategorioissa
    # A Ä Ö I
    
    # "tä" -> "dän" || "ta" -> "dan" || "tö" -> "dön" || "ti" -> "din"
    # Lisää esimerkkejä "tö" ja "ti" päätteistä
    #pöytä -> pöydän
    #näätä -> näädän
    #setä -> sedän
    #mätä -> mädän
    #hätä -> hädän
    #rata -> radan
    #pata -> padan
    #sota -> sodan
    #kytö -> kydön
    #pati -> padin
    
    # "pi"  -> "vin" || "pa"  -> "van" || "pä"  -> "vän" || "pö"  -> "vön"    ???"py" -> "vyn"???  
    # "ppi" -> "pin" || "ppa" -> "pan" || "ppä" -> "pän" || "ppö" -> "pön"
    # "tti" -> "tin" || "tta" -> "tan" || "ttä" -> "tän" || "ttö" -> "tön"
        #tatti -> tatin
        #ratti -> ratin
        #letti -> letin
        #pefletti -> pefletin
        #timantti -> timantin
        #potta -> potan
        #rotta -> rotan
        #soppa -> sopan
        
        #syöpä -> syövän
        #kyrpä -> kyrvän
        #kääpä -> käävän
    
        #lätty -> lätyn
    
    # "nti" -> nnin || "nta" -> "nnan"
        #tunti -> tunnin
        #panta -> pannan  
        #ranta -> rannan
        #mäntä -> männän

    #käpy -> kävyn
    #läpy -> lävyn
    #levy -> levyn
    #tyly -> tylyn
    #hyppy -> hypyn
    

#TAVUTTAJAA TARVITSEVAT LOGIIKAT
    # "n" kirjain tulee tavujen väliin, tarvitaanko tavuttajaa???????, jotkin näistä päättyvät "n" kirjaimeen, etsi yhteinen tekijä
    # Onko poikkeus pronominejä???
    #joka -> jonka
    #mikä -> minkä
    #jokin -> jonkin
    #kukin -> kunkin
    #joku -> jonkun      ---- Tässä "n" on myös lopussa???????
    #mikin -> minkin,

#EN OSAA OMISTUSMUOTOA TAI EN OLE VARMA
    
    #ken -> kenin tai ?ken -> kenen?
    #kumpikin -> kummankin
    #kumpainenkin -> kumpaisenkin
    #kukaan -> kunkaan
    #kumpikaan -> kummankaan
    #kumpainenkaan -> kumpaisenkaan
    #muuan -> muutaman
    
    # "kään"
    #kenkään -> kenenkään
    #mikään -> minkään
    







import SuomiKieliKirjasto as merkittaja #Kirjasto jakaa kirjanasyötetyt kirjaimet, kirjain tyyppeihin. Vokaalit yms.



def L(sana):
    #Esimerkkejä:
        #poikkeukset  ---> LÖYTYYKÖ MUITA? ONKO LOGIIKKA?
        #kannel -> kanteleen   "n" tilalle "t"
        #ommel -> ompeleen     "m" tilalle "p"
        #kennel -> kennelin == Kaikki lainasanat ovat "in" päätteisiä. VOI PASKA
    
        # "vel" -> "velen"
            #sävel -> sävelen
            #nivel -> nivelen

        # "l" -> "leen"
            #seppel -> seppeleen
            #askel -> askeleen
            #kyynel -> kyyneleen
            #petkel -> petkeleen
            #sammal -> sammaleen
            #taival -> taivaleen
            #vemmel -> vemmeleen
        
    #Poikkeus 1#, muuttaa "nn" tialle "nt", päättyy "een"
    #kannel -> kanteleen
    
    #Poikkeus 2#, muuttaa "mm" tiallle "mp", päättyy "een"
    #ommel -> ompeleen
    
    # "vel" -> "velen"
    # esim. "sävel" -> "sävelen"
    if len(sana) > 3:
        if sana[len(sana) - 3].lower() == "v" and sana[len(sana) - 2].lower() == "e" and sana[len(sana) - 1].lower() == "l":
            return sana + "en"
        
    # Muissa tilanteissa on pääte "een"
    # esim. "askel" -> "askeleen
    return sana + "een"

def N(sana):
    # "in" -> "imen"
        #Jos "tin" pääte ja kaksi tavua -> "ttimen"
        #liitin -> liittimen      
        #siitin -> siittimen
        #soitin -> soittimen
        #keitin -> keittimen
    
        #Jos "tin" pääte ja kolme tai enemmän tavutaja -> "timen"
        #tulostin -> tulostimen  
        #pakastin -> pakastimen
    
        #survin -> survimen
        #puhelin -> puhelimen
        #avain -> avaimen
        #eläin -> eläimen
        #istuin -> istuimen
        #kirjain -> kirjaimen
        #poljin -> polkimen

    #nen -> sen
        #jokainen -> jokaisen
        #toinen -> toisen
        #millainen -> millaisen
        #maalainen -> maalaisen
        #kumpainen -> kumpaisen
        #samainen -> samaisen
    
    # "nen" -> "sen"
    # esim. "toinen" -> "toisen"
    if len(sana) > 2:
        if sana[len(sana) - 3].lower() == "n" and sana[len(sana) - 2].lower() == "e" and sana[len(sana) - 1].lower() == "n":
            sanaList = list(sana)
            sanaList[len(sanaList) - 3] = "s"
            sana = "".join(sanaList)
            return sana
    
    # "in" -> "imen"
    # esim. "pakastin" -> "pakastimen"
    if len(sana) > 3:
        if sana[len(sana) - 2] == "i" and sana[len(sana) - 1] == "n":
            sanaList = list(sana)
            sanaList[len(sanaList) - 1] = "m"
            sana = "".join(sanaList)
            sana += "en"
            return sana

def E(sana):
    # "e" -> "een"          #yksittäisestä konsonantista tulee tupla kun tavuja on kaksi
        #HUOM. Astevaihtelu
        #pääte -> päätteen
        #siite -> siitteen
        #tuote -> tuotteen
        #aate -> aatteen
        #lomake -> lomakkeen
        #lääke -> lääkkeen
        #seppele -> seppeleen ????
    # "ee" -> "een"
        #essee -> esseen   
        #tee -> teen
    # tuplakonsonantti "e" päätteessä -> "n"
        #nalle -> nallen
        #kalle -> kallen
        #nukke -> nuken
        #pelle -> pellen
    # "le" -> "len"
        #ale -> alen
        #tele -> telen

    #EI TOIMI VIELÄ:       ETSI YHDISTÄVÄ TEKIJÄ
        #vene -> veneen
        #käärme -> käärmeen
        #perkele -> perkeleen
        #lause -> lauseen
        #ihme -> ihmeen
        #hylje -> hylkeen  # j -> k

    global merkittaja

    #Jos tupla konsonatti ennnen "e" päätettä, tulee perään vain "n" lisä
    #esim. nalle -> nallen
    if len(sana) > 4:
        sanaTyyppi = merkittaja.FindLetterType(sana)
        if  sanaTyyppi[len(sanaTyyppi) - 2] == "k" and sana[len(sana) - 2] == sana[len(sana) - 3]:
            return sana + "n"
    
    #Jos tupla "e", niin pääte "n"
    #esim. "tee" -> "teen" || "essee" -> "esseen"
    if len(sana) > 1: #väh 2 merkkiä  "ee" -> "een"
        if sana[len(sana) - 1] == "e" and sana[len(sana) - 2] == "e":
            return sana + "n"
    
    #Jos "le", niin pääte "len"
    #Esim. "ale" -> "alen" || "tele" -> "telen"
    if len(sana) > 2: #väh 3
        if sana[len(sana) - 2] == "l" and sana[len(sana) - 1] == "e":
            return sana + "n"

    #Jos ei mikään edeltävistä kategorioista, niin "e" -> "een" ja edeltävästä konsonantista tulee tupla.
    #esim. "Tuote" -> "Tuotteen"
    if len(sana) > 2: #väh 3
        sanaTyyppi = merkittaja.FindLetterType(sana)
        if sanaTyyppi[len(sanaTyyppi) - 2] == "k": #Toiseksi viimeisen tulee olla konsonantti
            sanaList = list(sana)
            sanaList[len(sanaList) - 1] = sanaList[len(sanaList) - 2] #Tupla
            sana = "".join(sanaList)
            sana += "een"
            return sana
    
    return sana + "en" #Jos mikään ei toimi, niin paikataan "en" päätteellä
    
def I(sana):
    # ----- i päätten taivutus ohjeet ----- #
    
    # "n" pääte
        #lasi -> lasin
            #Tupla vokaali edeltävässä tavuss?
        #siili -> siilin
        #viini -> viinin
        #kaali -> kaalin

    # "si" -> "den"        jos i edeltävä vokaali on "e", "ä", tai "u", niin s kirjaimen tilalle d
        #vesi -> veden
        #käsi -> käden
        #susi -> suden
    
    # "ti" -> "den"
        #lehti -> lehden
        #suti -> sudin ??????? WTF,            Liittyy varmaan susi -> suden, jolloin suti ei voi olla suden. FUUUK
    
    # i -> en
        #meri -> meren
        #liemi -> liemen
        #lumi -> lumen
        #pieni -> pienen
        #suuri -> suuren
        #pilvi -> pilven
        #kieli -> kielen
        #nimi -> nimen
        #moni -> monen            
        #huuli -> huulen                 
    
    #Mysteerit
        #joki -> joen
        #reki -> reen

    #i -> ien     i -> en
    #kaikki -> kaikkien       i -> ien   ? MONIKKO ?
    #ien -> ienen         #Tapa mut
    #RATKAISTUT:
    # "pi" -> "man"
        #kumpi -> kumman,         
        #parempi -> paremman     
        #jompikumpi -> jommankumman #Tekee muutoksen tuplana, koska yhdyssana  ### EI TOIMI VIELÄ ###
    
    # "rsi" -> "rren"
        #varsi -> varren    
        #korsi -> korren
        #pursi -> purren
    
    # "lpi" -> "lven"
        #alpi -> alven
        #helpi -> helven
    
    # "rsi" -> "rren"
    # esim. "varsi" -> varren"
    if len(sana) > 3: #väh 4
        if sana[len(sana) - 3] == "r" and sana[len(sana) - 2] == "s" and sana[len(sana) - 1] == "i":
            sanaList = list(sana)
            sanaList[len(sanaList) - 2] = "r"
            sanaList[len(sanaList) - 1] = "e"
            sana = "".join(sanaList)
            sana += "n"
            return sana
    
    # "lpi" -> "lven"
    #alpi -> alven
    if len(sana) > 3: #väh 4
        if sana[len(sana) - 3] == "l" and sana[len(sana) - 2] == "p" and sana[len(sana) - 1] == "i":
            sanaList = list(sana)
            sanaList[len(sanaList) - 2] = "v"
            sanaList[len(sanaList) - 1] = "e"
            sana = "".join(sanaList)
            sana += "n"
            return sana

    # "pi" -> "man"
    # esim. kumpi -> kumman 
    if len(sana) > 3: #väh 4
        if sana[len(sana) - 2] == "p" and sana[len(sana) - 1] == "i":
            sanaList = list(sana)
            sanaList[len(sanaList) - 2] = "m"
            sanaList[len(sanaList) - 1] = "a"
            sana = "".join(sanaList)
            sana += "n"
            return sana

def yksitavuinen(sana):
    sana += "n"
    return sana

def MuunnaGenetiivi(sana):
    import Tavuttaja
    if len(Tavuttaja.TavutaLause(sana)[0]) == 1: #Jos sana on yks
        return yksitavuinen(sana)
    if sana[len(sana) - 1] == "l": #L
        return L(sana)
    if sana[len(sana) - 1] == "n": #N
        return N(sana)
    if sana[len(sana) - 1] == "e": #E
        return E(sana)
    if sana[len(sana) - 1] == "i": #I
        return I(sana)
while True:
    print(MuunnaGenetiivi(input("Syötä genetiiviksi muutettava sana: ")))