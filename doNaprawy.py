import json
import random
import time

#rozmiar tablicy z danymi
hmSize = 15

i=0
#tablica z danymi
HM = []
#tablica wartoci danych
HMV = []
#Procent szans na mutacje
HMCR = 70
#czas przez jaki będzie działał program 
czas_dzialania = 0.001
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

#ilosć prób
p2 = 500000


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
            
            fin = (k_val / k_ryz)*100  
            
            
            
            
            
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
    print("teraz = "+ str(now-program_start))
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
    
    #losowanie cieżki dalszego działania
    r_HMCR = random.randint(0,100)
    
    #pozycja decyzyjna czy program mutuje czy odwieża pulę 
    if(r_HMCR < HMCR):
        print("pamiec")
        udzwig = 50.0
        gabaryt = 50.0
        max_row_size = 0S
        index_tab = []
        new_tap = []
        new_HM_entry_test = []
        
        for i in range(len(HM)):
            if len(HM[i])>max_row_size:
                max_row_size=len(HM[i])
                
        print("Najdłuższy ma = " + str(max_row_size))
        
        row_count = 0
        temp_index = 0
        
        for i in range(len(HM)):
            for y in range(max_row_size):
                if(y in range(len(HM[i]))):
                   S
                    temp_index=temp_index+1 
                else:
                   temp_index=temp_index+1 
            row_count=row_count+1
            
                   
            
                    

                    
                
        
    else:
        print("Siła")
        udzwig = 50.0
        gabaryt = 50.0
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
                break
                    
        temp_min = min(HMV)
        ind = HMV.index(temp_min)
        #print(ind)
        if(fin>HMV[ind]):
            HMV[ind] = fin
            HM[ind] = ids2
            print("zamiana sila")
            dalej = False
            
        else:
            print("brak zamiana sila")
            #print("sila jescze raz!")
            #continue
            #break
            dalej = False
        
print(HMV_temp)
print("- - - ")        
print(HM)  
print(" - ")   
print(HMV)
        
        
            
        
    
