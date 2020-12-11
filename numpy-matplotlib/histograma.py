import numpy as np #biblioteca necessária para leitura arquivo
import matplotlib.pyplot as plt #biblioteca necessária para histograma


#histograma com o valor_total exportado no phpmyadmin
dados = np.genfromtxt('valor_total.csv', delimiter='"')
histograma = plt.hist(dados, bins="scott")
#histograma = plt.hist(dados, bins=10)
plt.show()

#histograma do tempo_decorrido disponibilizado na descrição
dados = np.genfromtxt('tempo_decorrido.csv')
histograma = plt.hist(dados, bins="scott")
#histograma = plt.hist(dados, bins=4)
plt.show()
