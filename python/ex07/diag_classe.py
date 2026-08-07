'''from abc import ABC
from datetime import date
from rich import print

class Pessoa(ABC):

    hoje = date.today()

    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def idade(self):
        idade = self.hoje.year - self._nascimento.year

        if (self.hoje.month, self.hoje.day) < (self._nascimento.month, self._nascimento.day):
            idade -= 1

        return idade

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, valor):
        if valor >= self.hoje:
            raise ValueError("[red]Data informada inválida!!![/]")

        idade = self.hoje.year - valor.year

        if (self.hoje.month, self.hoje.day) < (valor.month, valor.day):
            idade -= 1

        if idade > 60:
            raise ValueError("[red]Já ultrapassou a idade de cursar nossos cursos![/]")

        self._nascimento = valor

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self._curso = curso
        self.curso_oficiais = ['ADM', 'SI','CONT','INGLÊS','MATEMÁTICA']

    def add_curso(self, curso): # adiciona um novo curso a lista
        if isinstance(curso, str) and len(curso) > 0:  # se a mensagem e uma instância de texto e tamanho de texto for maior que zero
            self.curso_oficiais.append(curso.strip())

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, valor):
        if valor in self.curso_oficiais:
            self._curso = valor
        else:
            raise ValueError("[red]Curso inválido[/]")'''

from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nascimento:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"O ano {ano} é inválido.")

    @property
    def idade(self):
        return date.today().year - self.nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionErrorError("Você não pode alterar a idade, mude o ano de nascimento.")

class Aluno(Pessoa):

    cursos_oficiais = ["SIS", "ADM", "FISIO", "MATEM"]

    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None
        self._curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise PermissionError(f"O curso {curso} não está na lista de cursos oficiais.")

    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        if 3 <= len(curso) <= 5:
            Aluno.cursos_oficiais.append(curso)# se o curso tiver mais de 3 letras e menos ou igual a 5 adiciona o curso na lista cursos oficiais

        if curso in Aluno.cursos_oficiais:
            raise ValueError(f"O curso {curso} já existe na lista de cursos oficiais.")
        else:
            raise ValueError(f"O curso {curso} está fora dos padrões oficiais do curso.")

