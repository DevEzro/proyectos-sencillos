# PROYECTO DE AVALONIA

## SET UP

Actualización e instalación de los certificados:
- `sudo apt update`
- `sudo apt install -y apt-transport-https ca-certificates wget`

Descarga de los paquetes de microsoft:
- `wget https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb`
- `sudo dpkg -i packages-microsoft-prod.deb`

Actualización e instalación de .NET:
- `sudo apt update`
- `sudo apt install -y dotnet-sdk-8.0`

Comprobar que se ha instalado correctamente y las rutas:
- `dotnet --version`
- `ls -l /usr/bin/dotnet`
- `ls -l /usr/share/dotnet/`

Dar permisos:
- `sudo chmod -R 755 /usr/share/dotnet/`
- `source ~/.bashrc`

Instalar las plantillas:
- `dotnet new --install Avalonia.Templates`

Inicializar un proyecto de Avalonia:
- `dotnet new --install avalonia.app - MiProyecto`


## EJECUCCIÓN
- Para ejecutar las pruebas: `dotnet clean`, `dotnet build` y `dotnet run`. O bien se pueden usar los ficheros run.sh (Linux) y run.bat (Windows) para ejecutar los tres a la vez.

## ERRORES (Linux)
- Puede pasar que, al pulsar sobre la imagen para la redirección a GitHub la consola muestre este error: `Error: Failed to open Wayland display, fallback to X11. WAYLAND_DISPLAY='wayland-0' DISPLAY=':0'
- A pesar de que funciona, si es un error que no quieres ver en la consola, modifica el fichero `/etc/gdm3/custom.conf`, desmutea la linea `#WaylandEnable=false` y reinicia el equipo.
