#Muuttaa syötetyn lauseen sanoiksi listaan, poistaen erikoismerkit väleistä
import SuomiKieliKirjasto as kirjasto

#Esimerkki lause kokeiltavaksi: "Kissa, käveli? kuussa!", palauttaa: ['Kissa', 'käveli', 'kuussa']

def MuutaSanoiksi(lause):
    #Päätemerkit korvataan väli lyönneillä, jolloin sanat pysyvät eriteltyinä
    for i in range(len(kirjasto.paatemerkit)):
        lause = lause.replace(kirjasto.paatemerkit[i], " ")
    #Sulkeet poistetaan kokokaan, koska ne eivät ole osa sanaa
    for i in range(len(kirjasto.sulkeet)):
        lause = lause.replace(kirjasto.sulkeet[i], "")
    
    sanat = lause.split(" ")
    
    for i in range(sanat.count("")):
        sanat.remove("")
    return sanat

#Pyörittää funktiota toistuvasti, jos ei kutsuta ulkopuolelta
if __name__ == "__main__":
   while True:
    print(MuutaSanoiksi(input("Syötä lause, jonka haluat muuttaa sanoiksi: ")))
    print("--------------------")