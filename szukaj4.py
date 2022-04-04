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
czas_dzialania = 10

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
            
            fin = (k_val / k_ryz)*100  - (gabaryt*udzwig*10)
            
            
            
            
            
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
        #ustawienie flagi mutacji tablicy 
        zamiana = True
        while zamiana:
            #print("Z pamięci")
            #print(str(HM[0][0]) + " = " + str(HMV[0]))
           # print(str(len(HM))+" = len of HM")
           
            #ustawienie zmiennych do wyszukania optymalnego rozmiaru nowego rozwiazania
            #--Jako że rozwiążania tworzone w poprzednim segmęcie niezawsze są jednakowej
            #-- długoci. To należy znaleźć pewne rozwiażanie tego problemu.
            #-- Ustawienie aby nowe rozwiazanie które skłąda się z już istniejących musiało być
            #-- tak samo długie jak najmniejsze czy największe. Spowodowało by trudnoć z znalezieniem
            #-- w puli optymalnych kombinacji.
            #-- Dlatego postawilimy na lepy traf i długoć tego rozwiażania jest ograniczana 
            #-- do wartoći pomiędzy tymi dwiema skrajnymi
            i=0
            z=9999
            m=0
            whm = []
            indexes = []
            
            while i < hmSize:
                #print(str(len(HM[i]))+" = len of HM["+str(i)+"]")
                if len(HM[i]) < z:
                    z = len(HM[i])
                if len(HM[i]) > m:
                    m = len(HM[i])
                whm.append(len(HM[i]))
                i=i+1
            # m = maksymalna długoć
            # z = minimalna długoć
            
            print("m = "+str(m))
            print("z = "+str(z))
                
            r_len = random.randint(z, m)
            for i in range(r_len):
                indexes.append(i)
            #r_len to długoć pomiędzy tymi skrajnymi
            print(str(r_len))
            print(indexes)
            
            #problematyczny moment generowania rozwiazania z pamięci 
            #ustawnianie zmiennych
            u=0
            p=0
            i=0
            HMI_TEST = []
            #pętla generowania nowego wyniku o ustalonej długoci z okrelonej choć zmiennej puli
            generowanie = True
            while generowanie:
            
                try:
                    r_k = random.choice(indexes)
                except IndexError:
                    generowanie = False
                try:
                    print("HM["+ str(p%len(HM))+"][" + str(r_k) +"] = "+ str(HM[p%len(HM)][r_k]))
                    if(HM[p%len(HM)][r_k] in HMI_TEST ):
                        print("POWTÓRKA 1 ")
                        break
                    else:
                        HMI_TEST.append(HM[p%len(HM)][r_k])
                        indexes.remove(r_k)
                except IndexError:
                    print("Error - procedura wyjątkowa")
                    try:
                        doskutku = True
                        while doskutku:
                            nr = random.randint(0,r_len)
                            print("HM["+ str(p%len(HM))+"][" + str(nr) +"] = "+ str(HM[p%len(HM)][nr]))
                            if(HM[p%len(HM)][nr] in HMI_TEST):
                                print("POWTÓRKA 2 ")
                                p=p+1
                                break
                            else:
                                HMI_TEST.append(HM[p%len(HM)][nr])
                                
                                try:
                                    indexes.remove(r_k)
                                except ValueError:
                                    indexes.pop()
                                doskutku = False
                    except IndexError:
                        continue
                    continue
                p=p+1
                if(len(indexes)==0):
                    print("Udało się!")
                    generowanie = False
            print("test")
            print(HMI_TEST)
            
            
            for i in HMI_TEST:
                #print(i)
                k_udz = k_udz + wei[i]
                k_gab = k_gab + siz[i]
                k_val = k_val + val[i]
                k_ryz = k_ryz + ris[i]
                
                fin = (k_val / k_ryz)*100  - ((udzwig-k_udz)*(gabaryt-k_gab)*10)

            if(udzwig < k_udz or gabaryt <  k_gab):   
                temp_min = min(HMV)
                ind = HMV.index(temp_min)
                
                if(fin>HMV[ind]):
                    print("zamiana")
                    HMV[ind] = fin
                    HM[ind] = HMI_TEST
                    zamiana = False
                    break
                else:
                    print("Braki zamiany")
                    break
            else:
                print("Braki zamiany")
                break
            
            
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
            
        else:
            continue
        
print(HMV_temp)
print("- - - ")        
print(HM)  
print(" - ")   
print(HMV)
        
        
            
        
    
