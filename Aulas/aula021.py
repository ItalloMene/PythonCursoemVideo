# Exemplo de Docstring:
def contador (i, f, p):
    """
     → Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVídeo
    """

    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')

help(contador)

#Exemplo de Parâmetro Opcional
def somar(a = 0,b = 0,c = 0):
    s = a + b + c
    print(f'A soma vale {s}.')

somar(3, 2, 5)
somar(8, 4)
somar(6)
somar(b=5, c=6)
somar(c=3, b=2)
somar()


print()
# Exemplo Escopo Global e Escopo Local
def teste(b):
    #global a - faz com que a variável 'a' global seja utilizada
    a = 8 # variável 'a' local
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 # variável 'a' global
teste(a)
print(f'A fora vale {a}')
#print(f'B fora vale {b}') - apresentará ERRO por conta do escopo local na função teste()
#print(f'C fora vale {c}') - apresentará ERRO da mesma forma que o B, por falta de Escopo

print()
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')

print()
# Uso do return - Retorno de Variável
def somar2(a=0,b=0,c=0):
    s = a + b + c
    return s
resp = somar2(3,2,5)
print(resp)
#ou
print(somar2(3,2,5))
#ou
r1 = somar2(3,2,5)
r2 = somar2(1,7)
r3 = somar2(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

print()
# Exemplo prática 1
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

print()
# Exemplo prática 2
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número:'))
if par(num):
    print('É par!')
else:
    print('Não é par!')