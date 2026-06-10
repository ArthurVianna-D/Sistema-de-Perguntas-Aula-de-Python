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

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print('\n===== CATÁLOGO =====')

        if not self.livros:
            print('Nenhum livro cadastrado.')
            return

        for livro in self.livros:
            print('-' * 30)
            print(livro)

    def buscar_por_codigo(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo:
                return livro

        return None
    
    def emprestar(self, codigo):
        livro = self.buscar_por_codigo(codigo)

        if livro is None:
            print('Livro não encontrado.')
            return

        if not livro.disponivel:
            print('Livro já emprestado.')
            return

        livro.disponivel = False
        print(f'"{livro.titulo}" emprestado com sucesso.')

    def devolver(self, codigo):
        livro = self.buscar_por_codigo(codigo)

        if livro is None:
            print('Livro não encontrado.')
            return

        livro.disponivel = True
        print(f'"{livro.titulo}" devolvido com sucesso.')

    def relatorio(self):
        total = len(self.livros)

        disponiveis = sum(
            1 for livro in self.livros
            if livro.disponivel
        )

        emprestados = total - disponiveis

        print('\n===== RELATÓRIO =====')
        print(f'Total: {total}')
        print(f'Disponíveis: {disponiveis}')
        print(f'Emprestados: {emprestados}')

