# ----- Rakenne Tiedosto ----- #
#Tehnyt: Aarni Junkkala

#Sisältää listoja suomen kielestä. Esim: aakkoset, vokaali, diftongit, äätämisryhmät, yms.
#Ei sisällä isoja kirjaimia, koska pythonissa on valmis funktio String.upper(), joka muuttaa isoksi.

numerot = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

aakkoset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
vokaalit = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
suomenkielisetVokaalit = ['a', 'e', 'i', 'o', 'u', 'y', 'ä', 'ö']
konsonantit = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
suomenkielisetKonsonantit = ['h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v'] #jätin "g" ja "d" kirjaimen pois vaikka kuuluisikin, koska on todella harvinaisia

## -------------------- Ääntäminen -------------------- ##
# -- Vokaali soinnut -- ##
etuVokaalit = ['ä', 'ö', 'y']
keskiVokaalit = ["i", "e"]    #Tälle uusinimi
takaVokaalit = ['a', 'o', 'u']

pyöreätVokaalit = ['o','ö','u','y']
laveatVokaalit = ['i','e','a','ä']
suppeatVokaalit = ['i','y','u']
puolisuppeatVokaalit = ['e','ö','o']
väljätVokaalit = ['ä','a']


#Ääntämisryhmät
dentaalisetKonsonantit = ['n', 's', 't', 'l', 'r'] #Näitä ääntäessä kieli koskee hampaisiin. epäilen s ja r
Klusiilit = ['p', 't', 'k', 'd', 'b', 'g']

puolivokaalit = ['v','j']

frikatiivit = ['s','h','f']

tremulantti = ['r']
lateraali = ['l']
likvidat = tremulantti + lateraali

palataalinasaali =['ng'] #Voi kusta paikkoja, koska en odottanut tarvitsevani kahta kirjainta määrittelyihin.
dentaalinasaali = ['n']
labiaalinasaali = ['m']
nasaalit = palataalinasaali + dentaalinasaali + labiaalinasaali

tenuisklusiilit = ["p", "t", "k"]
mediaklusiili = ['d', 'b', 'g']
klusiilit = tenuisklusiilit + mediaklusiili

Soinnilliset = vokaalit + nasaalit + likvidat + ["h"]
Soinnittomat = ['p', 't', 'k', 's']


## -------------------- Diftongit -------------------- ##
#diftongit, Vokaalit jotka voivat olla peräkkäin samassa tavussa
diftongit = ['ei', 'ai', 'oi', 'ui', 'äi', 'öi', 'yi',    'au', 'eu', 'iu', 'ou',     'äy', 'öy', 'iy', 'ey']
valjenevatdiftongit = ['ie',     'uo', 'yö'] #väljenevät diftongit ovat diftongeja, jos ne ovat ensimmäisessä tavussa. Esim: sie|ni  hy|gi|e|ni|a
#Konsonanttiyhtymät
kahdenKonsonantinYhtymat = ['lt', 'lk', 'lm', 'lp', 'lj', 'lv', 'ls', 'lh', 'rt', 'rk', 'rm', 'rp', 'rj', 'rv', 'rs', 'rh', 'rn', 'ht', 'hd', 'hk', 'hm', 'hj', 'hn', 'hv', 'hl', 'hr', 'st', 'sk', 'sp', 'sm','sn', 'sh', 'sv', 'ts', 'tk', 'tp', 'tj', 'tr', 'tv', 'th', 'ps', 'pr', 'pl', 'ks', 'kr', 'nk', 'nt', 'np', 'ns', 'nh', 'nj', 'mp', 'ms']
kolmenKonsonantinYhtymat = ['mpp', 'ntt', 'nss', 'nkk', 'lpp', 'ltt', 'lss', 'lkk', 'rpp', 'rtt', 'rss', 'rkk']

## -------------------- Erikoismerkit -------------------- ##
erikoismerkit = [' ', '-', "'", '.', ',', ':', ';', '?', '!', '…','(', ')', '[', ']', '{', '}', '⟨', '⟩', '|', '+', '-', '*', '/', '=', '≠', '≈', '<', '>', '≤', '≥', '(', ')', '[', ']', '{', '}', '×', '⋅', '÷', '%', '‰', '°', 'π'] #Kesken, täytä oleellisilla merkeillä
paatemerkit = ['.', ',', ':', ';', '?', '!', '…'] #päättää lauseen
sulkeet = ['(', ')', '[', ']', '{', '}', '⟨', '⟩']
matemaattisetSymbolit = ['+', '-', '*', '/', '=', '≠', '≈', '<', '>', '≤', '≥', '(', ')', '[', ']', '{', '}', '×', '⋅', '÷', '%', '‰', '°', 'π']