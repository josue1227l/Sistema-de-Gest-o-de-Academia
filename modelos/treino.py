class Treino:
    def __init__(self, nome, objetivo):
        self.nome = nome
        self.objetivo = objetivo
        self.exercicios = []

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)