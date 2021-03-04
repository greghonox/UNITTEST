from re import findall
from requests import get

URL = 'https://api.genderize.io?name='

def pegar_primeiroNome(nome):  return findall('\w*', nome)[0]

def pegar_sexo(nome):
    cn = get(URL + pegar_primeiroNome(nome))
    sexo = cn.json() if(cn.status_code == 200) else 'NAO RECONHECIDO'
    return sexo

if __name__ == '__main__':
    print(pegar_sexo('Gregorio Honorato'))
