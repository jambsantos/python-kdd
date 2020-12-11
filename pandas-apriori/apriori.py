#importa bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #biblioteca para análise de dados
from apyori import apriori #implementação do algoritmo apriori

#importa o arquivo csv
dados = pd.read_csv('pizzaria.csv', header=None) #comando para ler o arquivo csv
qtd = len(dados) #quantidade de registros

registros = [] #cria uma estrutura de lista chamada registros

#laço de repetição para adicionar os dados na lista de registros
for i in range(0, qtd): #laço de repetição de com intervalo de 0 a qtd-1
    registros.append([str(dados.values[i, j]) for j in range (0, 7)]) #adiciona na lista cada elemento de cada registro 
        
#criando regras de associação
#associacoes recebe a aplicação da função apriori sobre os registros, com o mínimo de suporte, confiança, lift e comprimento definidos    
associacoes = apriori(registros, min_support = 0.0053, min_confidence =0.20, min_lift=5, min_lenght=2 )
resultado_associacoes = list(associacoes) #transforma as associacoes em uma lista

resultado_final = []

#laço de repeticao de cada item de resultados
for item in resultado_associacoes:
    par = item[0] #recebe o item na posicao 0
    itens = [i for i in par] #itens recebe x para cada x no par
    
    value0 = str(itens[0]) #item 1
    value1 = str(itens[1]) #item 2
    value2 = str(item[1])[:7] #suporte fatiando na 7ºposição
    value3 = str(item[2][0][2])[:7] #confianca fatiando na 7º posição
    value4 = str(item[2][0][3])[:7] #lift fatiando na 7º posição
    
    linhas = (value0, value1, value2, value3, value4) #linha recebe os valores
    
    resultado_final.append(linhas) #adiciona no resultado final
    
    Label = ['Item 1', 'Item 2', 'Suporte', 'Confiança', 'Lift']
    
    #a cada iteração do laço, sugestão aumentará, pois a lista resultado_final ficará maior
    sugestao = pd.DataFrame.from_records(resultado_final, columns=Label) #constroi as tuplas
    
    print (sugestao)

