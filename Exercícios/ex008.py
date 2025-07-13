# DESAFIO 008 - Escreva um programa que leia um valor em metros e a exiba convertida em centímetros e milímetros.
# km hm dam m dm cm mm
from calendar import day_name

medida = float(input('Ums distãncia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a: \n{:.4f}km; \n{:.4f}hm; \n{:.4f}dam; \n{:.0f}dm; \n{:.0f}cm e {:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))