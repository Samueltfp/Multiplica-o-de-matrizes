 # Definição das matrizes
A = [[3, 1, 3], [6, 5, 5]]
B = [[100, 50], [50, 100], [50, 50]]

# Matriz resultado
C = [[0, 0], [0, 0]]

# Multiplicação das matrizes
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

# Resultado
for row in C:
    print(row)