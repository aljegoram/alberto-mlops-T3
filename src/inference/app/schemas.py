from pydantic import BaseModel, Field

class PacienteInput(BaseModel):
    edad: int = Field(..., ge=0, le=120)
    presion: int = Field(..., ge=50, le=250)
    sintomas: int = Field(..., ge=0, le=10)

class PrediccionOutput(BaseModel):
    resultado: str
    fuente_modelo: str
    version_modelo: str
