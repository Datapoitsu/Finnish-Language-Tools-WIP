# ----- Rakenne Tiedosto ----- #
#Sisältää listoja suomen kielestä. Esim: aakkoset, vokaali, diftongit, yms.

numerot = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

aakkoset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
vokaalit = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
suomenkielisetVokaalit = ['a', 'e', 'i', 'o', 'u', 'y', 'ä', 'ö']
konsonantit = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
suomenkielisetKonsonantit = ['h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v'] #jätin "g" kirjaimen pois vaikka kuuluisikin, koska on todella harvinainen

#Vokaali soinnut
etuVokaalit = ['ä', 'ö', 'y']
keskiVokaalit = ["i", "e"]
takaVokaalit = ['a', 'o', 'u']

#diftongit
diftongit = ['ai', 'ei', 'oi', 'ui', 'yi', 'äi', 'öi', 'au', 'eu', 'iu', 'ou', 'äy', 'öy', 'iy', 'ey']
valjenevatdiftongit = ['ie', 'uo', 'yö'] #väljenevät diftongit ovat diftongeja, jos ne ovat ensimmäisessä tavussa. Esim: sie|ni  hy|gi|e|ni|a

#Konsonanttiyhtymät
kahdenKonsonantinYhtymat = ['lt', 'lk', 'lm', 'lp', 'lj', 'lv', 'ls', 'lh', 'rt', 'rk', 'rm', 'rp', 'rj', 'rv', 'rs', 'rh', 'rn', 'ht', 'hd', 'hk', 'hm', 'hj', 'hn', 'hv', 'hl', 'hr', 'st', 'sk', 'sp', 'sm','sn', 'sh', 'sv', 'ts', 'tk', 'tp', 'tj', 'tr', 'tv', 'th', 'ps', 'pr', 'pl', 'ks', 'kr', 'nk', 'nt', 'np', 'ns', 'nh', 'nj', 'mp', 'ms']
kolmenKonsonantinYhtymat = ['mpp', 'ntt', 'nss', 'nkk', 'lpp', 'ltt', 'lss', 'lkk', 'rpp', 'rtt', 'rss', 'rkk']

#Erikoismerkit
erikoismerkit = [' ', '-', "'", '.', ',', ':', ';', '?', '!', '…','(', ')', '[', ']', '{', '}', '⟨', '⟩', '|', '+', '-', '*', '/', '=', '≠', '≈', '<', '>', '≤', '≥', '(', ')', '[', ']', '{', '}', '×', '⋅', '÷', '%', '‰', '°', 'π'] #Kesken, täytä oleellisilla merkeillä
paatemerkit = ['.', ',', ':', ';', '?', '!', '…'] #päättää lauseen
sulkeet = ['(', ')', '[', ']', '{', '}', '⟨', '⟩']
matemaattisetSymbolit = ['+', '-', '*', '/', '=', '≠', '≈', '<', '>', '≤', '≥', '(', ')', '[', ']', '{', '}', '×', '⋅', '÷', '%', '‰', '°', 'π']