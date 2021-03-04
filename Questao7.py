'''Escreva uma função que receba a idade do usuário e indique se ele pode ou não encher a
cara de cachaça'''
def idade(idade1):
    if idade1 >= 18:
        print("Pode encher a cara de cachaça")
    else:
        print("Nao pode encher a cara de cachaça")

idade1 = int(input("Digite sua idade "))
idade(idade1)
