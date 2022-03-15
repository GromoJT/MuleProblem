import json
import random
import math

udzwig = 150.0
gabaryt = 150.0

ids = []
nam = []
wei = []
siz = []
val = []
ris = []

ids2 = []
nam2 = []
wei2 = []
siz2 = []
val2 = []
ris2 = []

with open('wynik.json') as f:
    data = json.load(f)
for item in data['items']:
    ids.append(item['id'])
    nam.append(item['name'])
    wei.append(item['weight'])
    siz.append(item['size'])
    val.append(item['value'])
    ris.append(item['risk'])

#print(ids)
#print(nam)
#print(wei)
#print(siz)
#print(val)
#print(ris)
#print(len(ids))

dalej=True
ilosc_prob = 10000

k_udz = 0.0
k_gab = 0.0
k_val = 0.0
k_ryz = 0.0
fin = 0.0

while dalej:
    r = random.randint(0, len(ids)-1)
    if r in ids2:
        pass
    if(udzwig > wei[r]) and (gabaryt > siz[r]):
        udzwig = udzwig-wei[r]
        gabaryt = gabaryt-siz[r]
    
        ids2.append(ids[r])
        nam2.append(nam[r])
        wei2.append(wei[r])
        siz2.append(siz[r])
        val2.append(val[r])
        ris2.append(ris[r])
        
        k_udz = k_udz + wei[r]
        k_gab = k_gab + siz[r]
        k_val = k_val + val[r]
        k_ryz = k_ryz + ris[r]
        
    else:
        ilosc_prob = ilosc_prob - 1
        
        if ilosc_prob < 1:
            dalej = False




fin = k_val / k_ryz
print(k_udz)
print(k_gab)
print(k_val)
print(k_ryz)
print(fin)

print(ids2)