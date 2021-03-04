'''Um fazendeiro cria Galinhas, Vacas e Porcos. Escreva uma função que receba a quantidade
de cada animal que o fazendeiro possui atualmente e retorne quantas patas tem na fazenda.'''

vacas = int(input("Quantas vacas possui na fazenda ? "))
galinhas = int(input("Quantas galinhas possui na fazenda ? "))
porcos = int(input("Quantos porcos possui na fazenda ? "))

def result(vacas,galinhas,porcos):
    return vacas * 4 + galinhas * 2 + porcos * 4

print("Na fazenda possui",result(vacas,galinhas,porcos),"patas")
    
    
