import subprocess
import sys

# Verifica se o numpy já está instalado, caso contrário, instala
try:
    # Numpy já está instalado e importado como np.
    import numpy as np

    a = 2
    b = 0
    c = -1
    d = 1

    # Definição da matriz
    matriz = np.array([
        [a, b, b, b],
        [a, a, b, b],
        [d, c, a, c],
        [b, d, c, a]
    ])

    # Cálculo dos autovalores e autovetores
    autovalores, autovetores = np.linalg.eig(matriz)

    # Ordenação dos autovalores e autovetores
    indices_ordenados = np.argsort(autovalores)
    autovalores_ordenados = autovalores[indices_ordenados]
    autovetores_ordenados = autovetores[:, indices_ordenados]

    autovetores_ajustados = []
    for i in range(autovetores_ordenados.shape[1]):
        autovetor = autovetores_ordenados[:, i]
        # Normalizar pelo maior valor absoluto
        autovetor /= np.max(np.abs(autovetor))
        # Arredondar para 1 casa decimal para correspondência exata
        autovetores_ajustados.append(np.around(autovetor, decimals=1))

    print("Matriz Utilizada: ")
    print("[2, 0, 0, 0],\n")
    print("[2, 2, 0, 0],\n")
    print("[1, -1, 2, -1],\n")
    print("[0, 1, -1, 2]\n")

    # Exibição dos autovalores e autovetores ajustados
    print("Autovalores ordenados:")
    print(autovalores_ordenados)

    print("\nAutovetores correspondentes:")
    for i, autovetor in enumerate(autovetores_ajustados):
        print(f"Autovetor correspondente ao autovalor λ = {autovalores_ordenados[i]}:")
        print(autovetor)

    print("\nNão é possível obter a diagonização da Matriz escolhida...")

# Caso o Numpy não esteja instalado, o trecho abaixo irá instalar.
except ImportError:
    print("Numpy não encontrado. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    import numpy as np
    print("Numpy instalado e importado como np.")
