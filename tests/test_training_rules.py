from src.data.generate_dataset import clasificar_paciente

def test_regla_no_enfermo():
    assert clasificar_paciente(25, 120, 0) == "NO ENFERMO"

def test_regla_terminal():
    assert clasificar_paciente(85, 190, 10) == "ENFERMEDAD TERMINAL"
