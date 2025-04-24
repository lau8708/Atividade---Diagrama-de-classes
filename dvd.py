class DVD:
    def __init__(self, titulo, sinopse, diretor, ator_principal, genero, faixa_etaria):
        self.titulo = titulo
        self.sinopse = sinopse
        self.diretor = diretor
        self.ator_principal = ator_principal
        self.genero = genero
        self.faixa_etaria = faixa_etaria

    def __str__(self):
        return f"DVD: {self.titulo} ({self.genero}) - Direção: {self.diretor}"class DVD:
    def __init__(self, titulo, sinopse, diretor, ator_principal, genero, faixa_etaria):
        self.titulo = titulo
        self.sinopse = sinopse
        self.diretor = diretor
        self.ator_principal = ator_principal
        self.genero = genero
        self.faixa_etaria = faixa_etaria

    def __str__(self):
        return f"DVD: {self.titulo} ({self.genero}) - Direção: {self.diretor}"
