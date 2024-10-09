import yaml, subprocess, platform, platform

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
fuentes_eventos = ["Application", "Security", "System"]
generar_archivo_configuracion(fuentes_eventos)

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
fuentes_eventos = ["Application", "Security", "System"]
generar_instalador(os_sistema, fuentes_eventos)
