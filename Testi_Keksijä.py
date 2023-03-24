# ----- Keksi testi ----- #
#Written by: Aarni Junkkala
#Keksii monta sanaa ja langdetectin kanssa etsii prosentti luvun sana keksijälle

from time import process_time
import SanaKeksija as keksija
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0
from progress.bar import Bar

class KeksitytSanat:
  def __init__(self, sana):
    self.sana = sana
    self.kieli = detect(sana)

class KeksitytKielet:
    def __init__(self, kieli):
        self.kieli = kieli
    pros = 0 #kuinka monta prosenttia sanoista on tätä kieltä.

KeksittavienSanojenMaara = 2000 #kestää noin 10sec, aseta isompi luku jos haluat tarkempaa dataa.

print("Sample size: " + str(KeksittavienSanojenMaara))
print("Sanojen keksintä aloitettu")
tic = process_time() 

Arvaukset = []

with Bar('Prosessoi sanojen keksintää', max=KeksittavienSanojenMaara) as bar:
    # Sanan luonti #
    for i in range(KeksittavienSanojenMaara):
        a = keksija.Keksi()
        Arvaukset.append(KeksitytSanat(a))
        bar.next()

# -- Jälkitoimenpiteet -- #
Kielet = [] #Lista uniikeista kielistä
kieliholder = [] #Tähän listaan tulee jokainen löydetty kieli kerran.
# Etsii kaikki kielet #
for i in range(len(Arvaukset)):
    kieliholder.append(Arvaukset[i].kieli)
kieliholder = list(dict.fromkeys(kieliholder)) #Karsii ylimmääreiset pois.

#Tekee jokaisesta kielestä luokan
for k in range(len(kieliholder)):
    Kielet.append(KeksitytKielet(kieliholder[k]))

#Laskee prosentit jokaiselle kielelle
for k in range(len(Kielet)):
    samoja = 0
    for i in range(len(Arvaukset)):
        if Kielet[k].kieli == Arvaukset[i].kieli:
            samoja += 1
    Kielet[k].pros = round(samoja / len(Arvaukset), 3) * 100

#Järjestää prosentin mukaan
def myFunc(e):
  return e.pros
Kielet.sort(reverse=True,key=myFunc)

TulostaKaikki = False #Vaihda jos haluat kaikki prosentit tulostetuksi
if TulostaKaikki == True:
    for i in range(len(Kielet)):
        print(Kielet[i].kieli + " " + str(Kielet[i].pros) + "%")
else:    
    for i in range(5):
        print(Kielet[i].kieli + " " + str(Kielet[i].pros) + "%")

toc = process_time()
print("Aika: " + str(toc - tic))