@echo off
setlocal enabledelayedexpansion

:: Definir los colores (0A para verde, 0B para azul)
set GREEN=0A
set BLUE=0B

:: Función para la animación
:animate
set message=%1
set /a counter=0
:loop
set /a counter+=1
if %counter% gtr 3 set /a counter=0

if %counter%==0 (
    echo [   ] %message%
) else if %counter%==1 (
    echo [.  ] %message%
) else if %counter%==2 (
    echo [.. ] %message%
) else (
    echo [...] %message%
)
timeout /t 1 /nobreak >nul
goto loop

:: Ejecutar comandos con animación

:: Limpiar el proyecto
start "" /b cmd /c call :animate "Limpiando el proyecto" & set anim_pid=!pid!
dotnet clean >nul 2>&1
taskkill /F /PID !anim_pid! >nul 2>&1
color %GREEN%
echo [✔] Limpiando el proyecto completado
color

:: Compilar el proyecto
start "" /b cmd /c call :animate "Compilando el proyecto" & set anim_pid=!pid!
dotnet build >nul 2>&1
taskkill /F /PID !anim_pid! >nul 2>&1
color %GREEN%
echo [✔] Compilando el proyecto completado
color

:: Ejecutar el proyecto
start "" /b cmd /c call :animate "Ejecutando el proyecto" & set anim_pid=!pid!
dotnet run >nul 2>&1
taskkill /F /PID !anim_pid! >nul 2>&1
color %GREEN%
echo [✔] Ejecutando el proyecto completado
color

endlocal