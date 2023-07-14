class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return f'Funcionario, {self.nome}'
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def __str__(self):
        return f'Caelum, {self.nome}'
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def buscar_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando curso desse mês')


class Alura(Funcionario):
    def __str__(self):
        return f'Alura, {self.nome}'
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete')

    def buscar_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas do fórum')

# Classe Mixins
class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass


class Senior(Hipster, Alura, Caelum):
    pass


luan = Senior('Luan')
print(luan)

