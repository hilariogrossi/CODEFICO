'''O Casamento de Padrões é um problema clássico em ciência da computação e é aplicado em áreas 
diversas como pesquisa genética, editoração de textos, buscas na internet, etc. Basicamente, ele 
consiste em encontrar as ocorrências de um padrão P de tamanho m em um texto T de tamanho n. 
Por exemplo, no texto T = “PROVA DE AEDSII” o padrão P = “OVA” é encontrado na posição 2 enquanto o 
padrão P = “OVO” não é encontrado. O algoritmo mais simples para o casamento de padrões é o 
algoritmo da “Força Bruta”, mostrado abaixo. Analise esse algoritmo e responda: Qual é a função de 
complexidade do número de comparações de caracteres utilizando a notação O e qual classe de 
complexidade esse algoritmo pertence'''

def forca_bruta(texto, padrao):
    n = len(texto)
    m = len(padrao)

    for i in range(n - m + 1):
        k = i
        j = 0

        while j < m and texto[k] == padrao[j]:
            j += 1
            k += 1

        if j == m:
            print("\nCasamento na posição", i, '\n')
            break


texto = "PROVA DE AEDSII"
padrao = "OVA"

forca_bruta(texto, padrao)
