# DESAFIO 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
cores = {
    'Negrito-azul' : '\033[1;4;44m',
    'Negrito-vermelho' : '\033[1;4;41m',
    'Negrito-verde' : '\033[1;4;42m',
    'Limpar' : '\033[m'
}
numero = int(input('`Por favor, Digite um número: '))
antes = numero - 1
depois = numero + 1
print('O número digitado foi {}{}{}, seu sucessor é {}{}{} e seu antecessor é {}{}{}. '.format(cores['Negrito-azul'],numero, cores['Limpar'],cores['Negrito-verde'], depois, cores['Limpar'], cores['Negrito-vermelho'],antes, cores['Limpar']))
