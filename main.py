'''
Desafio 9 - Removendo valores.

Para este desafio , vamos começar com a lista anterior "Frutas" do desafio anterior

Vamos remover a "manga" da lista usando o método remove()
Depois vamos remover o ultimo elemento com o comando del

e por fim imprimir o valor da lista.

'''

#Lista

frutas = ['maça', 'banana', 'manga','uva','abacaxi']

#Acessando para encontrar o index banana.
frutas.remove('manga')
del frutas[-1]

#saida
print(frutas)
