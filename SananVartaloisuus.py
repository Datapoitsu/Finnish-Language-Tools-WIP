## -------------------- Sanan Vartaloisuus -------------------- ##
#Written by: Aarni Junkkala

import Tavuttaja
import SuomiKieliKirjasto as SKK

#nomini = substantiivi, adjektiivi, numeraali, pronomini
#Vartalo on siis se osa sananmuotoa, joka jää jäljelle kun taivutustunnukset erotetaan

#HUOM. Ei todellakaan ole vielä täydellinen!

#Done! (a). Vain vokaalivartaloisia ovat myös (a1)yksitavuiset sanat sekä sellaiset joiden vartalo päättyy (a2)diftongiin
#      (b). Sen sijaan kun vokaalivartalon lopussa on (b1) e tai (b2) VV, sana on yleensä kaksivartaloinen
#      (c)  poikkeuksena eA-nominit sekä lukumäärältään pienet ryhmät: verbin lukea tyyppiset tapaukset,
#           verbin lukea tyyppiset tapaukset (» § 72) sekä kivi‑, nalle- (» § 65) ja vapaa-tyyppien (» § 67) nominit (» § 64 asetelma 26).

#(a1) ei, moi, maa -> 1
#(a2) meditoi(-da), ->
#(b1) pyyhe, lomake -> 2
#(b2) tietää -> 2
#(c) nukke, kurre, pelle, toope, genre, joule -> 1


#(3) Yksikön nominatiivin lopussa on i mutta sanavartalossa on e ja sen edellä h, l, m, n, r, s tai t, esim.
# vuohi : vuohe+n : vuoh+ta
# tuli  : tule+n  : tul+ta
# lumi  : lume+n  : lun+ta
# sieni : siene+n : sien+tä
# saari : saare+n : saar+ta
# lapsi : lapse+n : las+ta
# susi  : sute+na : sut+ta

#Palauttaa vartaloisuuden
#talo -> 1
#nalle -> 2
#meditoi (-da) -> 1

def EtsiVartaloisuus(sana):
    #Pilkotaan sana tavuihin
    tavut = Tavuttaja.Tavuta(sana)
    
    #Yksi tavuiset sanat ovat aina yksivartaloisia
    if len(tavut) == 1:
        return 1
    
    #Jos sana päättyy diftongiin, niin se on yksivartaloinen
    if tavut[-1][-2:] in SKK.diftongit:
        return 1
    
    #Jos sana päättyy e, niin yleensä kaksivartaloinen (Selvitä esimerkki tapauksesta, jossa ei toteudu)
    if tavut[-1][-1] == "e":
        return 2
    
    #-li, -ni, -ri loppuiset sanat ovat kaksivartaloisia (esim. tuuli, huoli, pieni, ääni, saari, suuri)
    if tavut[-1][-1] == "i":
        if tavut[-1][-2] == "s" or tavut[-1][-2] == "n" or tavut[-1][-2] == "r":
    
    #Jos sana päättyy VV, niin yleensä kaksivartaloinen (Selvitä esimerkki tapauksesta, jossa ei toteudu)
    if len(tavut[-1]) >= 2:
        if tavut[-1][-2] in SKK.vokaalit and tavut[-1][-1] in SKK.vokaalit:
            return 2
    
    #Etsii tavujen määrän, jotka päättyvät vokaaliin. Esim. Talo -> 2, Pelto -> 1
    vokaalipääte = 0
    for i in range(len(tavut)):
        if tavut[i][-1] in SKK.vokaalit:
            vokaalipääte += 1
    
    #Jos kaikki tavut ovat vokaali päätteisiä, niin sana on yksivartaloinen
    if vokaalipääte == len(tavut):
        return 1

    return 2

print(EtsiVartaloisuus("marrie"))
print(EtsiVartaloisuus("kaataa"))
    