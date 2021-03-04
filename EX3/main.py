from os import getcwd
from requests import get
from os import cpu_count
from platform import platform
URL = 'https://jsonplaceholder.typicode.com/posts'

def estouAqui():
    aqui = getcwd()
    # print(f'ESTOU {aqui}')
    return aqui

def algumasCoisa():
    processadores = cpu_count()
    sistema_opera = platform()
    return processadores, sistema_opera

class PegarDados:
    def consumir_dados(self): return get(URL)

if(__name__ == "__main__"):
    print(PegarDados().consumir_dados().json())
    print(estouAqui())
    print(algumasCoisa())
