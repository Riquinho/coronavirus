import urllib.request, json
import matplotlib.pyplot as plt
import numpy as np 

import argparse


response = urllib.request.urlopen('https://pomber.github.io/covid19/timeseries.json')
data = json.loads(response.read())

print('\n\nLista de Paises disponiveis: \n\n')
print(list(data.keys()))
print('\n\nPara gerar o grafico de comparacao execute: python infectados.py -ps1 pais1 -ps2 pais2 \n\n')

parser = argparse.ArgumentParser(description='Comparacao de crescimento de infectados')
parser.add_argument('--ps1','-ps1', help='Primeiro Pais')
parser.add_argument('--ps2','-ps2', help='Segundo Pais')
args = parser.parse_args()


def get_dados(pais1,pais2):
	dados_confirmed_ps1 = []
	dados_confirmed_ps2 = []
	menor_data = len(data[pais1]) -1 if len(data[pais1]) < len(data[pais2]) else len(data[pais2]) -1
	print('Menor data, será o inicio da contagem: ' + str(menor_data))
	while menor_data  > 0:
		
		#print(data[pais1][menor_data ])
		#print(number)
		confirmed_ps1 = data[pais1][menor_data]['confirmed']	 
		confirmed_ps2 = data[pais2][menor_data]['confirmed']
	 
		dados_confirmed_ps1.append(confirmed_ps1)
		dados_confirmed_ps2.append(confirmed_ps2)

		menor_data  = menor_data - 1

		#print('\n')


	dados_confirmed_ps1.reverse()
	dados_confirmed_ps2.reverse()
	
	print('\n Dados capturados: \n')
	print(dados_confirmed_ps1)
	print(dados_confirmed_ps2)
	print('\n')
	
	menor_data = len(data[pais1]) -1 if len(data[pais1]) < len(data[pais2]) else len(data[pais2]) -1
	print('dias: ' + str(menor_data))

	
	for i in list(range(menor_data)):
		try:
			dados_confirmed_ps1.remove(0)
		except:
			pass
		try:
			dados_confirmed_ps2.remove(0)
		except:
			pass
	
	print('\n Dados capturados(removendo zeros): \n')
	print(dados_confirmed_ps1)
	print(dados_confirmed_ps2)
	print('\n')
	

	faltantes_ps1 = menor_data - len(dados_confirmed_ps1)
	print('faltantes_ps1: ' + str(faltantes_ps1))

	faltantes_ps2 = menor_data - len(dados_confirmed_ps2)
	print('faltantes_ps2: ' + str(faltantes_ps2))


	for i in range(faltantes_ps1):
		num = np.average(dados_confirmed_ps1, weights  = list(range(len(dados_confirmed_ps1))))
		dados_confirmed_ps1.append(dados_confirmed_ps1[-1] + num)

	for i in range(faltantes_ps2):
		num = np.average(dados_confirmed_ps2,weights  = list(range(len(dados_confirmed_ps2))))
		dados_confirmed_ps2.append(dados_confirmed_ps2[-1] + num)

	print(dados_confirmed_ps1)
	print(dados_confirmed_ps2)
	
	print('\n')
	print('O programa pega o numero de dias de infectados em ambos os paises e projeta o crescimento dos infectados por dias em ambos os paises, caso algum pais tenha menos dias de registro, o calculo da projecao e realizado por media ponderada') 

	fig, ax = plt.subplots() 
	ax.plot(list(range(menor_data)) , dados_confirmed_ps1, label=str(pais1))
	ax.plot(list(range(menor_data)) , dados_confirmed_ps2, label=str(pais2))
	ax.set_title('Crescimento de infectados')
	ax.set_xlabel('Dias')
	ax.set_ylabel('Infectados')
	plt.legend(loc='best')
	plt.show()		



get_dados(args.ps1,args.ps2)