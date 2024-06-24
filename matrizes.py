import numpy as np

A = np.array([[1, 2], [3, 5]])
B = np.array([[1, 3, 4], [4, 7 , -1]])
C = np.array([[2, 0], [1, 3]])

# print(A[0][1]) # Acessando um item da matriz

# Operações com matrizes:

#  - Somar duas matrizes
# Msoma = A + C
# print(Msoma)

# - Multiplicando uma matriz por um escalar
# Mesc = 2 * A
# print(Mesc)

# - Multiplicando duas Matrizes:
# AC = np.dot(A , C)
# print("AC = ",AC)

# - Transposta de uma matriz:
# A_tranposta = A.T
# print("A = ", A)
# print("A_transposta = ", A_tranposta)

# - Determinante de uma matriz:
# Adet = np.linalg.det(A)
# print("Determinante de A = ", Adet)

# - Inversa de uma matriz:
# Ainv = np.linalg.inv(A)
# print("Inversa de A = ", Ainv)