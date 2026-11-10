# Proyecto XYZ

Proyecto base para la automatización XYZ.
 ## Instalación del proyecto

1. Tener Python instalado.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```powershell
python setup.py
```

Este comando crea automáticamente el entorno virtual,
las carpetas del proyecto e instala las dependencias.
## Estructura

- `App/`: código de la aplicación.
- `Tests/`: pruebas automatizadas.
- `dev_env/`: entorno virtual de Python.

## Activar el entorno virtual

En Windows:

```powershell
.\dev_env\Scripts\Activate.ps1
```

En macOS o Linux:

```sh
source dev_env/bin/activate
```

## Ejecutar las pruebas

```sh
pytest
```
