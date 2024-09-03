print('  Bem-Vindo a loja de gelados do Mateus da Silva') #boas vindas
print('-' * 20, 'CARDÁPIO', '-' * 20)
print('-' * 50)
print('---|', ' Tamanho ', '|', '  Cupuaçu (CP) ', '|', ' Açaí (AC)', '|---')
print('---|', '    P    ', '|', '   R$  9,00    ', '|', ' R$ 11,00 ', '|---')
print('---|', '    M    ', '|', '   R$ 14,00    ', '|', ' R$ 16,00 ', '|---')
print('---|', '    G    ', '|', '   R$ 18,00    ', '|', ' R$ 20,00 ', '|---')
print('-' * 50)

# Inicialização do acumulador de valores dos pedidos
soma = 0

while True:
    # Solicitação do sabor ao usuário
    sabor = input('Escolha o sabor(AC/CP): ')
    if sabor not in ["AC", "CP"]:
        print('Sabor inválido. Tente novamente.')
        continue # Uso do continue para voltar ao início do loop


    # Solicitação do tamanho ao usuário
    tam = input('Escolha o tamanho(P/M/G): ')
    if tam not in ["P", "M", "G"]:
       print('Tamanho inválido. Tente novamente.')
       continue # Uso do continue para voltar ao início do loop


    else:
        # if/elif e/ou  else com cada uma das combinações de sabor e tamanho
        if sabor == "Cupuaçu" or sabor == "CP":
            if tam == "P":
                soma += 9
                print('Tamanho "P" de Cupuaçu (CP) custa R$10 reais')

            elif tam == "M":
                soma += 14
                print('Tamanho "M" de Cupuaçu (CP) custa R$14 reais')

            elif tam == "G":
                soma += 18
                print('Tamanho "G" de Cupuaçu (CP) custa R$18 reais')

        if sabor == "Açai" or sabor == "AC":
            if tam == "P":
                soma += 11
                print('Tamanho "P" de Açai (AC) custa R$10 reais')

            elif tam == "M":
                soma += 16
                print('Tamanho "M" de Açai (AC) custa R$14 reais')

            elif tam == "G":
                soma += 20
                print('Tamanho "G" de Açai (AC) custa R$18 reais')

        # Pergunta se o usuário deseja pedir mais alguma coisa
        pergunta = input('Deseja pedir mais alguma coisa? (S/N): ')
        if pergunta == "N":
            print('Valor total é de ' + str(soma) + ' reais!')
            break # Uso do break para sair do loop