from pathlib import Path

from none.utils.helper import create_structure, load_template


def fastapi(folder: str = "."):
    """
    Genera un proyecto FastAPI en la carpeta actual o en una nueva con -f.
    """
    try:
        tpl = load_template("fastapi")
        target = Path(folder)
        target.mkdir(parents=True, exist_ok=True)
        create_structure(tpl, base_path=target)
    except FileNotFoundError:
        typer.echo("❌ Plantilla 'fastapi' no encontrada.")
