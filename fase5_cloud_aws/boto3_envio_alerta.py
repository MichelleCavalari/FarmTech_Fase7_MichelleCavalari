# fase5_cloud_aws/boto3_envio_alerta.py
"""
Alerta de irrigação:
- Modo SIMULADO (padrão): imprime a mensagem (útil p/ demo e README).
- Modo REAL (SNS): se USE_AWS=1 e SNS_TOPIC_ARN estiver definido, envia via AWS SNS.

Como setar (Windows, PowerShell):
  setx USE_AWS "1"
  setx AWS_DEFAULT_REGION "sa-east-1"   # ou sua região
  setx SNS_TOPIC_ARN "arn:aws:sns:...:meu-topico"
  # reinicie o PyCharm após setx
"""

import os
import random
from datetime import datetime

USE_AWS = os.getenv("USE_AWS", "0") == "1"
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN", "")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "sa-east-1")

def gerar_leitura_exemplo():
    """Simula uma leitura de sensor (você pode trocar para ler do SQLite se quiser)."""
    leitura = {
        "umidade": round(random.uniform(10, 80), 1),
        "temperatura": round(random.uniform(18, 36), 1),
        "setor": random.choice(["A", "B", "C"])
    }
    return leitura

def construir_mensagem(leitura):
    acoes = []
    if leitura["umidade"] < 25:
        acoes.append(f"Irrigar setor {leitura['setor']} por 15 minutos")
    if leitura["temperatura"] > 32:
        acoes.append("Verificar sombreamento/ventilação")
    if not acoes:
        acoes.append("Sem ação: condições dentro da faixa")
    msg = (
        f"[FarmTech Alert] {datetime.now():%Y-%m-%d %H:%M:%S}\n"
        f"Umidade: {leitura['umidade']}% | Temp: {leitura['temperatura']}°C | Setor: {leitura['setor']}\n"
        f"Ação recomendada: {', '.join(acoes)}"
    )
    return msg

def enviar_alerta(mensagem):
    if not USE_AWS:
        print("=== MODO SIMULADO ===")
        print(mensagem)
        return "SIMULADO_OK"

    # Modo real via SNS
    try:
        import boto3
        if not SNS_TOPIC_ARN:
            raise RuntimeError("SNS_TOPIC_ARN não definido no ambiente.")
        sns = boto3.client("sns", region_name=AWS_REGION)
        resp = sns.publish(TopicArn=SNS_TOPIC_ARN, Message=mensagem, Subject="Alerta FarmTech")
        print("Alerta enviado via SNS. MessageId:", resp.get("MessageId"))
        return resp.get("MessageId")
    except Exception as e:
        print("Falha ao enviar SNS. Caindo para MODO SIMULADO.\nMotivo:", e)
        print("=== MODO SIMULADO ===")
        print(mensagem)
        return "FALLBACK_SIMULADO"

if __name__ == "__main__":
    leitura = gerar_leitura_exemplo()
    msg = construir_mensagem(leitura)
    enviar_alerta(msg)
