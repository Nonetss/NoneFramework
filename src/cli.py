import typer
from utils import create_structure, load_template

app = typer.Typer()


@app.command()
def generate(plantilla: str):
    try:
        template = load_template(plantilla)
        create_structure(template)
    except FileNotFoundError:
        typer.echo(f"❌ Plantilla '{plantilla}' no encontrada.")


if __name__ == "__main__":
    app()
