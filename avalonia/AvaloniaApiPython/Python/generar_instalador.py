import yaml, subprocess, platform, platform

def generar_archivo_configuracion(fuentes):
    # Creamos una estructura de configuración para Winlogbeat en Windows
    config = {
        'winlogbeat': {
            'event_logs': [{'name': fuente} for fuente in fuentes]
        }
    }

    # Guardamos la configuración en un archivo YAML
    with open('winlogbeat.yml', 'w') as file:
        yaml.dump(config, file)

    print("Archivo 'winlogbeat.yml' generado con éxito.")

# Lista de fuentes de eventos (puedes modificarla para adaptarla a lo que necesites)
fuentes_eventos = ["Application", "Security", "System"]
generar_archivo_configuracion(fuentes_eventos)

def generar_instalador(os_sistema, fuentes):
    # Generar el archivo de configuración YAML
    generar_archivo_configuracion(fuentes)

    if os_sistema.lower() == 'windows':
        # Aquí puedes usar herramientas como NSIS, Inno Setup o pyinstaller para empaquetar el instalador
        # En este ejemplo usaremos pyinstaller para simplificar
        subprocess.run(['pyinstaller', '--onefile', '--add-data', 'winlogbeat.yml;.', 'agente.py'])
        print("Instalador para Windows generado con éxito.")
        return 'dist/agente.exe'

    elif os_sistema.lower() == 'linux':
        # En Linux, podrías crear un paquete .deb o .rpm usando herramientas como dpkg o fpm
        # Este ejemplo es solo ilustrativo
        print("Instalador para Linux aún no implementado.")
        return None

    else:
        raise ValueError("Sistema operativo no soportado.")

# Detectar el sistema operativo y generar instalador
os_sistema = platform.system()
fuentes_eventos = ["Application", "Security", "System"]
generar_instalador(os_sistema, fuentes_eventos)
