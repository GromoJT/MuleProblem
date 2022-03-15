import json
import random

ResultSize = 50000
GotowaLista = '{"items":[\n'
ids = []
rar = []
nam = []
wei = []
siz = []
val = []
ris = []

mod1id = []
mod1name = []
mod1Weight = []
mod1Size = []
mod1Value = []
mod1Risk = []


ids2 = []
rar2 = []
nam2 = []
wei2 = []
siz2 = []
val2 = []
ris2 = []

mod2id = []
mod2Rarity = []
mod2name = []
mod2Weight = []
mod2Size = []
mod2Value = []
mod2Risk = []

ids3 = []
rar3 = []
nam3 = []
wei3 = []
siz3 = []
val3 = []
ris3 = []

ids4 = []
rar4 = []
nam4 = []
wei4 = []
siz4 = []
val4 = []
ris4 = []

common = []
uncommon = []
rare = []
epic = []
legendary = []

m_id = []
m_normal = []
m_rare = []
m_epic = []
m_legendary = []

with open('baseItems.json') as f:
    data = json.load(f)
for item in data['baseItems']:
    ids.append(item['itemId'])
    rar.append(item['itemRarity'])
    nam.append(item['itemName'])
    wei.append(item['itemWeight'])
    siz.append(item['itemSize'])
    val.append(item['itemValue'])
    ris.append(item['itemRisk'])

with open('mod1.json') as f1:
    data1 = json.load(f1)
for mod in data1['mod1']:
    mod1id.append(mod['modId'])
    mod1name.append(mod['modName'])
    mod1Weight.append(mod['modWeight'])
    mod1Size.append(mod['modSize'])
    mod1Value.append(mod['modValue'])
    mod1Risk.append(mod['modRisk'])

with open('mod2.json') as f1:
    data1 = json.load(f1)
for mod in data1['mod2']:
    mod2id.append(mod['modId'])
    mod2Rarity.append(mod["modRarity"])
    mod2name.append(mod['modName'])
    mod2Weight.append(mod['modWeight'])
    mod2Size.append(mod['modSize'])
    mod2Value.append(mod['modValue'])
    mod2Risk.append(mod['modRisk'])

print(mod2Rarity)
mod2list_len = len(data1["mod2"])

items_len = len(data['baseItems'])

i=0
while i < mod2list_len:
    if mod2Rarity[i] == "legendary":
        m_legendary.append(mod2id[i])
    elif mod2Rarity[i] =="epic":
        m_epic.append(mod2id[i])
    elif mod2Rarity[i] =="rare":
        m_rare.append(mod2id[i])
    else:
        m_normal.append(mod2id[i])
    i = i + 1

print(m_legendary)

i=0
while i < items_len:
    if rar[i] == "legendary":
        legendary.append(ids[i])
    elif rar[i] =="epic":
        epic.append(ids[i])
    elif rar[i] =="rare":
        rare.append(ids[i])
    elif rar[i] =="uncommon":
        uncommon.append(ids[i])
    else:
        common.append(ids[i])
    i = i + 1


# print("Legendary = ",legendary)
# print("Epic = ",epic)
# print("Rare = ",rare)
# print("Uncommon = ",uncommon)
# print("Common = ",common)


i = 0
sedes = 0
while i < ResultSize:
    r = random.uniform(0.0,1.0)
    if r < 0.0005:
        sedes = sedes + 1
        r2 = random.choice(legendary)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    elif (r < 0.01 and r >= 0.0005):
        r2 = random.choice(epic)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    elif (r < 0.03 and r >= 0.01):
        r2 = random.choice(rare)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    elif (r < 0.15 and r >= 0.03):
        r2 = random.choice(uncommon)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    else:
        r2 = random.choice(common)
        ids2.append(i)
        nam2.append(nam[r2])
        wei2.append(round(wei[r2] * random.uniform(0.8, 1.2), 2))
        siz2.append(round(siz[r2] * random.uniform(0.8, 1.2), 2))
        val2.append(round(val[r2] * random.uniform(0.8, 1.2), 2))
        ris2.append(round(ris[r2] * random.uniform(0.8, 1.2), 2))
    i = i + 1


# print(sedes)
# print(ids2)
# print(nam2)
# print(wei2)
# print(siz2)
# print(val2)
# print(ris2)

# po wygenerowaniu bazowych itemów następuje teraz nadanie im pierwszego modyfikatora (w tym wypadku jakości oznaczonej podobnie co rzadkość)

