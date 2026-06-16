class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_telefone(self):
        return self.__telefone