"""
Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o seu status
de acordo com a tabela abaixo:
- Abaixo de 18.5: abaixo do peso ideal;
- Entre 18.5 e 25: peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida;
"""
print('=' * 22)
print('  \033[94mAVALIADOR DE IMC\033[m')
print('=' * 22)
nome = str(input('Digite o nome da pessoa a ser avaliada: '))
altura = float(input('Digite sua altura (x.xx): '))
peso = float(input('Digite seu peso em Kg: '))
imc = peso / pow(altura, 2)

print('=' * 15)
print('   \033[94mRESULTADO\033[m')
print('=' * 15)
if (imc > 0) and (imc < 18.5):
    print('O resultado do IMC de \033[1;96m{}\033[m é \033[1;96m{:.1f}\033[m, considerado como \033[1;96mAbaixo do peso\033[m.'.format(nome, imc))
elif (imc >= 18.5) and (imc < 25):
    print('O resultado do IMC de \033[1;96m{}\033[m é \033[1;96m{:.1f}\033[m, considerado como \033[1;96mPeso ideal\033[m.'.format(nome, imc))
elif (imc >= 25) and (imc < 30):
    print('O resultado do IMC de \033[1;96m{}\033[m é \033[1;96m{:.1f}\033[m, considerado como \033[1;96mSobrepeso\033[m.'.format(nome, imc))
elif (imc >= 30) and (imc < 40):
    print('O resultado do IMC de \033[1;96m{}\033[m é \033[1;96m{:.1f}\033[m, considerado como \033[1;96mObesidade\033[m.'.format(nome, imc))
elif imc >= 40:
    print('O resultado do IMC de \033[1;96m{}\033[m é \033[1;96m{:.1f}\033[m, considerado como \033[1;96mObesidade mórbida\033[m.'.format(nome, imc))
else:
    print('\033[91m[ERRO] Não foi possível calcular o IMC!\033[m \nPor favor tente novamente!')
