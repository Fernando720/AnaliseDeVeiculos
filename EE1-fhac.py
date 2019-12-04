''' analisando arquivo veículos.txt com lista de carros/vans '''

arquivo = open('veiculos.txt','r')

listaLinhas = arquivo.readlines()
#quantos veículos cadastrados?
cadastrados = len(listaLinhas)-1
print("veículos cadastrados: ",cadastrados)

#quantos veículos disponíveis?
disponiveis = 0
for n in range(1,len(listaLinhas)):
    
    if "False" in listaLinhas[n]:
        disponiveis = disponiveis + 1
    
print("veículos disponíveis: ",disponiveis)

#quantos carros Corollas disponíveis?
corolla = 0
for n in range(1,len(listaLinhas)):
    
    if "Corolla" in listaLinhas[n]:
        corolla = corolla + 1
    
print("veículos corolla: ",corolla)

#quantos carros de 2017?

ano = 0
for n in range(1,len(listaLinhas)):
    
    if "2017" and "carro" in listaLinhas[n]:
        ano =  ano + 1
    
print("veículos de 2017: ",ano)

#quantos veículos não têm a placa iniciada com a letra 'P'?

i=1
linhaLista = []
placa = 0
while i<len(listaLinhas):
    linhaLista = listaLinhas[i].split("\t")
    if linhaLista[6][0] == "P":
        placa = placa + 1
    i=i+1
print("carros com placa iniciada com a placa 'P': ",placa)
