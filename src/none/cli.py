from pathlib import Path

import typer
from utils import create_structure, load_template

app = typer.Typer()


@app.command()
def fastapi(
    folder: str = typer.Option(
        ".", "-f", "--folder", help="Ruta donde crear el proyecto"
    )
):
    """Genera un proyecto FastAPI en el directorio actual o en uno nuevo con -f."""
    try:
        template = load_template("fastapi")

        # Si folder no existe aún, crealo
        folder_path = Path(folder)
        folder_path.mkdir(parents=True, exist_ok=True)

        create_structure(template, base_path=folder_path)
    except FileNotFoundError:
        typer.echo("❌ Plantilla 'fastapi' no encontrada.")
