num = int(input('Escolha um numero inteiro:'))

print(''' Escolha uma das bases para conversao:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL 
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Opção escolhida:'))

if opcao == 1:
   print('{} Convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')