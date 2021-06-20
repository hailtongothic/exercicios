a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

delta = (b ** 2) - 4 * a * c

if delta <0:
    print('Não tem Raiz Real!')
if delta == 0:
    print('Tem uma Raiz Real!')
if delta > 0:
    print('Tem duas Raizes Reais que são: {}, {} {}'.format(a, b, c))