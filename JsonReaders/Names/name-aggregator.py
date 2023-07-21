import os

nameFiles = os.listdir('./Names/NamesByYear/')

nameSet = set()

for nameFile in nameFiles:
    file = open('./Names/NamesByYear/'+ nameFile, mode='r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        (name, gender, count) = line.split(',')
        nameSet.add(name.lower())
with open('output.json','w') as f:
    for name in nameSet:
        f.write(name.upper() + '\n')