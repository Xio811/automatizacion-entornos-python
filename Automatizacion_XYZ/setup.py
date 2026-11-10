from pathlib import Path
import subprocess
import sys


BASE_DIR = Path(__file__).resolve().parent
DEPENDENCIAS = ["flask", "SQLAlchemy", "pytest"]


def crear_carpetas():
    for carpeta in ["App", "Tests"]:
        (BASE_DIR / carpeta).mkdir(exist_ok=True)

    (BASE_DIR / "App" / "__init__.py").touch(exist_ok=True)
    print("Carpetas creadas correctamente.")


def crear_requirements():
    archivo = BASE_DIR / "requirements.txt"
    archivo.write_text("\n".join(DEPENDENCIAS) + "\n", encoding="utf-8")
    print("Archivo requirements.txt creado.")


def crear_readme():
    contenido = """# Proyecto XYZ

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
.\\dev_env\\Scripts\\Activate.ps1
```

En macOS o Linux:

```sh
source dev_env/bin/activate
```

## Ejecutar las pruebas

```sh
pytest
```
"""
    (BASE_DIR / "README.md").write_text(contenido, encoding="utf-8")
    print("Archivo README.md creado.")


def preparar_entorno():
    entorno = BASE_DIR / "dev_env"
    if not entorno.exists():
        subprocess.run([sys.executable, "-m", "venv", str(entorno)], check=True)

    if sys.platform == "win32":
        python_entorno = entorno / "Scripts" / "python.exe"
    else:
        python_entorno = entorno / "bin" / "python"

    print("Entorno virtual preparado.")
    subprocess.run(
        [
            str(python_entorno),
            "-m",
            "pip",
            "install",
            "-r",
            str(BASE_DIR / "requirements.txt"),
        ],
        check=True,
    )
    print("Dependencias instaladas correctamente.")


def main():
    crear_carpetas()
    crear_requirements()
    crear_readme()
    preparar_entorno()
    print("\nPROYECTO CONFIGURADO CORRECTAMENTE")


if __name__ == "__main__":
    main()
