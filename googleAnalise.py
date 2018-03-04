import csv
from pre_processo.PreProcessamento import PreProcesso
from clustering.DBSCAN import Dbscan
dataPath ="dados/clash_royale.csv"
print('========= Buscando Dados Treino =============')
processador = PreProcesso()
clusterizador = Dbscan()

reviews = []
with open(dataPath, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        frase = processador.prePorcessar(row[1])
        #print (frase)
        reviews.append((frase,row[0],row[1],row[2],row[3]))
print('=========== DONE =============================')

print('=========== CLUSTERING ==========')
clusters = clusterizador.dbScan(reviews,0.3,2)
ind= 0
for cluster in clusters:
    print("cluster "+str(ind))
    for frase in cluster:
        print(frase)
    ind+=1