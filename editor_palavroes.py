from urllib import request

def lendo_arquivo():
    arquivo = 'texto.txt'
    lugar = open('C:/Users/vick_/OneDrive/Documents/GitHub/python_projects/'+arquivo, 'r')
    texto = lugar.read()
    print(texto)
    lugar.close()
    checa_palavrao(texto)

def checa_palavrao(algo):
    conexao  = request.urlopen("http://www.wdylike.appspot.com/?q="+algo,None)
    output = conexao.read()
    print(output)
    conexao.close()
    if "true" in output:
        print("Opa, tem palavrão")
    elif "false" in output:
        print("Ufa, esse texto não tem palavrão")
    else:
        print("Não foi possível verificar")
lendo_arquivo()            
            
        
