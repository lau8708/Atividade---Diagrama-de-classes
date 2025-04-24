class Repositorio:
    def _init_(self):
        self.amigos = []
        self.dvds = []
        self.emprestimos = []

    def adicionar_amigo(self, amigo):
        self.amigos.append(amigo)

    def adicionar_dvd(self, dvd):
        self.dvds.append(dvd)

    def registrar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listar_emprestimos(self):
        for emp in self.emprestimos:
            print(emp)
