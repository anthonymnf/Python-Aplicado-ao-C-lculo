import numpy as np

# Ex. de sistema de equações:
# 2x + y = 5
# -3x + 4y = 2

A = np.array([[2, 1], [-3, 4]]) #Matriz com as duas eq
B = np.array([5, 2]) # Matriz com os resultados das eq

x = np.linalg.solve(A, B)
print("Valores de x: ")
print(x)