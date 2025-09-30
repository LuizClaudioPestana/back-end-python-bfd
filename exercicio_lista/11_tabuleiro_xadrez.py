import numpy as np

tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]

tabuleiro[0] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

tabuleiro[1] = ["pea"] * 8

tabuleiro[6] = ["pea"] * 8

tabuleiro[7] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

tabuleiro_np = np.array(tabuleiro)

print("\nTabuleiro de Xadrez:")
for linha in tabuleiro_np:
    print(" ".join(linha))
