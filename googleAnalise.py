import csv
from pre_processo.PreProcessamento import PreProcesso
dataPath ="dados/clash_royale.csv"
print('========= Buscando Dados Treino =============')
p = PreProcesso()
reviews = []
with open(dataPath, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        frase = p.prePorcessar(row[1])
        #print (frase)
        reviews.append((frase,row[0],row[1],row[2],row[3]))
print('=========== DONE =============================')
