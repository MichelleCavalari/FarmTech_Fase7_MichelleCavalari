# 🌱 FarmTech Solutions – Fase 7  
### Sistema Integrado de Gestão Agrícola com IoT, Machine Learning, Cloud e Visão Computacional  
**Curso:** Inteligência Artificial – FIAP  
**Aluna:** Michelle Cavalari  
**Fase:** 7 (Integração Final)

---

## 🎯 Descrição Geral

Nesta fase, o objetivo foi **integrar todos os serviços desenvolvidos entre as Fases 1 a 6** em um sistema completo, centralizado e funcional, capaz de consolidar as soluções da FarmTech Solutions em um único ambiente.  

O projeto utiliza **Python**, **IoT (ESP32)**, **Machine Learning**, **AWS Cloud**, **Streamlit** e **Visão Computacional (YOLO/STUB)**, compondo um ecossistema digital que pode ser facilmente adaptado para outros setores além do agronegócio.

---

## 🧩 Estrutura do Projeto

```
FarmTech_Fase7_MichelleCavalari/
├── main.py                          # Menu principal de integração
├── README.md                        # Documentação do projeto
├── requirements.txt                 # Dependências do projeto
│
├── fase1_base_dados/
│   └── calculos_area.py             # Cálculo de área e insumos
│
├── fase2_banco_relacional/
│   └── estoque.py                   # Controle de estoque e custos
│
├── fase3_iot_esp32/
│   └── simulador_iot.py             # Sensores e automação IoT
│
├── fase4_dashboard_ml/
│   └── dashboard.py                 # Dashboard interativo (Streamlit + ML)
│
├── fase5_cloud_aws/
│   └── boto3_envio_alerta.py        # Serviço de mensageria AWS (simulado/real)
│
└── fase6_visao_computacional/
    ├── predict_yolo.py              # Processamento de imagens YOLO/STUB
    ├── imagens_teste/               # Imagens de entrada
    ├── resultados/                  # Resultados gerados
    └── weights/                     # Pesos YOLO (opcional)
```

---

## ⚙️ Execução do Sistema

### 🔸 Instalação das dependências
```bash
pip install -r requirements.txt
```

### 🔸 Execução do menu principal
```bash
python main.py
```

O menu exibe as fases integradas:
```
🌾 FarmTech - Sistema Integrado (Fase 7)
[1] Fase 1: Cálculos
[2] Fase 2: Estoque/ Custos
[3] Fase 3: IoT/ Sensores (simulado)
[4] Fase 4: Dashboard (Streamlit)
[5] Fase 5: AWS Alertas
[6] Fase 6: Visão Computacional
[0] Sair
```
<img width="1017" height="378" alt="image" src="https://github.com/user-attachments/assets/9e5f4fb2-3794-417e-aa29-2b4a111cf43c" />

---

## 💻 Módulos e Funcionalidades

### 🌾 **Fase 1 – Base de Dados Inicial**
- Cálculo de área de plantio e manejo de insumos.
- Geração de base de dados inicial para análise posterior.

---

### 📊 **Fase 2 – Banco de Dados Estruturado**
- Estrutura relacional de estoque e custos.
- CRUD completo com persistência em arquivo JSON.

---

### 🌡️ **Fase 3 – IoT e Automação**
- Simulação de sensores (umidade, temperatura, nutrientes).
- Lógica de irrigação automática com ESP32 simulado.

---

### 📈 **Fase 4 – Dashboard e Machine Learning**
- Dashboard interativo via **Streamlit**.
- Modelo de Regressão Logística (Scikit-Learn) para previsão de irrigação.
- Visualização de métricas e gráficos.

---

### ☁️ **Fase 5 – Cloud e Segurança (AWS)**
- Integração simulada de mensageria AWS (SNS).
- Logs de segurança e compliance (ISO 27001 e 27002).

---

### 🤖 **Fase 6 – Visão Computacional**
- Detecção de pragas e falhas na lavoura usando YOLOv8.
- Caso o modelo `best.pt` não esteja disponível, executa **modo STUB** com imagens geradas automaticamente.
- Resultados salvos em `/fase6_visao_computacional/resultados/`.

## 🧠 Como Rodar o Dashboard

```bash
streamlit run fase4_dashboard_ml/dashboard.py
```

A dashboard exibe:
- Leitura de sensores em tempo real.
- Gráficos interativos.
- Treinamento e teste do modelo de ML.
- Aba “Alertas AWS” com botão de envio de alerta (via SNS ou modo simulado).

---

## 🤝 Equipe e Tecnologias

| Componente | Tecnologia |
|-------------|-------------|
| Linguagem Principal | Python 3.13 |
| Dashboard | Streamlit |
| Banco de Dados | SQLite |
| Machine Learning | Scikit-Learn |
| IoT | ESP32 (simulado) |
| Cloud | AWS SNS / Boto3 |
| Visão Computacional | YOLOv8 / Pillow |
| IDE | PyCharm |

---

## 🎥 Demonstração

📹 **Vídeo (até 10 min):**  
Mostrando todas as funcionalidades das Fases 1 a 6 integradas via menu.  
**Link YouTube (não listado):**  
👉 [https://youtu.be/ZKANloa7LRI]


