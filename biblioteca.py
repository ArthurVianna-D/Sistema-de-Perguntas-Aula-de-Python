class Livro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = 'Disponível' if self.disponivel else 'Emprestado'

        return (
            f'Código: {self.codigo}\n'
            f'Título: {self.titulo}\n'
            f'Autor: {self.autor}\n'
            f'Status: {status}'
        )

