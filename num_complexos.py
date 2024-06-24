import numpy as np

# Notação retangular:
# z = 3 + 1j*4

# print("Real = ", np.real(z))
# print("Imaginaria = ", np.imag(z))
# print("Magnitude = ", np.abs(z))
# print("Fase(rad) = ", np.angle(z))
# print("Fase(graus) = ", np.angle(z)*180/np.pi)

# Notação polar: z = 2e^pi/3
# z = 2*np.exp(1j*np.pi/3)
# print("Magnitude = ", np.abs(z))
# print("Fase(rad) = ", np.angle(z))
# print("Real = ", np.real(z))
# print("Imaginaria = ", np.imag(z))

# # Conjugado de Z:
# z = 3 + 1j*4
# zconj = np.conj(z)
# print("Conjugado de Z = ", zconj)

# Operações com Números complexos:
#   z1=3+j4  e  z2=5−j2 , vamos determinar  z1+z2 ,  z1−z2 ,  z1z2  e  z1/z2 .
z1 = 3 + 1j*4
z2 = 5 - 1j*2

zsoma = z1 + z2
print("Zsoma = ", zsoma)

zssub = z1 - z2
print("Zssub = ", zssub)

zmult = z1 * z2
print("Zmult = ", zmult)

zdiv = z1 / z2
print("Zdiv = ", zdiv)