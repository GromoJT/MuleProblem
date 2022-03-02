import json
import random

ids = []
rar = []
nam = []
wei = []
siz = []
val = []
ris = []

common = []
uncommon = []
rare = []
epic = []
legendary = []


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

items_len = len(data['baseItems'])
print(items_len)
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


print("Legendary = ",legendary)
print("Epic = ",epic)
print("Rare = ",rare)
print("Uncommon = ",uncommon)
print("Common = ",common)

for i in data['baseItems']:
    r = random.uniform(0.0,1.0)
    if r <0.001:
        pass
    elif (r < 0.03 and r >= 0.001):
        pass
    elif (r < 0.05 and r >= 0.03):
        pass
    elif (r < 0.2 and r >= 0.05):
        pass
    else:
        pass

