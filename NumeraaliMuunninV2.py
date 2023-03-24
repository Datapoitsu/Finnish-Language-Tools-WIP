## -------------------- Numeraali Muunnin -------------------- ##
#Written by: Aarni Junkkala

#Numeraali formaatit
NumeraaliYkkoset = ["nolla","yksi","kaksi","kolme","neljä","viisi","kuusi","seitsemän","kahdeksan","yhdeksän"]
NumeraaliYkkosetPartitiivi = ["nollaa","yhtä","kahta","kolmea","neljää","viittä","kuutta","seitsemää","kahdeksaa","yhdeksää"]

NumeraaliPienKertoma = ["kymmenen","sata"]
NumeraaliPienKertomaPartitiivi = ["kymmentä","sataa"]

KeskiKertoma = "tuhat"
KeskiKertomaPartitiivi = "tuhatta"

#Seuraava luku on aina miljoona kertaa suurempi
NumeraaliSuurKertoma = ["miljoona","miljardi","biljoona","triljoona","kvadriljoona","kvintiljoona","sekstiljoona","septiljoona","oktiljoona","noviljoona","dekiljoona"]
NumeraaliSuurKertomaPartitiivi = ["miljoonaa","miljardia","biljoonaa"]




def MuutaNumeroksi(numeraali):
    print(numeraali)

def MuutaYksikkoNumeraaliksi(numero):
    numero = str(numero)
    if len(numero) > 1:
        return False

    return NumeraaliYkkoset[numero]

#Muuttaa kolmen numeron sarjan numeraaliksi.
def MuutaKolmikkoNumeraaliksi(numero):
    print("Kolmen sarja: " + str(numero))
    sana = ""
    numero = str(numero)
    #Tarkistetaan sataset
    #if len(numero) == 3:
        #if numero[0] == 1:
            










def MuutaNumeraaliksi(numero):
    #Muuttaa numeron stringiksi, jotta käsittely on helpompaa.
    numero = str(numero)
    
    #Palauttaa nollan heti
    if numero == "0":
        return NumeraaliYkkoset[0]
    
    #Lukujen pilkkominen
    
    
    
    print(numerot)
    
    







    
if __name__ == "__main__":
    while True:
        i = input("Syötä numero: ")
        i = i.replace(" ","") #poistaa välit, matikkaa varten
        i = i.replace(",",".") #korvaa pilkun pisteellä, matikkaa varten
        try:
            print(MuutaNumeraaliksi(i))
            
            #print("Numeraalina: " + str(muunnaNumeraaliksi(i)))
            #print("--------------------")
        except ValueError:
            print("Error: syötetty arvo ei ole numero")
            print("--------------------")