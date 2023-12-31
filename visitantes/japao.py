import matplotlib.pyplot as plt
import numpy as np
import csv

visitantes = []


def carrega_dados():
    with open('Number of foreign visitors to Japan by month_ .csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            visitantes.append(linha)    # lista de dicionários


def titulo(texto, traco="-"):
    print()
    print(texto)
    print(traco*40)


def top_20():
    titulo("Top 20: Países com maior número de Visitantes")

    paises = []
    numeros = []

    for linha in visitantes:
        if linha['Country'] in paises:
            indice = paises.index(linha['Country'])
            numeros[indice] += int(linha['Visitor'])
        else:
            paises.append(linha['Country'])
            numeros.append(int(linha['Visitor']))

    # ordena as listas
    numeros2, paises2 = zip(*sorted(zip(numeros, paises), reverse=True))

    print("Nº País Estrangeiro........: Nº Visitantes")
    contador = 0

    for pais, num in zip(paises2, numeros2):
        contador += 1
        # uso do separador de milhares (_), substituindo-o por .
        print(f"{contador:2d} {pais:25} {num:_.0f}".replace("_", "."))
        if contador == 20:
            break


def compara2():
    titulo("Gráfico Comparando Visitantes Estrangeiros de 2 Países")

    pais1 = input("1º País: ").upper()
    pais2 = input("2º País: ").upper()

    anos = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']
    num1 = [0,       0,      0,      0,      0,      0,      0]
    num2 = [0,       0,      0,      0,      0,      0,      0]

    for linha in visitantes:
        if linha["Country"].upper() == pais1:
            indice = anos.index(linha['Year'])
            num1[indice] += int(linha['Visitor'])
        elif linha["Country"].upper() == pais2:
            indice = anos.index(linha['Year'])
            num2[indice] += int(linha['Visitor'])

    # create data
    x = np.arange(7)
    width = 0.4

    # plot data in grouped manner of bar type
    plt.bar(x-0.2, num1, width, color='red')
    plt.bar(x+0.2, num2, width, color='blue')
    plt.xticks(x, anos)
    plt.xlabel("Anos")
    plt.ylabel("Nº Visitantes")
    plt.legend([pais1, pais2])
    plt.show()


def compara3():
    titulo("Gráfico Comparando Visitantes Estrangeiros de 3 Países")

    pais1 = input("1º País: ").upper()
    pais2 = input("2º País: ").upper()
    pais3 = input("3º País: ").upper()

    anos = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']
    num1 = [0,       0,      0,      0,      0,      0,      0]
    num2 = [0,       0,      0,      0,      0,      0,      0]
    num3 = [0,       0,      0,      0,      0,      0,      0]

    for linha in visitantes:
        if linha["Country"].upper() == pais1:
            indice = anos.index(linha['Year'])
            num1[indice] += int(linha['Visitor'])
        elif linha["Country"].upper() == pais2:
            indice = anos.index(linha['Year'])
            num2[indice] += int(linha['Visitor'])
        elif linha["Country"].upper() == pais3:
            indice = anos.index(linha['Year'])
            num3[indice] += int(linha['Visitor'])

    # Criar figura e eixos
    fig, ax = plt.subplots()

    # Plotar os dados
    ax.plot(anos, num1, label=pais1)
    ax.plot(anos, num2, label=pais2)
    ax.plot(anos, num3, label=pais3)

    # Mostrar os rótulos dos eixos e a legenda do gráfico
    ax.set_xlabel('Ano')
    ax.set_ylabel('Nº de Visitantes')
    ax.legend()

    # Exibir o gráfico pronto
    plt.show()


def compara4():
    titulo("Gráfico Comparando Visitantes Estrangeiros de 4 Países")

    pais1 = input("1º País: ").upper()
    pais2 = input("2º País: ").upper()
    pais3 = input("3º País: ").upper()
    pais4 = input("4º País: ").upper()

    # poderia ser total1 = 0, total2 = 0...
    totais = [0, 0, 0, 0]

    for linha in visitantes:
        if linha["Country"].upper() == pais1:
            totais[0] += int(linha['Visitor'])
        elif linha["Country"].upper() == pais2:
            totais[1] += int(linha['Visitor'])
        elif linha["Country"].upper() == pais3:
            totais[2] += int(linha['Visitor'])
        elif linha["Country"].upper() == pais4:
            totais[3] += int(linha['Visitor'])
        
    # converte as strings em list
    paises = f"{pais1}_{pais2}_{pais3}_{pais4}".split("_")

    fig, ax = plt.subplots()
    ax.pie(totais, labels=paises, autopct="%.1f%%")

    plt.show()


# -------------------------------------- Programa Principal
carrega_dados()

while True:
    titulo("Visitantes Estrangeiros no Japão", "=")
    print("1. Top 20 Países com + Visitantes")
    print("2. Comparativo entre 2 países (gráfico de colunas)")
    print("3. Comparativo entre 3 países (gráfico de linhas)")
    print("4. Comparativo entre 4 países (gráfico de pizza")
    print("5. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top_20()
    elif opcao == 2:
        compara2()
    elif opcao == 3:
        compara3()
    elif opcao == 4:
        compara4()
    else:
        break
