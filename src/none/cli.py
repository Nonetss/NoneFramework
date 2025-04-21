from pathlib import Path

import typer

from none.utils.helper import create_structure, load_template

app = typer.Typer(help="Generador de proyectos")


@app.command()
def fastapi(
    folder: str = typer.Option(
        ".",
        "-f",
        "--folder",
        help="Ruta donde crear el proyecto (por defecto: directorio actual)",
    )
):
    """
    Genera un proyecto FastAPI en el directorio actual o en uno nuevo con -f.
    """
    try:
        tpl = load_template("fastapi")
        target = Path(folder)
        target.mkdir(parents=True, exist_ok=True)
        create_structure(tpl, base_path=target)
    except FileNotFoundError:
        typer.echo("❌ Plantilla 'fastapi' no encontrada.")
