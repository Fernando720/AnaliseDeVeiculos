from matplotlib import pyplot as plt


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
    

def reservados():
    corolla = 0
    prisma = 0
    listaModelos =["Uno", ]
    for vec in listaVeiculos:
        
        if vec.modelo != listaModelos:
            listaModelos.append(vec.modelo)
    
    
    print(listaModelo)        

    modelos = ["Corolla","Prisma"]
    reservados = [corolla,prisma]

    #plt.figure(2)
    #plt.bar(modelos,reservados)
    

tipos()
reservados()
#plt.show()

