'''Escreva uma função que receba como argumento a quantidade de Km percorridos por um
carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. A
função deve retornar o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15
por km rodado.'''

km = int(input("Quantidade de km percorridos ? "))
qdias = int(input("Quantidade de dias o carro foi alugado ? "))

def aluguel(km,qdias):
    return km * 0.15 + qdias * 60

print("valor pago:",aluguel(km,qdias))


