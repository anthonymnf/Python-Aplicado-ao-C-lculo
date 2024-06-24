import numpy as np

# Criando vetores usando NUmpy

# v1 = np.array([1, 2, 3])
# print(v1)
# v2 = np.array([-1, 2, 3])
# print(v2)

# v3 = np.arange(0,11,2) #O segundo argumento não entra no array
# print(v3)

# v4 = np.arange(3,0, -0.4) #Array decrescivo
# print(v4)

# v5 = np.linspace(0, 20, 7)
# print(v5)
# print("Último valor do vetor = ", v5[-1])
# v5[-1] = 30
# print("Último valor do vetor atualizado = ", v5[-1])

# Operações com vetores:
v1 = np.array([1, 2, 3])
v2 = np.array([-1, 2, -3])

# vsoma = v1 + v2
# print("Soma de vetores: ", vsoma)

# vsub = v1 - v2
# print("Subtração de vetores: ", vsub)

# vmult_esc = v1 * 2
# print("Multiplicação de v1 * 2: ", vmult_esc)

# v_produto_escalar = np.dot(v1, v2)
# print("Produto escalar de v1 e v2: ", v_produto_escalar )

# v_produto_vetorial = np.cross(v1, v2)
# print("Produto vetorial de v1 e v2: ", v_produto_vetorial )

norma_vet = np.linalg.norm(v1)
print("Norma do vetor v1: ", norma_vet)
