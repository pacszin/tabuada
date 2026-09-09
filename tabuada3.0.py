import time
print('---------------------------------------')
print('Calculadora de tabuada maneira :D')
print('---------------------------------------')
time.sleep(0.75)
n = int(input('Digite um número: '))
i = 1
while i <= 10:
    time.sleep(0.75)
    x = n*i
    print(f'{n} vezes {i} é igual a {x}')
    i += 1
fim = input('Obrigado por usar a calculadora. Pressione enter para sair:')
time.sleep(0.5)
print('Até a próxima :D')