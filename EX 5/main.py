from os import getcwd, path

class Ajuda:
    def __init__(self, caminho: object) -> object:
        self.caminho = caminho

    def pegar_caminho(self):
        """"""
        base = getcwd()
        return path.join(base, self.caminho)

class Worker:
    def __init__(self):
        self.ajuda = Ajuda('db')

    def woker(self):
        print(f'caminho de trabalho {self.ajuda.pegar_caminho()}')
        return self.ajuda.pegar_caminho()

if(__name__ == '__main__'):
    print(Worker().woker())