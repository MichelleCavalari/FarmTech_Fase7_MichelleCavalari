import os

def menu():
    print("\n🌾 FarmTech - Sistema Integrado (Fase 7)")
    print("[1] Fase 1: Cálculos")
    print("[2] Fase 2: Estoque/ Custos")
    print("[3] Fase 3: IoT/ Sensores (simulado)")
    print("[4] Fase 4: Dashboard (Streamlit)")
    print("[5] Fase 5: AWS Alertas")
    print("[6] Fase 6: Visão Computacional")
    print("[0] Sair")

while True:
    menu()
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        os.system("python fase1_base_dados/calculos_area.py")
    elif opcao == "2":
        os.system("python fase2_banco_relacional/estoque.py")
    elif opcao == "3":
        os.system("python fase3_iot_esp32/simulador_iot.py")
    elif opcao == "4":
        os.system("streamlit run fase4_dashboard_ml/dashboard.py")
    elif opcao == "5":
        os.system("python fase5_cloud_aws/boto3_envio_alerta.py")
    elif opcao == "6":
        os.system("python fase6_visao_computacional/predict_yolo.py")
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
