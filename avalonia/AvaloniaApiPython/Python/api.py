from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import platform, generar_instalador
from generar_instalador import *

app = FastAPI()

# Modelo de datos para la solicitud
class InstaladorRequest(BaseModel):
    sistema_operativo: str
    fuentes: list

# Endpoint para generar el instalador
@app.post("/generar_instalador/")
def generar_instalador_endpoint(request: InstaladorRequest):
    try:
        resultado = generar_instalador(request.sistema_operativo, request.fuentes)
        return {"mensaje": "Instalador generado correctamente", "archivo": resultado}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