i=0
while i < ResultSize:
    r = random.uniform(0.0,1.0)
    if r < 0.001:
        ids3.append(i)
        nam3.append(mod1name[4] + " "+ nam2[i])
        wei3.append(wei2[i])
        siz3.append(siz2[i])
        val3.append(round(val2[i] * mod1Value[4], 2))
        ris3.append(round(ris2[i] * mod1Risk[4], 2))
    elif (r < 0.01 and r >= 0.001):
        ids3.append(i)
        nam3.append(mod1name[3] + " " + nam2[i])
        wei3.append(wei2[i])
        siz3.append(siz2[i])
        val3.append(round(val2[i] * mod1Value[3], 2))
        ris3.append(round(ris2[i] * mod1Risk[3], 2))
    elif (r < 0.05 and r >= 0.01):
        ids3.append(i)
        nam3.append(mod1name[2] + " " + nam2[i])
        wei3.append(wei2[i])
        siz3.append(siz2[i])
        val3.append(round(val2[i] * mod1Value[2], 2))
        ris3.append(round(ris2[i] * mod1Risk[2], 2))
    elif (r < 0.15 and r >= 0.05):
        ids3.append(i)
        nam3.append(mod1name[1] + " " + nam2[i])
        wei3.append(wei2[i])
        siz3.append(siz2[i])
        val3.append(round(val2[i] * mod1Value[1], 2))
        ris3.append(round(ris2[i] * mod1Risk[1], 2))
    else:
        ids3.append(i)
        nam3.append(nam2[i])
        wei3.append(wei2[i])
        siz3.append(siz2[i])
        val3.append(round(val2[i] * mod1Value[0], 2))
        ris3.append(round(ris2[i] * mod1Risk[0], 2))
    i = i + 1

# print(ids3)
# print(nam3)
# print(wei3)
# print(siz3)
# print(val3)
# print(ris3)

# Teraz dodajemy mod2



i = 0
while i < ResultSize:
    r = random.uniform(0.0,1.0)
    if r < 0.0005:
        r2 = random.choice(m_legendary)
        ids4.append(i)
        nam4.append(mod2name[r2] +" "+ nam3[i])
        wei4.append(round(wei3[i] * mod2Weight[r2], 2))
        siz4.append(round(siz3[i] * mod2Size[r2], 2))
        val4.append(round(val3[i] * mod2Value[r2], 2))
        ris4.append(round(ris3[i] * mod2Risk[r2], 2))
    elif (r < 0.01 and r >= 0.0005):
        r2 = random.choice(m_epic)
        ids4.append(i)
        nam4.append(mod2name[r2] + " " + nam3[i])
        wei4.append(round(wei3[i] * mod2Weight[r2], 2))
        siz4.append(round(siz3[i] * mod2Size[r2], 2))
        val4.append(round(val3[i] * mod2Value[r2], 2))
        ris4.append(round(ris3[i] * mod2Risk[r2], 2))
    elif (r < 0.03 and r >= 0.01):
        r2 = random.choice(m_rare)
        ids4.append(i)
        nam4.append(mod2name[r2] + " " + nam3[i])
        wei4.append(round(wei3[i] * mod2Weight[r2], 2))
        siz4.append(round(siz3[i] * mod2Size[r2], 2))
        val4.append(round(val3[i] * mod2Value[r2], 2))
        ris4.append(round(ris3[i] * mod2Risk[r2], 2))
    else:
        r2 = random.uniform(0.0,1.0)
        if r2 <0.3:
            r2 = random.choice(m_normal)
            nam4.append(mod2name[r2] + " " + nam3[i])
            ids4.append(i)
            wei4.append(round(wei3[i] * mod2Weight[r2], 2))
            siz4.append(round(siz3[i] * mod2Size[r2], 2))
            val4.append(round(val3[i] * mod2Value[r2], 2))
            ris4.append(round(ris3[i] * mod2Risk[r2], 2))
        else:
            nam4.append(nam3[i])
            ids4.append(i)
            wei4.append(round(wei3[i] * 1.0, 2))
            siz4.append(round(siz3[i] * 1.0, 2))
            val4.append(round(val3[i] * 1.0, 2))
            ris4.append(round(ris3[i] * 1.0, 2))
    i = i + 1

# print(ids4)
# print(nam4)
# print(wei4)
# print(siz4)
# print(val4)
# print(ris4)

#GotowaLista = GotowaLista +"{'TEST':TEST}]}"

i = 0
while i < ResultSize-1:
    GotowaLista = GotowaLista+'{"id":'+str(ids4[i])+','+\
                  '"name":"'+nam4[i]+\
                  '","weight":'+str(wei4[i])+\
                  ',"size":'+str(siz4[i])+\
                  ',"value":'+str(val4[i])+\
                  ',"risk":'+str(ris4[i])+'},'
    i=i+1
GotowaLista = GotowaLista+'{"id":'+str(ids4[ResultSize-1])+\
              ',"name":"'+nam4[ResultSize-1]+\
              '","weight":'+str(wei4[ResultSize-1])+\
              ',"size":'+str(siz4[ResultSize-1])+\
              ',"value":'+str(val4[ResultSize-1])+\
              ',"risk":'+str(ris4[ResultSize-1])+'}]}'

print(GotowaLista)
print(type(GotowaLista))

wynik = json.loads(GotowaLista)
print(wynik)
print(type(wynik))

new_wynik = json.dumps(wynik,indent=4)
print(new_wynik)

with open('wynik.json', 'w') as f:
    json.dump(wynik, f,indent=4)




