import numpy  as np
import matplotlib.pyplot as plt

# Por exemplo, vamos plotar a função: y(x)=cos(20πx)
x = np.linspace(0, 1, 1000) #Quanto mais pontos mais suave o gráfico
y = np.cos(20*np.pi*x)

#Plotar gráfico
# plt.xlabel("x")
# plt.ylabel("y(x)")
# plt.title("Gráfico de y(x)=cos(20πx)")
# plt.grid()
# plt.plot(x, y)
# plt.show()

# Colocando mais de uma função em um único gráfico
#Definindo o vetor x
# x = np.linspace(0, 2, 1500)

# #Definindo as funcoes
# y1 = x**2       #y1(x) = x^2
# y2 = x**3       #y2(x) = x^3
# y3 = np.sin(x)  #y3(x) = sin(x)

# #Criando os graficos
# plt.plot(x, y1, label="y = x^2")
# plt.plot(x, y2, label="y = x^3")
# plt.plot(x, y3, label="y = sin(x)")
# plt.xlabel("x")
# plt.title("Gráficos sobrepostos")
# plt.grid()
# plt.legend()
# plt.show()

#Subplot - Um gráfico do lado/abaixo do outro:
x = np.linspace(0, 2, 1500)

#Definindo as funcoes
y1 = x**2       #y1(x) = x^2
y2 = x**3       #y2(x) = x^3
y3 = np.sin(x)  #y3(x) = sin(x)

#Criando os graficos
plt.subplot(3, 1, 1)
plt.plot(x, y1, label="y = x^2")
plt.grid()
plt.xlabel("x")
plt.ylabel("y1(x)")

plt.subplot(3, 1, 2)
plt.plot(x, y2, label="y = x^3")
plt.grid()
plt.xlabel("x")
plt.ylabel("y2(x)")

plt.subplot(3, 1, 3)
plt.plot(x, y3, label="y = sin(x)")
plt.grid()
plt.xlabel("x")
plt.ylabel("y3(x)")

plt.tight_layout()
plt.show()

