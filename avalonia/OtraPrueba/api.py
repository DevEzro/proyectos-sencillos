from fastapi import FastAPI
from pydantic import BaseModel
import yaml
import subprocess
import os

app = FastAPI()

@app.post("/crear-proyecto/")
def crear_proyecto(nombre_proyecto: str, ruta_destino: str):
    # Cambiar a la ruta destino donde se creará el proyecto
    try:
        os.chdir(ruta_destino)
        # Comando para crear el proyecto de Avalonia
        comando = ["dotnet", "new", "avalonia.mvvm", "-n", nombre_proyecto]

        # Ejecutar el comando
        resultado = subprocess.run(comando, check=True, capture_output=True, text=True)
        
        return {
            "message": f"Proyecto '{nombre_proyecto}' creado con éxito (revisar la ruta indicada))",
            "output": resultado.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "error": f"Error al crear el proyecto: {e}",
            "details": e.stderr
        }
    except FileNotFoundError as e:
        return {
            "error": f"La ruta destino no existe: {ruta_destino}",
            "details": str(e)
        }
    
class InstaladorRequest(BaseModel):
    sistema_operativo: str
    fuentes: list[str]
    ruta_instalador: str

# Endpoint para generar el instalador con fuentes configuradas
@app.post("/generar-instalador/")
def generar_instalador(instalador_data: InstaladorRequest):
    sistema_operativo = instalador_data.sistema_operativo
    fuentes = instalador_data.fuentes
    ruta_instalador = instalador_data.ruta_instalador

    if sistema_operativo.lower() == "windows":
        # Ruta del archivo winlogbeat.yml
        ruta_winlogbeat = os.path.join(ruta_instalador, "winlogbeat.yml")

        # Configurar las fuentes en el archivo winlogbeat.yml
        configuracion = {
            'winlogbeat.event_logs': [{'name': fuente} for fuente in fuentes]
        }

        try:
            # Escribir la configuración en el archivo winlogbeat.yml
            with open(ruta_winlogbeat, 'w') as archivo_yml:
                yaml.dump(configuracion, archivo_yml)
            return {
                "message": f"Instalador generado correctamente en {ruta_instalador}",
                "detalles": configuracion
            }
        except Exception as e:
            return {"error": f"Error al generar el instalador: {e}"}
    else:
        return {"error": f"Generación de instaladores no implementada para {sistema_operativo}"}
