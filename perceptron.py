import numpy as np

# Dados: (Nome, x0=1, Estudou, fez_Trabalho, passou)
dados = [
    ('Joãozinho', np.array([1, 0, 0]), 0),
    ('Huguinho',  np.array([1, 0, 1]), 0),
    ('Zezinho',   np.array([1, 1, 0]), 1),
    ('Luizinho',  np.array([1, 1, 1]), 1)
]

pesos = np.zeros(3)
taxa_aprendizagem = 0.1

print(f"Pesos Iniciais: {pesos}\n")

for ciclo in range(2):
    print(f"CICLO {ciclo + 1}")
    for nome, x, esperado in dados:
        obtido = 1 if np.dot(pesos, x) >= 0 else 0
        erro = esperado - obtido
        
        print(f"{nome:10} | In:{x} | Esperado:{esperado} | Obtido:{obtido}")
        
        if erro:
            pesos += taxa_aprendizagem * erro * x 
            print(f" -> Erro. Novos Pesos: {pesos}")
        else:
            print(f" -> OK")

print(f"\nResultado: {pesos}")