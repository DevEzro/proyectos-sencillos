#!/bin/bash

# Función para la animación
animate() {
    message=$1  # Mensaje a mostrar
    
    # Mientras se ejecuten los comandos se hará la animación de los puntos
    # junto con el mensaje al lado
    while true
    do
        echo -ne "\033[0;34m[   ] $message\r" # '\033[0:34m' es el color Azul en ANSI (para darle color a los mensajes)
        sleep 0.33 # Espera 0.33 segundos entre animaciones
        echo -ne "\033[0;34m[.  ] $message\r"
        sleep 0.33
        echo -ne "\033[0;34m[.. ] $message\r"
        sleep 0.33
        echo -ne "\033[0;34m[...] $message\r"
        sleep 0.33
    done
}

# Animación para el comando 'dotnet clean'
animate "Limpiando el proyecto" &
clean_pid=$!
dotnet clean > /dev/null 2>&1
kill $clean_pid
echo -ne "\033[0;32m[✔] Limpiando el proyecto completado.\n" # '\033[0:34m' es el color Verde. Mismo caso que antes

# Animación para el comando 'dotnet build'
animate "Compilando el proyecto" &
build_pid=$!
dotnet build > /dev/null 2>&1
kill $build_pid
echo -ne "\033[0;32m[✔] Compilando el proyecto completado.\n"

# Animación para el comando 'dotnet run'
animate "Ejecutando el proyecto" &
run_pid=$!
dotnet run > /dev/null 2>&1
kill $run_pid
echo -ne "\033[0;32m[✔] Ejecutando el proyecto completado.\n"