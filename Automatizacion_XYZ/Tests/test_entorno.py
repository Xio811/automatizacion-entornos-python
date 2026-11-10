import importlib.metadata


def test_dependencias_instaladas():
    dependencias = ["flask", "SQLAlchemy", "pytest"]

    for dependencia in dependencias:
        version = importlib.metadata.version(dependencia)
        assert version is not None


def test_operacion_basica():
    resultado = 10 + 5
    assert resultado == 15