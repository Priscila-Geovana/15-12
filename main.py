'''
1.	Suponha que você seja uma pessoa apaixonada por futebol e resolveu fazer um programa simples para acompanhar a Copa do Mundo do Catar. Seu programa funciona da seguinte maneira:
a.	[valor: 20 pontos] O sistema permite o cadastro de seleção que participou da Copa. Após cada inserção, o sistema pergunta ao usuário se ele deseja continuar inserindo dados ou se quer parar.
b.	[valor: 20 pontos] Os nomes das seleções são salvos em uma lista.
c.	[valor: 20 pontos] Quando o usuário encerra a inserção de seleções, o sistema deve perguntar se ele quer remover alguma seleção da lista. Caso afirmativo, o usuário deve informar o nome que deve ser retirado.
d.	[valor: 20 pontos] A lista deve ser gravada em um arquivo de texto (txt).
e.	[valor: 20 pontos] O seu código deve ser enviado para o GitHub e precisa ter, ao menos, um commit. Convide o usuário daniela.toda@ifro.edu.br para repositório.

Digite logo abaixo o código que você elaborou para resolver o item:

time = []
'''
time = []

while True:
  timeadc=input("deseja colocar um time? ")
  if timeadc == "sim":
    timenome=input('nome do time: ')
    time.append(timenome)
  else:
    break

print(time)

while True:
  timeremv = input("deseja deletar algum time? ")
  if timeremv == "sim":
    timenomeremv=input("qual deseja excluir? ")
    time.remove(timenomeremv)
  else:
    break

print(time)