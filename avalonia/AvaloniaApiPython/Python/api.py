import platform, yaml, subprocess, platform
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# region -------------- API --------------
# Inicializa la API
app = FastAPI()

# Modelo de datos
class InstaladorRequest(BaseModel):
    sistema_operativo: str
    fuentes: list

# Endpoint para generar el instalador
#   - Prueba a llamar al método generar instalador pasando los argumentos de SO y fuentes
@app.post("/generar_instalador/")
def generar_instalador_endpoint(request: InstaladorRequest):
    try:
        resultado = generar_instalador(request.sistema_operativo, request.fuentes)
        return {"mensaje": "Instalador generado correctamente", "archivo": resultado}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# endregion

# PROVISIONAL
# region ------ GENERA INSTALADOR --------
# Genera el archivo winlogbeat.yml
def generar_archivo_configuracion(fuentes):
    # Estructura para Winlogbeat en Windows
    config = {
        'winlogbeat': {
            'event_logs': [{'name': fuente} for fuente in fuentes]
        }
    }

    # Guarda en un archivo YAML
    with open('winlogbeat.yml', 'w') as file:
        yaml.dump(config, file)

    print("Archivo 'winlogbeat.yml' generado con éxito.")

# Lista de fuentes de eventos
fuentes_ingesta = ["Application", "Security", "System"]
generar_archivo_configuracion(fuentes_ingesta)

def generar_instalador(os_sistema, fuentes):
    # Archivo de configuración YAML
    generar_archivo_configuracion(fuentes)

    # Genera el instalador para windows y linux
    if os_sistema.lower() == 'windows':
        # Pyinstaller para crear el agente
        subprocess.run(['pyinstaller', '--onefile', '--add-data', 'winlogbeat.yml;.', 'agente.py'])
        print("Instalador para Windows generado con éxito.")
        return 'dist/agente.exe'

    elif os_sistema.lower() == 'linux':
        print("Instalador para Linux aún no implementado.")
        return None

    else:
        raise ValueError("Sistema operativo no soportado.")

# Detectar el sistema operativo y generar instalador
os_sistema = platform.system()
fuentes_ingesta = ["Application", "Security", "System"]

generar_instalador(os_sistema, fuentes_ingesta)
# endregion