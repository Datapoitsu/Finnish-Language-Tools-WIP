# ----- Tavutesti ----- #
#Tehnyt: Aarni Junkkala

import Tavuttaja

kirjoita = False #Vaihda jos haluat kokeilla valmista sanasettiä

testattavat = ["", "VÄLJENTÄVÄT DIFTONGIT:", "sieni", "hygienia", "tuoli", "tie", "orjien",
               "", "TAVALLISET DIFTONGIT:", "taide", "peite", "toinen", "tuisku", "hyi", "täit", "töitä", "taulu", "teurastaa", "tiuskaista", "touhuta", "äyriäinen", "töykeä", "siistiytyä", "terveys",
               "", "ERIKOISIA:", "ekstra", "vaa'assa", "periaatteet", "kaaos", "kiuas",
               "", "ULKOMAAN SANOJA:", "klaava", "kraateri", "kraatteri", "stressi", "sprinkleri", "sprintteri", "halstrada", "demonstraatio",        
               "", "HAUSKOJA SANOJA:", "progressio", "priima", "altistua", "diftongi", "toistolause",  "substanssi"
               "elektroniikka", "kontradiktioita", "kiertokulkue", "paloauto", "uima-allas", "eroosio",  "reagoida",
               "Tieto- ja Viestintätekniikan perustutkinto", "yhdyssana", "Ranska", "Marui" ]

if kirjoita == False:
    for t in range(len(testattavat)):
        print(testattavat[t], Tavuttaja.TavutaLause(testattavat[t]))
else:
    while True: #infite repeat
        i = input("Syötä tavutettava sana: ")
        print(Tavuttaja.TavutaLause(i))
        print("--------------------")
