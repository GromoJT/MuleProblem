import json
import random
import time
import math

#rozmiar tablicy z danymi
hmSize = 15

i=0
#tablica z danymi
HM = []
#tablica wartoci danych
HMV = []
#Procent szans na mutacje
HMCR = 70
MUT = 2
#czas przez jaki będzie działał program 
czas_dzialania = 5
#tymczasowe tablice do transferu danych
HM_temp = []
HMV_temp = []

#inicjacja tablic wartoci pobieranych z pliku jason
ids = []
nam = []
wei = []
siz = []
val = []
ris = []



#Wczytanie wartoći z pliku jason do korespondujących tablic
with open('wynik.json') as f:
    data = json.load(f)
for item in data['items']:
    ids.append(item['id'])
    nam.append(item['name'])
    wei.append(item['weight'])
    siz.append(item['size'])
    val.append(item['value'])
    ris.append(item['risk'])


#pętla która pocżatkowo zapełnia tablice danych przypadkowymi wynikami
while i < hmSize:
    #maksymalne kryterium do spełnienia 
    udzwig = 50.0
    gabaryt = 50.0

    #tymczasowe zmienne
    k_udz = 0.0
    k_gab = 0.0
    k_val = 0.0
    k_ryz = 0.0
    fin = 0.0
    
    #zmienna kontynuacji generowania
    dalej=True
    ilosc_prob = 100
    
    #inicjacja drugiego rzędu tablic pomocniczych
    ids2 = []
    nam2 = []
    wei2 = []
    siz2 = []
    val2 = []
    ris2 = []
    
    #generowanie losowego wyniku
    while dalej:
        #pobieranie losowego nr indeksu z puli 
        r = random.randint(0, len(ids)-1)
        if r in ids2:
            #jeli został wylosowany indeks już obecny na liscie to ponawiany jest process
            pass
        # sprawdzenie kryterium zgodnoci
        if(udzwig > wei[r]) and (gabaryt > siz[r]):
            #update kryterium zdolnosci
            udzwig = udzwig-wei[r]
            gabaryt = gabaryt-siz[r]
        
            #dopisanie elementu z jednej tablicy pomocniczej do drugiej 
            ids2.append(ids[r])
            nam2.append(nam[r])
            wei2.append(wei[r])
            siz2.append(siz[r])
            val2.append(val[r])
            ris2.append(ris[r])
            
            #obliczanie jakoci rozwiązania
            k_udz = k_udz + wei[r]
            k_gab = k_gab + siz[r]
            k_val = k_val + val[r]
            k_ryz = k_ryz + ris[r]
            
            try:
                fin = ((k_val/(k_ryz+(udzwig-k_udz)+(gabaryt-k_gab))))*100
            except ZeroDivisionError:
                fin = ((k_val/(k_ryz+(udzwig-k_udz)+(gabaryt-k_gab))))*100
            
            
            
            
        else:
            #przy nieudanej próbie licznik się zmniejsza
            ilosc_prob = ilosc_prob - 1
            
            if ilosc_prob < 1:
                #gdzy osiągnie 0 ta częć programu zostaje zakończona
                dalej = False
        
    #inkrementacja indeksu pętli 
    i = i+1
    
    #dodanie gotowych wynikóW do tablic
    HM.append(ids2)
    HMV.append(fin)
    HM_temp.append(ids2)
    HMV_temp.append(fin)

#Wydrukowanie gotowego zbioru rozwiązań
print(HMV)
#zmienna inicjująca koniec programu
koniec = False
dalej = True
#time stamp rozpoczęcia czsci optymilizacyjnej
program_start = time.time()

