from modelos.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, email, telefone, cargo, salario):
        super().__init__(nome, email, telefone)

        self.__cargo = cargo
        self.__salario = salario

    def get_cargo(self):
        return self.__cargo

    def get_salario(self):
        return self.__salario