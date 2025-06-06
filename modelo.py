import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Exemplo de DataFrame com dados fictícios
data = pd.DataFrame({
    'temperatura': [32, 28, 40],
    'umidade': [40, 60, 20],
    'vento': [12, 8, 15],
    'chuva': [0, 5, 0],
    'ndvi': [0.3, 0.6, 0.1],
    'solo': [1, 2, 3],  # 1: pastagem, 2: floresta, 3: solo exposto
    'topografia': [100, 250, 50],  # altitude ou declividade
    'proximidade_urbana': [2, 5, 1],  # em km
    'historico_queimadas': [5, 1, 10],  # nº de eventos anteriores
    'raios': [0, 1, 3]
})

# 2. Pesos conforme tabela
pesos = {
    'temperatura': 0.20,
    'umidade': 0.20,
    'vento': 0.15,
    'chuva': 0.10,
    'ndvi': 0.10,
    'solo': 0.05,
    'topografia': 0.05,
    'proximidade_urbana': 0.05,
    'historico_queimadas': 0.05,
    'raios': 0.05
}

# 3. Normalização dos dados (escala 0 a 1)
scaler = MinMaxScaler()
dados_normalizados = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

# 4. Cálculo do score ponderado
def calcular_score(row):
    score = 0
    for var in pesos:
        # Para variáveis que diminuem o risco (chuva, umidade, ndvi), invertemos
        if var in ['umidade', 'chuva', 'ndvi']:
            score += (1 - row[var]) * pesos[var]
        else:
            score += row[var] * pesos[var]
    return round(score * 100, 2)  # Escala 0-100

dados_normalizados['score'] = dados_normalizados.apply(calcular_score, axis=1)

# 5. Classificação de risco
def classificar_risco(score):
    if score <= 20:
        return "Baixo"
    elif score <= 40:
        return "Moderado"
    elif score <= 60:
        return "Alto"
    elif score <= 80:
        return "Muito Alto"
    else:
        return "Extremo"

dados_normalizados['classificacao'] = dados_normalizados['score'].apply(classificar_risco)

# 6. Resultado final
resultado = pd.concat([data, dados_normalizados[['score', 'classificacao']]], axis=1)
print(resultado)
