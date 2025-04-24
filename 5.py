from amigo import Amigo
from dvd import DVD
from emprestimo import Emprestimo
from repositorio import Repositorio

# Criando instâncias
repo = Repositorio()

amigo1 = Amigo("Lucas", "11988887777", "lucas@email.com")
dvd1 = DVD("Matrix", "Um hacker descobre a verdade", "Wachowski", "Keanu Reeves", "Ação", 16)

# Registrando no repositório
repo.adicionar_amigo(amigo1)
repo.adicionar_dvd(dvd1)

# Criando e registrando um empréstimo
emprestimo1 = Emprestimo(dvd1, amigo1)
repo.registrar_emprestimo(emprestimo1)

# Listando os empréstimos
repo.listar_emprestimos()