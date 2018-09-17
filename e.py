'''
Problema: encontrar n casas decimais de e
Passos: criar uma função para definir a precisão das casas decimais
'''

from math import e

def precision(valor,casas_decimais):
    return '%.*f' %(valor,casas_decimais)

if __name__ == '__main__':

    teste_valor = False

    while teste_valor == False:

        print("O número máximo de casas decimais é 50")
        decimais = int(input())
        if decimais <= 50:
            teste_valor = True

    print(precision(decimais,e))
    
    

