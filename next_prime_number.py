'''
Sempre que o usúario quiser ver um numero primo
Esse vai precionar s, para ver o proximo
Caso não queira mais ver, vai precionar n

Funções a serem criadas:
1. Checa se um número é primo
2. Chama o  próximo numero até ser primo
3. Função principal if __name__ = '__main__'

. O valor do número primo começa com 2
. Os próximos valores serão a partir de 2
'''

def eh_primo(num):
    for n in range(2,int((num/2)+1)):
        if num!=n and num%n==0:
            return False
    return num

def proximo_primo(numero):
    numero+=1
    while not eh_primo(numero):
        numero+=1
    return numero
    
if __name__ == '__main__':
    primo = 2
    while True:
        entrada = input("Você deseja ver o próximo primo? (s/n)")
        if entrada == 's':
            primo=proximo_primo(primo)
            print(primo)       
        else:
            break
