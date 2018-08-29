import os
import re
lista=[]

def renomeia_arquivos():
    lista=os.listdir('C:/Users/vick_/Documents/Desenvolvimento/python/prank')
    for file in lista:
        novo_nome=re.sub("[0-9]","",file)

        old_file = os.path.join("C:/Users/vick_/Documents/Desenvolvimento/python/prank", file)
        new_file = os.path.join("C:/Users/vick_/Documents/Desenvolvimento/python/prank", novo_nome)
        os.rename(old_file, new_file)
    # tirar os numero
    # renomear

renomeia_arquivos()
