# Infectados.py

![Comparação da projeção de Infectados](https://i.ibb.co/cFhb5Tp/git.png)

Você já se perguntou como anda a curva de crescimento de infectados em seu Pais em relação aos demais Paises?

OBS: Programa feito para estudo da linguagem, simula a projeção de dados por media ponderada.

Basicamente o programa busca a quantidades de dias do primeiro infectado em cada Pais e gera uma projecao por media ponderada comparando o crescimento diario de infectados em cada Pais

No exemplo da imagem, foi pego as datas da primeira infecção na Italia, que ocorreu no dia 31-01-2020 e do Brasil no dia 26-02-2020.
Pegou o numero de infectados que cresciam em cada dia em ambos os Paises.
Marcou o primeiro dia com o numero de infectados em cada Pais.
Fez a projeção por media ponderada do numero de infectados do Brasil para o numero de dias da Italia.

Programa que compara entre paises a taxa de crescimento de infectados, possui o objetivo de alertar e comparar a efetivação das medidas adotadas por diversos paises.

  - API da dados usando https://pomber.github.io/covid19/timeseries.json
  - Comparação entre dois paises
  - Necessário Python com as bibliotecas numpy e matplotlib

Para visualizar todos os paises que estão disponiveis:
  - python infectados.py

Para visualizar a comparação entre dois paises:
  - python infectados.py -ps1 Pais1 -ps2 Pais2
    
		
		
