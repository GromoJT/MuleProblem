import json
import random





hmSize = 15
i=0
HM = []
HMV = []
HMCR = 70

HM_temp = []
HMV_temp = []

ids = []
nam = []
wei = []
siz = []
val = []
ris = []

p2 = 500000

with open('wynik.json') as f:
    data = json.load(f)
for item in data['items']:
    ids.append(item['id'])
    nam.append(item['name'])
    wei.append(item['weight'])
    siz.append(item['size'])
    val.append(item['value'])
    ris.append(item['risk'])


while i < hmSize:
    udzwig = 50.0
    gabaryt = 50.0

    k_udz = 0.0
    k_gab = 0.0
    k_val = 0.0
    k_ryz = 0.0
    fin = 0.0
    
    dalej=True
    ilosc_prob = 100

    ids2 = []
    nam2 = []
    wei2 = []
    siz2 = []
    val2 = []
    ris2 = []
    
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
            
            fin = (k_val / k_ryz)*100
            
            
            
            
            
        else:
            ilosc_prob = ilosc_prob - 1
            
            if ilosc_prob < 1:
                dalej = False
        
    
    i = i+1
    
    HM.append(ids2)
    HMV.append(fin)
    HM_temp.append(ids2)
    HMV_temp.append(fin)

print(HMV)

koniec = False
dalej = True

while koniec!=True:
    
    udzwig = 50.0
    gabaryt = 50.0

    k_udz = 0.0
    k_gab = 0.0
    k_val = 0.0
    k_ryz = 0.0
    fin = 0.0
    
    ids2 = []
    nam2 = []
    wei2 = []
    siz2 = []
    val2 = []
    ris2 = []
    
    r_HMCR = random.randint(0,100)
    
    if(r_HMCR < HMCR):
        
        
    else:
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
                
                fin = (k_val / k_ryz)*100
                
                
            else:
                dalej = False
                    
        temp_min = min(HMV)
        ind = HMV.index(temp_min)
        print(ind)
        if(fin>HMV[ind]):
            HMV[ind] = fin
            HM[ind] = ids2
            koniec = True
            break
        else:
            continue
        
print(HMV)
        
        
            
        
    
