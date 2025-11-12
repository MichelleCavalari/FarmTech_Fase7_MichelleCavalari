# fase6_visao_computacional/predict_yolo.py
from pathlib import Path
from typing import List
from PIL import Image

# --- Pastas base ---
BASE_DIR = Path(__file__).parent.resolve()
WEIGHTS = BASE_DIR / "weights" / "best.pt"
IN_DIR = BASE_DIR / "imagens_teste"
OUT_DIR = BASE_DIR / "resultados"

# --- Utilidades ---
def ensure_dirs() -> None:
    IN_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

def list_images(p: Path) -> List[Path]:
    exts = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}
    return [x for x in p.glob("*") if x.suffix.lower() in exts]

def debug_paths(imgs: List[Path]) -> None:
    print("=== DEBUG PATHS ===")
    print("BASE_DIR:", BASE_DIR)
    print("IN_DIR  :", IN_DIR, "(existe:", IN_DIR.exists(), ")")
    print("OUT_DIR :", OUT_DIR, "(existe:", OUT_DIR.exists(), ")")
    print("WEIGHTS :", WEIGHTS, "(existe:", WEIGHTS.exists(), ")")
    print("Imagens encontradas:", [p.name for p in imgs])
    print("===================\n")

# --- Processamento STUB (sem YOLO) ---
def stub_process(images: List[Path]) -> List[Path]:
    """Gera saída mesmo se a imagem de entrada estiver bloqueada."""
    outs = []
    for img in images:
        dest = OUT_DIR / f"{img.stem}_stub{img.suffix}"
        try:
            # 1) tenta abrir normalmente
            with Image.open(img) as im:
                im = im.convert("RGB")
                im.save(dest)
                outs.append(dest)
                print(f"[STUB] Gerado: {dest.name}")
        except Exception as e:
            # 2) se der PermissionError ou outro, cria uma imagem placeholder
            print(f"[STUB] Falha ao processar {img.name}: {e} -> usando placeholder")
            try:
                placeholder = Image.new("RGB", (320, 200), color=(30, 180, 90))
                # escreve um texto simples (sem depender de fonte externa)
                import PIL.ImageDraw as ImageDraw
                d = ImageDraw.Draw(placeholder)
                d.text((10, 10), f"PLACEHOLDER\n{img.name}", fill=(255, 255, 255))
                placeholder.save(dest)
                outs.append(dest)
                print(f"[STUB] Placeholder gerado: {dest.name}")
            except Exception as e2:
                print(f"[STUB] Falhou também no placeholder: {e2}")
    return outs


# --- Processamento YOLO (se houver pesos) ---
def yolo_process(images_dir: Path, conf: float = 0.25, imgsz: int = 640) -> List[Path]:
    from ultralytics import YOLO  # import tardio
    model = YOLO(str(WEIGHTS))

    # limpar OUT_DIR
    for f in OUT_DIR.glob("*"):
        try:
            if f.is_file():
                f.unlink()
        except Exception:
            pass

    model.predict(
        source=str(images_dir),
        conf=conf,
        imgsz=imgsz,
        save=True,
        project=str(OUT_DIR),
        name="predicoes",
        exist_ok=True,
        verbose=False
    )

    pred_dir = OUT_DIR / "predicoes"
    outs = []
    for f in pred_dir.glob("*"):
        try:
            with Image.open(f) as im:
                im = im.convert("RGB")
                dest = OUT_DIR / f.name
                im.save(dest)
                outs.append(dest)
                print(f"[YOLO] Gerado: {dest.name}")
        except Exception as e:
            print(f"[YOLO] Falha ao mover/salvar {f.name}: {e}")
    return outs

# --- Main ---
def main():
    print(">> START predict_yolo.py")
    ensure_dirs()

    # lista/gera imagem de teste
    imgs = list_images(IN_DIR)
    if not imgs:
        fake = IN_DIR / "teste.jpg"
        Image.new("RGB", (160, 120), color="green").save(fake)
        imgs = [fake]
        print(f"Criada imagem de teste: {fake.name}")

    debug_paths(imgs)

    # decide modo
    if WEIGHTS.exists():
        print("Executando YOLO (best.pt encontrado).")
        outs = yolo_process(IN_DIR)
    else:
        print("best.pt NÃO encontrado. Rodando em modo STUB (PIL).")
        outs = stub_process(imgs)

    # relatório
    if outs:
        print("\nArquivos gerados em:", OUT_DIR)
        for o in outs:
            print(" -", o.name)
    else:
        print("Nenhum arquivo de saída gerado.")

    input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    main()
