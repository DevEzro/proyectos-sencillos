from fastapi import FastAPI
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
            "message": f"Proyecto '{nombre_proyecto}' creado con éxito en {ruta_destino}",
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
