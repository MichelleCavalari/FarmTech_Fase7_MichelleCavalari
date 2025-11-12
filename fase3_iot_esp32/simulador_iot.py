# fase3_iot_esp32/simulador_iot.py
import random
import time

def ler_sensores():
    return {
        "umidade": round(random.uniform(10, 80), 1),
        "temperatura": round(random.uniform(18, 36), 1),
        "ph_estimado": round(random.uniform(5.0, 7.5), 1)
    }

if __name__ == "__main__":
    print("Simulando 5 leituras de sensores...")
    for i in range(5):
        leitura = ler_sensores()
        print(f"[{i+1}] {leitura}")
        time.sleep(0.5)

    print("\nRegras:")
    print("- Se umidade < 25% -> Acionar irrigação setor A")
    print("- Se temperatura > 32°C -> Verificar sombreamento")
