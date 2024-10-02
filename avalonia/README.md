# PROYECTO DE AVALONIA

## SET UP
sudo apt remove --purge dotnet-sdk
sudo apt remove --purge dotnet-runtime

Actualizar e instalar los certificados:
- `sudo apt update`
- `sudo apt install -y apt-transport-https ca-certificates wget`

Descarga e instalación de los paquetes de Microsoft:
- `wget https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb`
- `sudo dpkg -i packages-microsoft-prod.deb`
- `sudo apt update`
- `sudo apt install -y dotnet-sdk-8.0`

Para comprobar que se ha instalado: `dotnet --version`
Comprobar los direcotrios:
- `ls -l /usr/bin/dotnet`
- `ls -l /usr/share/dotnet/`

Dar permisos a los directorios y contenido:
- `sudo chmod -R 755 /usr/share/dotnet/`
- `source ~/.bashrc`

Inicializar un proyecto de Avalonia:
- `dotnet new --install Avalonia.Templates`

## EJECUCCIÓN
- Para ejecutarlo: `dotnet clean`, `dotnet build` y `dotnet run`. O bien ejecutar el fichero `run.sh` para ejecutar las tres a la vez (Linux)
