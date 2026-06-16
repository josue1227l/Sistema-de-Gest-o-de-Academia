from modelos.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, email, telefone, matricula, plano):
        super().__init__(nome, email, telefone)

        self.__matricula = matricula
        self.__plano = plano

    def get_matricula(self):
        return self.__matricula

    def get_plano(self):
        return self.__plano