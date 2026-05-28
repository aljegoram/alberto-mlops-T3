import numpy as np
import pandas as pd
from pathlib import Path

RANDOM_SEED = 42
OUTPUT_PATH = Path("data/processed/pacientes_sinteticos.csv")

def clasificar_paciente(edad: int, presion: int, sintomas: int) -> str:
    if edad >= 80 and sintomas >= 9 and presion >= 180:
        return "ENFERMEDAD TERMINAL"
    if edad >= 60 and sintomas >= 8 and presion >= 150:
        return "ENFERMEDAD CRÓNICA"
    if sintomas <= 1 and presion < 130:
        return "NO ENFERMO"
    if sintomas <= 4 and presion < 140:
        return "ENFERMEDAD LEVE"
    return "ENFERMEDAD AGUDA"

def generar_dataset(n: int = 1000, output_path: Path = OUTPUT_PATH) -> Path:
    rng = np.random.default_rng(RANDOM_SEED)
    edades = rng.integers(18, 95, size=n)
    presiones = rng.integers(90, 205, size=n)
    sintomas = rng.integers(0, 11, size=n)
    labels = [clasificar_paciente(int(e), int(p), int(s)) for e, p, s in zip(edades, presiones, sintomas)]
    df = pd.DataFrame({"edad": edades, "presion": presiones, "sintomas": sintomas, "diagnostico": labels})
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")
    return output_path

if __name__ == "__main__":
    print(f"Dataset generado en: {generar_dataset()}")
