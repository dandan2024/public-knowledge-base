#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considerando US$1,00 = R$3,27

real = float(input('Quanto dinheiro você tem  na carteira? R$'))
dolar = real / 3.27
print('Com R${} você pode comprar US${}'.format(real, dolar))