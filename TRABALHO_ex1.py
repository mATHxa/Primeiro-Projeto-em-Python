print('Bem-Vindo a loja do Mateus da Silva')
valor = float(input('Qual o valor do produto: '))
qtd = int(input('Qual a quantidade do produto: '))


# Se o valor for MENOR que 2500 o desconto será 0%
if(valor * qtd > 0 and valor * qtd < 2500 and qtd != 0):
    print(f'O valor sem desconto: {valor * qtd}')

# Se o valor for IGUAL OU MAIOR que 2500 e MENOR que 6000 o desconto será 4%
elif(valor * qtd >= 2500 and valor * qtd < 6000 and qtd != 0):
    desconto = (valor * qtd) * 4 // 100
    produto = (valor * qtd) - desconto

    print(f'O valor sem desconto: {valor * qtd}')
    print(f'O valor com desconto: {produto}')

# Se o valor for IGUAL OU MAIOR que 6000 e MENOR que 10000 o desconto será 7%
elif(valor * qtd >= 6000 and valor * qtd < 10000 and qtd != 0):
    desconto = (valor * qtd) * 7 // 100
    produto = (valor * qtd) - desconto

    print(f'O valor sem desconto: {valor * qtd}')
    print(f'O valor com desconto: {produto}')
    
# Se o valor for MAIOR que 10000 o desconto será 11%
elif(valor * qtd >= 10000 and qtd != 0):
    desconto = (valor * qtd) * 11 // 100
    produto = (valor * qtd) - desconto    

    print(f'O valor sem desconto: {valor * qtd}')
    print(f'O valor com desconto: {produto}')

else:    
    print('Valor inválido. Tente novamente...')
