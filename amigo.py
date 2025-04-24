class Amigo:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Amigo: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"
