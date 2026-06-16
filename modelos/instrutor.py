from modelos.pessoa import Pessoa

class instrutor(Pessoa):
    def __init__(self, nome, email, telefone, cref, especialidade):
        super().__init__(nome, email, telefone)

        self.__cref = cref
        self.__especialidade = especialidade

    def get_cref(self):
        return self.__cref

    def get_especialidade(self):
        return self.__especialidade