from matplotlib import pyplot as plt
from collections import Counter

arquivo = open("veiculos.txt",'r')
listaLinhas = arquivo.readlines()

#criando classe veiculos com os atributos necessários para fazer a questão:
class Veiculo:
    def __init__(self,infos):
        listaInfo = infos.split() 		#ao criar uma lista de objetos, foi necessário fazer o 'split()'. Cada item desta lista é um atributo distinto
        self.tipo = listaInfo[0] 		#atributo 'tipo' é o primeiro item da lista retornada pelo 'split'
        self.modelo = listaInfo[2] 		#atributo 'modelo' é o terceiro item da lista retornada pelo 'split()'
        self.ano = listaInfo[5] 		#atributo 'ano' é o sexto item da lista retornada pelo 'split()'
        self.autonomia = listaInfo[4] 		#atributo 'autonomia' é o quinto item da lista retornada pelo 'split()'
        self.reservado = listaInfo[9] 		#atributo 'reservado' é o décimo item da lista retornada pelo 'split()'
    
listaVeiculos =[]
for n in range(1,len(listaLinhas)):
    listaVeiculos.append(Veiculo(listaLinhas[n])) #cria lista de objetos (veiculos) com os atributos da classe Veículo (tipo, modelo, ano, autonomia, reservado).

'''Descrição do passo acima: cada linha do documento 'veiculos.txt' vai ser recebida pela classe Veiculo, sofrerá o split(), ganhará os atributos da classe e será
adicionada a listaVeiculos'''

#letra a
def tipos():
    carros = 0 #iniciando contadores
    utes = 0
    vans = 0
    for vec in listaVeiculos:
        if vec.tipo == "carro":
            carros = carros + 1
        elif vec.tipo == "ute":
            utes = utes + 1
        elif vec.tipo == "van":
            vans = vans + 1

    tipos = ["carro","utilitário","van"] #listas que darão origem ao gráfico
    quantidade = [carros,utes,vans]
    
    plt.figure(1)
    plt.bar(tipos,quantidade)
    plt.ylabel("Quantidade")
    plt.title("Quantidades de cada tipo de veículo")

#letra b
def reservados():
    
    listaModelos =[]
    for vec in range(0,len(listaVeiculos)):
        if listaVeiculos[vec].reservado == "True": 		#se o veículo estiver reservado
            listaModelos.append(listaVeiculos[vec].modelo) 	#adiciona o modelo deste veículo (que é um objeto com atributos, dentre eles, o modelo) à lista de modelos
    dictModelos = Counter(listaModelos) 			#faz a contagem de quanto cada modelo aparece e retorna uma lista de dicionários. Em cada um, 
													#a chave é o modelo e o valor da chave é a frequencia
    
    
    modelos = dictModelos.keys() 				#pega as chaves (modelo) da lista do Counter e adiciona em uma lista separada
    quantidades = dictModelos.values() 			#pega os valores (frequencia com a qual cada modelo aparece) de cada chave e adiciona em outra lista separada
    #print(dictModelos)
    

    plt.figure(2)
    plt.bar(modelos,quantidades)
    plt.ylabel("Quantidade")
    plt.title("Quantidade de veículos reservados por modelo")

#Daqui para baixo, o código ainda não foi baixado (criado no bloco de notas por motivo de equipamento deficiente)

#letra c
def carros2017():
    listaAno = []
    for vec in range(0,len(listaVeiculos)):
        listaAno.append(listaVeiculos[vec].ano) 	#segue o mesmo raciocínio da função anterior (reservado())
    contagem = Counter(listaAno)
    anosOrd = sorted(contagem.items())
    dictAno = dict(anosOrd)
    anosFabricacao = dictAno.keys()
    quantidades = dictAno.values()
    
    plt.figure(3)
    plt.bar(anosFabricacao,quantidades)
    plt.ylabel("Quantidade de veículos")
    plt.title("Quantidade de veículos por ano de fabricação")

#letra d
def mediaAutonomiaPorAno():
    
    listaAno = []
    for vec in range(0,len(listaVeiculos)):
        listaAno.append(listaVeiculos[vec].ano)
    contagem = Counter(listaAno) 			#contagem de cada ano
    anosOrd = sorted(contagem.items())                                                
    dictAno = dict(anosOrd)
     
    anosFabricacao = dictAno.keys() 			#transforma as chaves (anos) em uma lista
     			
    autonomiaPorAno = []
    for ano in dictAno:
        somaAutonomia = 0
        media = 0
        
        for vec in range(0,len(listaVeiculos)):
            if ano == listaVeiculos[vec].ano:
                somaAutonomia = somaAutonomia + float(listaVeiculos[vec].autonomia)
        media = somaAutonomia/dictAno[ano]
        autonomiaPorAno.append(media)
        
    '''A ordenação do dicionário foi importante para organizar o gráfico por ordem crescente de anos de fabricação'''
    
    
    plt.figure(4)
    plt.bar(anosFabricacao,autonomiaPorAno)
    plt.ylabel("autonomia média (km/L)(?)")
    plt.title("Autonomia média por ano de fabricação")

tipos()
reservados()
carros2017()
mediaAutonomiaPorAno()
plt.show()

