# 📄 Modelo Preditivo de Risco de Queimadas

## 🔍 Objetivo

Este projeto tem como objetivo desenvolver um modelo preditivo baseado em dados ambientais e geográficos que calcula um **score de risco de queimadas** de 0 a 100. O score é derivado de variáveis com pesos cientificamente fundamentados e classificado em faixas de risco.

---

## 🔧 Tecnologias Utilizadas

* **Python 3**
* **Pandas** – Manipulação de dados
* **Scikit-learn** – Normalização dos dados (`MinMaxScaler`)
* **Jupyter Notebook ou Google Colab** – Ambiente de execução recomendado

---

## 📅 Variáveis de Entrada (Features)

| Variável              | Descrição                                    | Tipo                |
| --------------------- | -------------------------------------------- | ------------------- |
| `temperatura`         | Temperatura do ar (°C)                       | Numérica            |
| `umidade`             | Umidade relativa do ar (%)                   | Numérica            |
| `vento`               | Velocidade do vento (km/h)                   | Numérica            |
| `chuva`               | Precipitação acumulada (mm)                  | Numérica            |
| `ndvi`                | Índice de vegetação normalizada (NDVI)       | Numérica            |
| `solo`                | Tipo de cobertura do solo (codificado)       | Categórica numérica |
| `topografia`          | Altitude ou declividade (m ou %)             | Numérica            |
| `proximidade_urbana`  | Distância até áreas urbanas ou rodovias (km) | Numérica            |
| `historico_queimadas` | Nº de queimadas anteriores registradas       | Numérica            |
| `raios`               | Ocorrência de raios (quantidade)             | Numérica            |

---

## ⚖️ Pesos das Variáveis

| Variável               | Peso (%) |
| ---------------------- | -------- |
| Temperatura            | 20%      |
| Umidade                | 20%      |
| Vento                  | 15%      |
| Chuva                  | 10%      |
| NDVI                   | 10%      |
| Solo                   | 5%       |
| Topografia             | 5%       |
| Proximidade Urbana     | 5%       |
| Histórico de Queimadas | 5%       |
| Raios                  | 5%       |

---

## 🔎 Lógica do Modelo

1. **Normalização**: todas as variáveis são normalizadas (0 a 1) com `MinMaxScaler`.
2. **Ajuste dos valores**: para variáveis que reduzem o risco (umidade, chuva, NDVI), usamos `(1 - valor)`.
3. **Cálculo do Score**: soma ponderada dos valores normalizados segundo os pesos.
4. **Classificação**: o score é convertido para a escala de 0 a 100 e classificado.

---

## 📊 Faixas de Classificação

| Faixa de Score | Classificação de Risco | Descrição                                                             |
| -------------- | ---------------------- | --------------------------------------------------------------------- |
| 0 – 20         | Baixo                  | Condições favoráveis; baixa probabilidade de ocorrência de queimadas. |
| 21 – 40        | Moderado               | Condições que podem permitir queimadas; atenção recomendada.          |
| 41 – 60        | Alto                   | Condições propícias; medidas preventivas devem ser consideradas.      |
| 61 – 80        | Muito Alto             | Alto risco; ações preventivas são necessárias.                        |
| 81 – 100       | Extremo                | Risco crítico; medidas de emergência devem ser implementadas.         |

---

## 📤 Saídas do Modelo

* **Score de risco** (0 a 100)
* **Classificação textual** (Baixo, Moderado, Alto, Muito Alto, Extremo)

---

## 🔬 Futuras Melhorias

* Treinar um modelo supervisionado com dados históricos (labels reais)
* Integração com APIs de clima e imagens de satélite
* Criação de dashboard com Streamlit ou Dash
* Disponibilização via API para consumo por sistemas de monitoramento

---

> Para mais detalhes, consulte o notebook `modelo_queimadas.ipynb` ou entre em contato com os desenvolvedores.
