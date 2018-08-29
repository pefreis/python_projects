import random

#Objeto que define métodos e atributos específicos de um jogador
#O Dealer é considerado um jogador
class Jogador(object):
    numlista = random.randint(0,3)
    numcarta = random.randint(0,12)

    def __init__(self, jogador_nome, jogador_soma=0):
        self.jogador_nome=jogador_nome
        self.jogador_soma=jogador_soma
    
    #Metodo de comprar carta
    def nova_carta(self):
        
        #nesse caso sorteamos nova carta do baralho
        while True:
            Jogador.numlista = random.randint(0,3)
            Jogador.numcarta = random.randint(0,12)
            carta = baralho[Jogador.numlista][Jogador.numcarta]    
            if carta != None:
                baralho[Jogador.numlista][Jogador.numcarta] = None
                break
                
        #definindo os naipes 
        if Jogador.numlista==0:
            naipe="copas"
        elif Jogador.numlista==1:
            naipe="paus"
        elif Jogador.numlista==2:
            naipe="ouros"
        else:
            naipe="espadas"
            
        #definindo nome das cartas especiais
        if carta==11:
            carta="Valete"
        elif carta==12:
            carta="Dama"
        elif carta==13:
            carta="Rei"
        elif carta==1:
            carta="Ás"
        
        
        #printamos a carta sorteada e transformamos em valor
        print("A carta sorteada para %s foi um %s de %s." %(self.jogador_nome,(carta),naipe.upper()))    
        if carta=="Ás":
            self.jogador_soma += 11
            if self.jogador_soma>21:
                self.jogador_soma-=10
        elif isinstance(carta,str):
            self.jogador_soma += 10
        else: 
            self.jogador_soma += carta
        return self.jogador_soma

#Função para avaliar o ganhador: dealer ou jogador
def avaliar_ganhador(jogador_soma, dealer_soma):
    print("SOMA DE CARTAS NA MÃO: %r" %(jogador.jogador_soma))
    print("SOMA DE CARTAS DO DEALER: %r" %(dealer.jogador_soma))
    if jogador_soma>dealer_soma:
        print("Parabéns, você ganhou!")
    elif jogador_soma<=dealer_soma:
        print("Puxa, você perdeu!")



#definimos o baralho
baralho=[[i for i in range(1,13+1)],[i for i in range(1,13+1)],[i for i in range(1,13+1)],[i for i in range(1,13+1)]]

#Começando o jogo, imprimindo instruções
print("Bem vindo ao jogo!")
nome = str(input("Digite o seu nome para começarmos: "))
jogador=Jogador(nome)



#Printamos a carta inicial do Dealer
print("\n------------------")
print("DEALER: Carta inicial")
dealer=Jogador("o dealer")
dealer.nova_carta()
contador_dealer=1
print("------------------\n")


#Printamos as cartas iniciais do jogador
print("\n------------------")
print("%s: Cartas iniciais"%(jogador.jogador_nome))
i=0
while i<2:
    jogador.nova_carta()
    i=i+1
print("SOMA DE CARTAS NA MÃO: %r" %(jogador.jogador_soma))
print("------------------\n")

#Verificamos soma de jogador
while jogador.jogador_soma<21:
    try:
        comando=str(input("\nPARA COMPRAR CARTA DIGITE: 'comprar' || PARA PASSAR A VEZ DIGITE: 'passar'\n"))
        if comando=='comprar':
            jogador.nova_carta()
            print("\n")
            print("SOMA DE CARTAS NA MÃO: %r" %(jogador.jogador_soma))
        elif comando=='passar':
            print("Estou satisfeito! Sua vez.")
            break
    except:
        print("Entrada inválida")

#verificamos se o jogador estourou a soma
if jogador.jogador_soma>21:
    print("Puxa, você perdeu!") 
    
#se nao estourou o dealer vai jogar
else:
    while dealer.jogador_soma<=17 or contador_dealer<5:
        dealer.nova_carta()
        contador_dealer+=1
        if dealer.jogador_soma>21:
            print("SOMA DE CARTAS DO DEALER: %r" %(dealer.jogador_soma))
            print("Parabéns, você ganhou!")
            break
        elif dealer.jogador_soma>17:
            avaliar_ganhador(jogador.jogador_soma,dealer.jogador_soma)