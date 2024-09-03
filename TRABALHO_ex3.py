print('Bem-vindo a copiadora do Mateus da Silva') #Print de boas-vindas

def escolha_servico():
    servicos = {
       "DIG": 1.10,
       "ICO": 1.00,
       "IPB": 0.40,
       "FOT": 0.20
    }

    while True:
        servico = input("Qual o serviço desejado \n"
                        "DIG - Digitalização \n"
                        "ICO - Impressão Colorida \n"
                        "IPB - Impressão Preto e Branco \n"
                        "FOT - fotocópia \n"
                        ">> ")

        if servico in servicos:
            return servicos[servico]
        else:
            print("Opção inválida, escolha o tipo de serviço novamente.")

def num_pagina():
    while True:
        try:
            num_paginas = int(input("Digite o número de páginas (até 20000): "))

            if num_paginas >= 1 and num_paginas < 20:
                return num_paginas
            elif num_paginas >= 20 and num_paginas < 200:
                return num_paginas * 0.85
            elif num_paginas >= 200 and num_paginas < 2000:
                return num_paginas * 0.80
            elif num_paginas >= 2000 and num_paginas < 20000:
                return num_paginas * 0.75
            else:
                print("Número de páginas não permitido. Tente novamente")
        except ValueError:
            print("Entrada inválida. Por favor digite um número.")

def servico_extra():
    servicos_adicionais = {
        "1": 15.00,
        "2": 40.00,
        "0": 0
    }

    while True:
        extra = input("Deseja adicionar algum serviço? \n"
                      "1 - Encadernação Simples - R$ 15.00 \n"
                      "2 - Encadernação Capa Dura - R$ 40.00 \n"
                      "0 - Não desejo mais nada \n"
                      ">> ")

        if extra in servicos_adicionais:
            return servicos_adicionais[extra]
        else:
            print("Opção inválida. Por favor, escolha entre 1, 2, ou 0.")

if __name__ == "__main__":
    try:
        valor_servico = escolha_servico()

        paginas_com_desconto = num_pagina()

        valor_extra = servico_extra()

        total = (valor_servico * paginas_com_desconto) + valor_extra

        print(f"O total a pagar é: R${total:.2f}")

    except Exception as e:
        print(f'Ocorreu um erro: {e}')