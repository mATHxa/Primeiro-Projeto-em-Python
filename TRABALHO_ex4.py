# Mensagem de boas-vindas
print('Bem-vindo a biblioteca do Mateus da Silva')

# Inicialização das lista de livros
lista_livro = []
id_global = 0

def cadastrar_livro(id):
        # Função para cadastrar livro
        nome = input("Nome do livro: ")
        autor = input("Autor do livro: ")
        editora = input("Editora do livro: ")

        livro= {
            'id': id,
            'nome': nome,
            'autor': autor,
            'editora': editora
        }

        lista_livro.append(livro)
        print('Livro cadastrado com sucesso!')
def consultar_livro():
    # Função para consultar livro
    while True:
        print('-' * 40)
        print('-' * 10, 'MENU CONSULTAR LIVRO', '-' * 10)
        opcao = input('Consulta dos livros: \n'
                      '1 - Consultar todos os livros \n'
                      '2 - Consultar livro por id \n'
                      '3 - Consultar livro(s) por autor \n'
                      '4 - Retornar \n'
                      '>> ')

        if opcao == '1':
            print("Consultando todos os livros:")
            for livro in lista_livro:
                print(livro)

        elif opcao == '2':
            id_consulta = int(input('Digite o id do livro: '))
            encontrado = False
            for livro in lista_livro:
                if livro['id'] == id_consulta:
                    print(livro)
                    encontrado = True
                    break
            if not encontrado:
                print('Livro não encontrado.')

        elif opcao == '3':
            autor_consulta = input('Digite o autor do livro: ')
            encontrado = False
            for livro in lista_livro:
                if livro['autor'] == autor_consulta:
                    print(livro)
                    encontrado = True
            if not encontrado:
                print('Livro não encontrado.')

        elif opcao == '4':
            break
        else:
            print('Opção inválida.')

def remover_livro():
    # Função para remover livro
    while True:
        id_remover = int(input('Digite o id do livro a ser removido: '))
        encontrado = False
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print(f'Livro removido com sucesso.')
                encontrado = True
                break
        if not encontrado:
                print('Id inválido.')
        else:
            break
def main():
    global id_global
    while True:
        print('-' * 42)
        print('-' * 10, 'MENU CONSULTAR LIVRO', '-' * 10)
        opcao = input('Consulta dos livros: \n'
                '1 - Cadastrar livro \n'
                '2 - Consultar livro \n'
                '3 - Remover Livro \n'
                '4 - encerrar programa \n'
                '>> ')

        if opcao == '1':
            id_global += 1
            cadastrar_livro(id_global)
        elif opcao == '2':
            consultar_livro()
        elif opcao == '3':
            remover_livro()
        elif opcao == '4':
            print('Programa encerrado.')
            break
        else:
            print('Opção inválida.')

if __name__ == "__main__":
    main()
