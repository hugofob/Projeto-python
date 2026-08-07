'''from diag_classe import *
from rich import inspect

def main():
    a1 = Aluno("Hugo", 1987, "SI")
    inspect(a1, private=True, methods=True)


if __name__ == '__main__':
    main()'''

from diag_classe import *
from rich import inspect

def main():
    a = Aluno("Hugo", 1987, "SIS")
    b = Aluno("Amanda", 1995, "FISIO")
    a.add_curso("POR")
    a.add_curso("MATEM")
    print(a.cursos_oficiais)
    print(a.__dict__)

if __name__ == '__main__':
    main()