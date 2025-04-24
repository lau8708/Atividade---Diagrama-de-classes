from datetime import date

class Emprestimo:
    def _init_(self, dvd, amigo, data_emprestimo=None, data_devolucao=None):
        self.dvd = dvd
        self.amigo = amigo
        self.data_emprestimo = data_emprestimo if data_emprestimo else date.today()
        self.data_devolucao = data_devolucao

    def _str_(self):
        return f"{self.dvd.titulo} emprestado para {self.amigo.nome} em {self.data_emprestimo}"
