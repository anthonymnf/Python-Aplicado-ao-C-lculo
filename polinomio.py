import numpy as np

# vamos criar o polinômio  p(x)=3x3+2x2−4x+1 .

# p = np.poly1d([3, 2, -4, 1]) # Sempre começa pelo coeficiente com maior peso
# print(p)

#Avaliando o polinomio
# y = p(2) #O polinomio p atua como uma função que retorna a imagem do p
# print(y)

# Operações com polinomios: p(x)=3x3+2x2−4x+1 e q(x)=x2−x+1
p = np.poly1d([3, 2, -4, 1])
q = np.poly1d([1, -1, 1])

#Soma:
# psum = p +q
# print(psum)

#Subtração:
# psub = p - q
# print(psub)

#Multiplicação:
# pmult = p * q
# print(pmult)

#Divisão:
# pdiv, prest = np.polydiv(p , q)
# print("Polinomio de quociente de p/q = ", pdiv)
# print("Polinomio de resto de p/q = ", prest)

# Raízes: (Vantagem: Calcula raízes de qualquer grau)
roots_p = np.roots(p)
roots_q = np.roots(q)
print("Raízes de p = ", roots_p)
print("Raízes de q = ", roots_q)



