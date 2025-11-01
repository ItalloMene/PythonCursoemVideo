"""
Desafio 083: Crie um programa onde o usuário digite uma expressão (matemática) qualquer que use parênteses.
O seu aplicativo deverá analisar a se expressão está com os parênteses abertos e fechados na ordem correta.
"""
cores = {
    'amarelo' : '\033[93m',
    'verde' : '\033[92m',
    'vermelho' : '\033[91m',
    'limpar' : '\033[m'
}

print('=' * 50)
print(f"{cores['amarelo']}{'EXPRESSÕES MATEMÁTICAS': ^50}{cores['limpar']}")
print('=' * 50)

expressao = str(input('→ Digite a expressão da sua escolha: ')).strip()

simbolos = list()

for simbolo in expressao:
    if simbolo == '(':
        simbolos.append('(')
    elif simbolo == ')':
        if len(simbolos) > 0:
            simbolos.pop()
        else:
            simbolos.append(')')
            break

if len(simbolos) == 0:
    print(f"{cores['verde']}=" * 50)
    print(f" → Expressão VÁLIDA!")
    print(f"=" * 50)
else:
    print(f"{cores['vermelho']}=" * 50)
    print(f" → Expressão INVÁLIDA!")
    print(f"=" * 50)
