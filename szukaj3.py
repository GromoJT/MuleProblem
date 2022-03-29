import json
import random
import time


hmSize = 15
i=0
HM = []
HMV = []
HMCR = 70
czas_dzialania = 10

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
program_start = time.time()

while koniec!=True:
    now = time.time()
    if(now - program_start > czas_dzialania):
        koniec = True
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
        zamiana = True
        while zamiana:
            #print("Z pamięci")
            #print(str(HM[0][0]) + " = " + str(HMV[0]))
           # print(str(len(HM))+" = len of HM")
            i=0
            z=9999
            m=0
            while i < hmSize:
                print(str(len(HM[i]))+" = len of HM["+str(i)+"]")
                if len(HM[i]) < z:
                    z = len(HM[i])
                if len(HM[i]) > m:
                    m = len(HM[i])
                i=i+1
            print("m = "+str(m))
            print("z = "+str(z))
                
            r_len = random.randint(z, m)
            print(str(r_len))
            
            u=0
            p=0
            HMI_TEST = []
            while p < r_len:
                print(u)
                r_k = random.randint(0, hmSize-1)
                #print(str(r_k))
                if(HM[r_k][u]):
                    
                    HMI_TEST.append(HM[r_k][u])
                    p=p+1
                    if(u<14):
                        u=u+1
            #print(HMI_TEST)
            
            for i in HMI_TEST:
                #print(i)
                k_udz = k_udz + wei[i]
                k_gab = k_gab + siz[i]
                k_val = k_val + val[i]
                k_ryz = k_ryz + ris[i]
                
                fin = (k_val / k_ryz)*100
                
            #print(fin)
            #print(k_udz)
            #print (k_gab)
            if(udzwig > k_udz or gabaryt > k_gab):   
                temp_min = min(HMV)
                ind = HMV.index(temp_min)
                
                if(fin>HMV[ind]):
                    #print("zamiana")
                    HMV[ind] = fin
                    HM[ind] = ids2
                    zamiana = False
                    break
                else:
                    #print("Braki zamiany")
                    continue
            else:
                break
        
    else:
        print("Siła")
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
            break
        else:
            continue
        
print(HMV)
        
        
            
        
    
