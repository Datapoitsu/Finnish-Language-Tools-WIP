## -------------------- Taivutus -------------------- ##
#Written by: Aarni Junkkala

# Ohjelma on kirjoitettu perustuen:
# https://fi.wiktionary.org/wiki/Liite:Suomen_sanojen_taivutustyypit
# Jokaiseen muodon kohdalle kirjoitettuna kuinka monta kappaletta kyseisen tyypin sanoja on sanakirjassa.

# Sijamuodot: 15kpl kertaa 2, koska monikko.


#Suomalaiset konsonantit on jaettu 51 eri luokkaan.
#Tavoitteenani on taivuttaa sana perusmuodosta kaikkiin päätteisiin.

#Vaikeuksia tulee muotojen 50 ja 51, jotka ovat yhdyssanoja.
#Vaikeutena sanojen erottaminen toisistaan.

#Helpointa aloittaa niiden sanatyyppien säännöistä, joita on vähemmän kuin muita.

## -- 1 -- #
#4128

#Vaikuttaa perusmuodolta.



## -- 2 -- #
#852



## -- 37 -- ##
def s37(sana):  
    #1
    #Esimerkki: vasen

    #Oletetaan säännön liittyvän sanan loppuun -sen
    print(37)

def s38(sana):
    #5692
    #Esimerkki:
    # sijamuoto yksikkö monikko
    
    # kieliopilliset sijamuodot
    # nominatiivi: nainen naiset         #Perusmuoto
    # genetiivi: naisen naisten          # -n
    #                   naisien          
    # partitiivi: naista naisia          # -a
    # akkusatiivi: nainen naiset         # Valinta liittyy puhtaasti verbiin. Fuck!
    #              naisen
    
    # sisäpaikallissijat
    # inessiivi: naisessa naisissa       # -ssa
    # elatiivi: naisesta naisista        # -sta
    # illatiivi: naiseen naisiin         # -en
    
    # ulkopaikallissijat
    # adessiivi: naisella naisilla       # -lla
    # ablatiivi: naiselta naisilta       # -lta
    # allatiivi: naiselle naisille       # -lle
    
    # muut sijamuodot
    # essiivi: naisena naisina           # -na
    #          (naisna)
    # translatiivi: naiseksi naisiksi    # -ksi
    # abessiivi: naisetta naisitta       # -tta
    # instruktiivi: – naisin             # -in
    # komitatiivi:  – naisine- + omistusliite  # -ine


    #Oletetaan säännön liittyvän sanan loppuun -nen
    print(38)






#Etsii ryhmän, johon substanttiivi kuuluu, perustuen sanan loppuun
def SubstanttiiviRyhma(sana):
    #37 -sen
    if sana[-3:] == "sen":
        s37(sana)
    if sana[-3:] == "nen":
        s38(sana)
SubstanttiiviRyhma("nainen")









