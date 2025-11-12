# fase1_base_dados/calculos_area.py
# Funções reutilizáveis + modo CLI para rodar pelo terminal/menu

from dataclasses import dataclass

# ---- Funções base ----
def area_retangular(largura_m: float, comprimento_m: float) -> float:
    """Área em m²."""
    return largura_m * comprimento_m

def hectares(area_m2: float) -> float:
    """Converte m² para hectares."""
    return area_m2 / 10_000

def sementes_por_hectare(densidade_kg_ha: float, area_m2: float) -> float:
    """Quantidade de sementes (kg) para a área."""
    return densidade_kg_ha * hectares(area_m2)

def custo_total_hectare(custo_sementes_kg: float, kg_sementes_ha: float,
                        custo_fert_ha: float, custo_def_ha: float,
                        custo_irrig_ha: float, custo_mao_obra_ha: float) -> float:
    """Soma de custos por hectare."""
    return (custo_sementes_kg * kg_sementes_ha
            + custo_fert_ha + custo_def_ha + custo_irrig_ha + custo_mao_obra_ha)

def custo_total(area_ha: float, custo_ha: float) -> float:
    """Custo total para a área em hectares."""
    return area_ha * custo_ha

# ---- Estrutura para resultado (útil se você quiser importar na dashboard) ----
@dataclass
class ResumoCustos:
    area_m2: float
    area_ha: float
    kg_sementes: float
    custo_por_hectare: float
    custo_total: float

def calcular_resumo(largura_m: float, comprimento_m: float,
                    densidade_kg_ha: float,
                    custo_sementes_kg: float, custo_fert_ha: float,
                    custo_def_ha: float, custo_irrig_ha: float,
                    custo_mao_obra_ha: float) -> ResumoCustos:
    area_m2 = area_retangular(largura_m, comprimento_m)
    area_ha = hectares(area_m2)
    kg_sem = sementes_por_hectare(densidade_kg_ha, area_m2)
    c_ha = custo_total_hectare(custo_sementes_kg, densidade_kg_ha,
                               custo_fert_ha, custo_def_ha,
                               custo_irrig_ha, custo_mao_obra_ha)
    c_total = custo_total(area_ha, c_ha)
    return ResumoCustos(area_m2, area_ha, kg_sem, c_ha, c_total)

# ---- Modo CLI (rodar pelo terminal ou main.py) ----
def cli():
    print("Fase 1 - Cálculos de Área e Insumos")
    try:
        largura = float(input("Largura do talhão (m): "))
        comprimento = float(input("Comprimento do talhão (m): "))
        densidade_kg_ha = float(input("Densidade de sementes (kg/ha): "))
        custo_sementes_kg = float(input("Custo da saca/quilo de sementes (R$ por kg): "))
        custo_fert_ha = float(input("Custo de fertilizante por ha (R$): "))
        custo_def_ha = float(input("Custo de defensivo por ha (R$): "))
        custo_irrig_ha = float(input("Custo de irrigação por ha (R$): "))
        custo_mao_obra_ha = float(input("Custo de mão de obra por ha (R$): "))
    except ValueError:
        print("Valores inválidos.")
        return

    r = calcular_resumo(largura, comprimento, densidade_kg_ha,
                        custo_sementes_kg, custo_fert_ha,
                        custo_def_ha, custo_irrig_ha, custo_mao_obra_ha)

    print("\n--- Resumo ---")
    print(f"Área: {r.area_m2:.2f} m² ({r.area_ha:.4f} ha)")
    print(f"Sementes necessárias: {r.kg_sementes:.2f} kg")
    print(f"Custo por hectare: R$ {r.custo_por_hectare:.2f}")
    print(f"Custo total: R$ {r.custo_total:.2f}")

if __name__ == "__main__":
    cli()
elif opcao == "1":
    os.system("python fase1_base_dados/calculos_area.py")
