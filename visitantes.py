import matplotlib.pyplot as plt
import numpy as np 
import csv

visitantes = []


def carrega_dados():
    with open('Number of foreign visitors to Japan by month_ .csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            visitantes.append(linha)


def titulo(msg, traco="-"):
    print()
    print(msg)
    print(traco*40)


def top20():
    pass

def compara2():
    titulo("Compara 2 países - Gráfico de Barras")

    pais1 = input("1º País: ").upper()
    pais2 = input("2º País: ").upper()

    anos = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']
    num1 = [   0,    0,    0,    0,    0,    0,    0]
    num2 = [   0,    0,    0,    0,    0,    0,    0]

    for linha in visitantes:
        if linha["Country"].upper() == pais1:
            indice = anos.index(linha["Year"])
            num1[indice] += int(linha['Visitor'])
        elif linha["Country"].upper() == pais2:
            indice = anos.index(linha["Year"])
            num2[indice] += int(linha['Visitor'])
      
    # create data 
    x = np.arange(7) 
    width = 0.4
    
    # plot data in grouped manner of bar type 
    plt.bar(x-0.2, num1, width, color='blue') 
    plt.bar(x+0.2, num2, width, color='red') 
    plt.xticks(x, anos) 
    plt.xlabel("Anos") 
    plt.ylabel("Nº Visitantes") 
    plt.legend([pais1, pais2]) 
    plt.show()    

def compara3():
    pass

def compara4():
    pass

# --------------------------------------- Programa Principal
carrega_dados()

while True:
    titulo("Número de Visitantes Estrangeiros do Japão", "=")
    print("1. Top 20 Países com + Visitantes")
    print("2. Compara 2 países (gráfico de barras)")
    print("3. Compara 3 países (gráfico de linhas)")
    print("4. Compara 4 países (gráfico de pizza)")
    print("5. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top20()
    elif opcao == 2:
        compara2()
    elif opcao == 3:
        compara3()
    elif opcao == 4:
        compara4()
    else:
        break
