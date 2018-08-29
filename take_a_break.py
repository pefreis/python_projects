import webbrowser
import time
from datetime import datetime



while True:
    print("Começando a contagem de jornada de trabalho as "+time.ctime())
    time.sleep(1800)
    url = "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
    webbrowser.open_new(url)
    resposta = input("Deseja iniciar um novo ciclo? Se sim, digite sim; se nao, digite nao.")
    if resposta=="sim":
    	continue
    elif resposta=="nao":
    	break
