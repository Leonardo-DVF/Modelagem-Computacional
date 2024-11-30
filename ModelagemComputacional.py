import subprocess
import sys

# Verifica se o numpy já está instalado, caso contrário, instala
try:
    import numpy as np

    # Matriz Original
    A = np.array([[2, 0, 0, 0], [2, 2, 0, 0], [1, -1, 2, -1], [0, 1, -1, 2]])

    # Cálculo dos autovalores e autovetores
    autovalores, autovetores = np.linalg.eig(A)

    # Formando a matriz diagonal (D)
    D = np.diag(autovalores)

    # Matriz inversa dos autovetores (P^-1)
    P_inv = np.linalg.inv(autovetores)

    # Verificando a diagonalização: A = P @ D @ P^-1
    A_reconstruida = autovetores @ D @ P_inv

    print("Integrantes: Leonardo Duarte Veiga Ferreira, Rafael Gomes Parente e Yann Soares Guimarães")
    print("Tema do problema: Construção de um algoritmo para resolver problemas de autovalor e autovetor de uma matriz, e realizar a diagonalização completa da matriz.")
    print("RESULTADOS:\n")

    # Exibindo os resultados
    print("Matriz Original:")
    print(A)

    print("\nAutovalores:")
    print(autovalores)

    print("\nAutovetores (P):")
    print(autovetores)

    print("\nMatriz Diagonal (D):")
    print(D)

    print("\nMatriz Inversa dos Autovetores (P^-1):")
    print(P_inv)

    print("\nReconstrução da Matriz (P @ D @ P^-1):")
    print(np.round(A_reconstruida, decimals=2))  # Arredondamento para evitar imprecisões numéricas

    # Verificando se a diagonalização foi realizada corretamente
    if np.allclose(A, A_reconstruida):
        print("\nA matriz foi diagonalizada corretamente!")
    else:
        print("\nErro na diagonalização. A reconstrução não corresponde à matriz original, logo a matriz não é diagonalizável...")
        
except ImportError:
    print("Numpy não encontrado. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np
    print("Numpy instalado e importado como np.")
