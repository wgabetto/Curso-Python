co = int(input('Qual a medida do cateto oposto? '))
ca = int(input('Qual a medida do cateto adjacente? '))
H = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é {}'.format(H))
#fazendo uso da bliblioteca
from math import hypot
h = hypot(co, ca)
print(h)