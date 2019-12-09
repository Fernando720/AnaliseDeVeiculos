from matplotlib import pyplot as plt
from collections import Counter

arquivo = open("veiculos.txt",'r')
listaLinhas = arquivo.readlines()

#criando classe veiculos com os atributos necessários para fazer a questão:
class Veiculo:
    def __init__(self,infos):
        listaInfo = infos.split()
        self.tipo = listaInfo[0]
        self.modelo = listaInfo[2]
        self.ano = listaInfo[5]
        self.autonomia = listaInfo[4]
        self.reservado = listaInfo[9]
    
listaVeiculos =[]
for n in range(1,len(listaLinhas)):
    listaVeiculos.append(Veiculo(listaLinhas[n]))

#quantidade de carros, vans e utilitários:
def tipos():
    carros = 0
    utes = 0
    vans = 0
    for vec in listaVeiculos:
        if vec.tipo == "carro":
            carros = carros + 1
        elif vec.tipo == "ute":
            utes = utes + 1
        elif vec.tipo == "van":
            vans = vans + 1

    tipos = ["carro","utilitário","van"]
    quantidade = [carros,utes,vans]
    
    plt.figure(1)
    plt.bar(tipos,quantidade)
    plt.ylabel("Quantidade")
    plt.title("Quantidades de cada tipo de veículo")

def reservados():
    
    listaModelos =[]
    for vec in range(1,len(listaVeiculos)):
        if listaVeiculos[vec].reservado == "True":
            listaModelos.append(listaVeiculos[vec].modelo)
    dictModelos = Counter(listaModelos)
    
    
    modelos = dictModelos.keys()
    quantidades = dictModelos.values()
    print(dictModelos)
    

    plt.figure(2)
    plt.bar(modelos,quantidades)
    plt.ylabel("Quantidade")
    plt.title("Quantidade de veículos reservados por modelo")
tipos()
reservados()
plt.show()

