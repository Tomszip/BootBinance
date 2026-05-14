# BootBinance

Bot de trading algorítmico en Python conectado a Binance.

Actualmente el proyecto se encuentra en una etapa inicial de desarrollo enfocada en:

- arquitectura del sistema
- conexión con Binance Testnet
- lectura de datos de mercado
- preparación para paper trading

---

# Objetivo del proyecto

Construir un bot de trading modular y escalable que permita:

1. operar primero en paper trading
2. probar estrategias automáticamente
3. analizar rendimiento
4. incorporar gestión de riesgo
5. evolucionar hacia trading real
6. eventualmente integrar machine learning e IA

---

# Tecnologías utilizadas

- Python
- Binance API
- python-binance
- pandas
- python-dotenv
- Git / GitHub

---

# Estado actual del proyecto

## Etapa 1 — Inicialización

### Completado

- estructura base del proyecto
- entorno virtual Python
- integración con Git y GitHub
- conexión a Binance Testnet
- lectura de precio BTCUSDT
- lectura de velas OHLCV
- integración con pandas

### En desarrollo

- estrategias de trading
- indicadores técnicos
- loops persistentes
- manejo de errores

### Pendiente

- paper trading
- wallet virtual
- registro de operaciones
- base de datos
- dashboard
- backtesting
- trading real

---

# Estructura del proyecto

```text
BootBinance/
│
├── main.py
├── config.py
├── requirements.txt
├── .gitignore
├── .env
│
├── data/
├── logs/
│
├── services/
│   ├── __init__.py
│   └── market_data.py
│
├── strategies/
│   └── __init__.py
│
└── utils/
    └── __init__.py