#pętla główna programu optymalizującego 
while koniec!=True:
    #pobranie czasu działąnia programu
    now = time.time()
   # print("teraz = "+ str(now-program_start))
    #sprawdzenie czy program nie powinien się już zakończyć 
    if(now - program_start > czas_dzialania):
        koniec = True
    
    #do dalszych pod iteracji już w tym miejscu resetowane są podstawowe zmienne
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
    
    #losowanie scieżki dalszego działania
    r_HMCR = random.randint(0,100)
    
    
    
    #pozycja decyzyjna czy program mutuje czy odwieża pulę 
    if(r_HMCR < HMCR):
        zamiana= True
        while zamiana:
           # print("pamiec")
           
            max_row_size = 0

            new_HM_entry_test = []
            
            
            #znajdowanie nadłuższego wiersza
            for i in range(len(HM)):
                if len(HM[i])>max_row_size:
                    max_row_size=len(HM[i])
                    
            #print("Najdłuższy ma = " + str(max_row_size))
            
            index_tab = [[ -1 for i in range(hmSize)] for j in range(max_row_size)]
        
            
            
           
            temp_index = 0
            
            
            for i in range(len(HM)):
                for y in range(len(HM[i])):
                    if(HM[i][y] is not None):    
                        if( HM[i][y]>-1):
                            index_tab[y][i] = HM[i][y]
                        else:
                            print("nie")
                    else:
                        print("nie")
                
                       
            #print(np.matrix(index_tab))
                        
            rand_length = random.randint(math.ceil(max_row_size/3), max_row_size)
            cur_pos = 0
            generowanie = True
            while generowanie:
                if cur_pos==rand_length:
                    generowanie = False
                    break
                else:
                    rc = random.choice(index_tab[cur_pos])
                    while(rc==-1):
                        rc = random.choice(index_tab[cur_pos])
                    new_HM_entry_test.append(rc)
                    cur_pos=cur_pos+1
            
            #print(new_HM_entry_test)
              
            temp_min = min(HMV)
           # print("min_hmv = " + str(temp_min))
            ind = HMV.index(temp_min)

            
            
            for i in new_HM_entry_test:
                #print(i)
                k_udz = k_udz + wei[i]
                k_gab = k_gab + siz[i]
                k_val = k_val + val[i]
                k_ryz = k_ryz + ris[i]
                
                try:
                    fin = ((k_val/(k_ryz+(udzwig-k_udz)+(gabaryt-k_gab))))*100
                except ZeroDivisionError:
                    fin = ((k_val/0.0001))*100
                
                if(fin==0):
                    break
            #print(k_udz)
            #print(k_gab)
            #print(fin)
            
            
            
            if(fin>temp_min and k_udz<50 and k_gab<50):
                HMV[ind] = fin
                HM[ind] = new_HM_entry_test
                print("+ Zamiana pamięć")
                zmiana = False
                dalej = False    
                #print("- * -")
            else:
                zmiana = False
               #print("- Brak zmiany pamięć")
            
            
            break
        
        
        
    
    else:
        kon = True
        #print("Siła")
        t_udzwig = 50.0
        t_gabaryt = 50.0
        while kon:
            r = random.randint(0, len(ids)-1)
            if r in ids2:
                pass
            if(t_udzwig > wei[r]) and (t_gabaryt > siz[r]):
                t_udzwig = t_udzwig-wei[r]
                t_gabaryt = t_gabaryt-siz[r]
            
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
                
                try:
                    fin = ((k_val/(k_ryz+(udzwig-k_udz)+(gabaryt-k_gab))))*100
                except ZeroDivisionError:
                    fin = ((k_val/0.0001))*100
                
                
            else:
                kon=False
                    
        temp_min = min(HMV)
        ind = HMV.index(temp_min)
        #print(ind)
        
        if(fin>HMV[ind]):
            HMV[ind] = fin
            HM[ind] = ids2
            #print("min_hmv = " + str(temp_min))
            #print(k_udz)
           # print(k_gab)
            #print(fin)
            print("+ Zamiana sila")
            dalej = False
            
        else:
            #print("- Brak zamiana sila")
            #print("sila jescze raz!")
            #continue
            #break
            dalej = False
    r_HMCR2 = random.randint(0, 100)
    if(r_HMCR2 < MUT):
        temp_HM_ev = []
        #print("MUTACJA!!!!")
        
        r3 = random.randint(0, len(HM)-1)
        r4 = random.choice(HM[r3])
        r6 = random.randint(0, len(HM[r3])-1)
        r5 = random.randint(0, len(ids)-1)
        temp_HM_ev = HM[r3]
        try:
            HM[r3][r6]=r5
        except IndexError:
            print(r4)
            HM[r3][r6%max_row_size]=r5
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
        
        for i in range(len(HM[r3])):
            nid = HM[r3][i]
            ids2.append(ids[nid])
            nam2.append(nam[nid])
            wei2.append(wei[nid])
            siz2.append(siz[nid])
            val2.append(val[nid])
            ris2.append(ris[nid])
            
            k_udz = k_udz + wei[r]
            k_gab = k_gab + siz[r]
            k_val = k_val + val[r]
            k_ryz = k_ryz + ris[r]
            
            try:
                fin = ((k_val/(k_ryz+(udzwig-k_udz)+(gabaryt-k_gab))))*100
            except ZeroDivisionError:
                fin = ((k_val/0.0001))*100
        if(fin>HMV[r3] and k_udz<50 and k_gab<50):
            HMV[r3] = fin
            print("Ewolucja!!!")
        else:
            HM[r3] = temp_HM_ev
            
            #print("Nagroda Darwina...")
        #print(fin)
print(HMV_temp)
print("- - - ")        
print(HM)  
print(" - ")   
print(HMV)

        
            
        
    
