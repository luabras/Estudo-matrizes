import numpy as np

#--------------------Criando matrizes--------------------

#Elementos das linhas sao separados por virgulas
#Colunas sao novos colchetes

# |2 -1|
# |0  4|
A = np.array([[2, -1], [0, 4]])
print("Matriz A:\n", A, "\n")

# |1 0 -4|
# |4 -3 2|
B = np.array([[1, 0, -4], [4, -3, 2]])
print("Matriz B:\n", B, "\n")

#Outra representacao de matriz no numpy
# |1 2|
# |3 4|
C = np.matrix('1 2; 3 4')
print("Matriz C:\n", C, "\n")

#Outra representacao de matriz no numpy
# |2 -1|
# |0  4|
D = np.matrix([[2, -1], [0, 4]])
print("Matriz D:\n", D, "\n")





#--------------------Tipos de matrizes--------------------

#Matriz linha 
# |3, 4, 5|
L = np.array([[3, 4, 5]])
print("Matriz linha:\n", L)
print("Formato da matriz (linhas, colunas):", L.shape, "\n")

#Matriz coluna 
# |1|
# |3|
# |7|
CL = np.array([[1], [3], [7]])
print("Matriz coluna:\n", CL)
print("Formato da matriz (linhas, colunas):", CL.shape, "\n")

#Matriz nula 
N = np.zeros([2, 2]) #matriz 2x2
print("Matriz nula:\n", N, "\n")

#Matriz diagonal
# |1 0 0 0 0|
# |0 3 0 0 0|
# |0 0 7 0 0|
# |0 0 0 8 0|
# |0 0 0 0 4|
DI = np.diag([1, 3, 7, 8, 4])
print("Matriz diagonal:\n", DI, "\n")
print("Formato da matriz (linhas, colunas):", DI.shape, "\n")

#Matriz identidade
I = np.eye(4) #matriz 4x4
print("Matriz identidade:\n", I, "\n")





#--------------------Matrizes transpostas--------------------

# S eh uma matriz simetrica, sua transposta eh igual a ela mesma
# |1 4 3|
# |4 2 5|
# |3 5 0|
S = np.array([[1, 4, 3], [4, 2, 5], [3, 5, 0]])
transS = np.transpose(S)
print("Matriz transposta de S:\n", transS, "\n")

# |1 2 3 6|
# |9 7 4 6|
A2 = np.array([[1, 2, 3, 6], [9, 7, 4, 6]])
transA2 = np.transpose(A2)
print("Matriz transposta de A2:\n", transA2, "\n")

#Outro metodo de calcular a transposta
trans2A2 = A2.T
print("Matriz transposta de A2, usando .T:\n", trans2A2, "\n")

# |8 5 3 3|
# |1 0 1 8|
B2 = np.array([[8, 5, 3, 3], [1, 0, 1, 8]])
transB2 = np.transpose(B2)
print("Matriz transposta de B2:\n", transB2, "\n")

#Comparando se duas matrizes são iguais
print("S eh igual a sua transposta?\n", np.array_equal(S, transS), "\n")

#A transposta de uma soma eh igual a soma das transpostas
print("A transposta de uma soma eh igual a soma das transpostas?", np.array_equal((A2+B2).T, (A2.T+B2.T)), "\n")





#--------------------Slicing--------------------

# |2 4 6|
# |4 7 1|
# |9 3 8|
A3 = np.array([[2, 4, 6], [4, 7, 1], [9, 3, 8]])
print(A3[:], "\n") #acessando todos os elementos da matriz
print(A3[:,:], "\n") #outra forma de acessar todos os elementos da matriz
print("Formato da matriz A3 (linhas, colunas):", A3.shape, "\n")

#Slicing da matriz A3
print("Elementos da segunda linha:", A3[1,:], "\n") #acessando todos os elementos da segunda linha [linha 1; todas as colunas]
print("Elementos da terceira linha:", A3[2,:], "\n") #acessando todos os elementos da terceira linha [linha 2; todas as colunas]
print("Elemento da segunda linha e segunda coluna:", A3[1,1], "\n") #acessando o elemento 7 [linha 1; coluna 1]
print("Elemento da terceira linha e primeira coluna:", A3[2,0], "\n") #acessando o elemento 9 [linha 2; coluna 0]

#Criando uma copia da matriz A3 (nao se deve usar apenas o =, e sim o copy())
B3 = A3.copy()
print("Matriz B3:\n", B3, "\n")

#Mudando o valor do elemento de B3 da segunda linha e terceira coluna
B3[1,2] = 77
print("Colocando 77 no valor do elemento da segunda linha e terceira coluna de B3:\n", B3, "\n")

#Mudando o valor do elemento de B3 da terceira linha e primeira coluna
B3[2,0] = 123
print("Colocando 123 no valor do elemento da terceira linha e primeira coluna de B3:\n", B3, "\n")

#Criando uma matriz da segunda coluna de B3
C2 = B3[:,1].copy()
print("Criando uma matriz C2 a partir da segunda coluna de B3:\n", C2, "\n")

# |2 3 7 1| 
# |8 6 9 3|
# |6 9 3 2|
# |4 3 7 5|
A4 = np.array([[2, 3, 7, 1], [8, 6, 9, 3], [6, 9, 3, 2], [4, 3, 7, 5]])

#Pegando os elementos 9, 3 e 2 (terceira linha, a partir da segunda coluna ate o fim)
A4[2, 1:4] #[linha 2, coluna 1:ate o elemento 4]

#Pegando os elementos 4, 3 e 7 (quarta linha, da primeira ate a terceira coluna)
A4[3, 0:3] #[linha 3, coluna 0:ate o elemento 3]

#Pegando os elementos 9, 3 e 7 (terceira coluna, da segunda ate a quarta linha)
A4[1:4, 2] #[linha 1:ate o elemento 4, coluna 2]





#----------Operacoes com matrizes----------

# |2 4 6|
# |1 2 7|
# |3 2 9|
X = np.array([[2, 4, 6], [1, 2, 7], [3, 2, 9]])

# |-1 4 5|
# | 6 3 1|
Y = np.array([[-1, 4, 5], [6, 3, 1]])

# |0  4  3|
# |1 -3 -1|
# |3  1  2|
Z = np.array([[0, 4, 3], [1, -3, -1], [3, 1, 2]])

#Soma

#X e Y não podem ser somadas diretamente, pois elas nao tem as mesmas dimensoes
#X(3x3) e Y(2x3)

#Soma de linha
sLinha = X[0,:]+Y[0,:] #somando primeira linha de X com primeira linha de Y
print("Soma da primeira linha de X com a primeira linha de Y:\n", sLinha, "\n")

#Soma de coluna de Z e Y retorna erro pois numero de elementos diferentes

#Soma de todos os elementos
sXZ = X+Z
print("Soma de X e Z:\n", sXZ, "\n")

#Subtracao
subXZ = X-Z
print("Subtracao de X e Z:\n", subXZ, "\n")

#Multiplicacao (nao se deve usar *, e sim dot())
mXZ = Z.dot(X)
print("Multiplicacao de X e Z:\n", mXZ, "\n")

#Divisao

#X e Y não podem ser divididas diretamente, pois elas nao tem as mesmas dimensoes
#X(3x3) e Y(2x3)

DV = X/Z
print("Divisao de X e Z:\n", DV, "\n")

#Multiplicacao por escalar
k = 2
kX = k*X
print("Multiplicacao de X por 2:\n", kX, "\n")