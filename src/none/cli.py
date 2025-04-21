# src/none/cli.py

import argparse

from none.commands.fastapi import fastapi


def main():
    """
    Generador de proyectos CLI (subcomando: fastapi).
    """
    parser = argparse.ArgumentParser(prog="none", description="Generador de proyectos")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcomando 'fastapi'
    fastapi_parser = subparsers.add_parser(
        "fastapi",
        help="Genera un proyecto FastAPI en la carpeta actual o en una nueva con -f",
    )
    fastapi_parser.add_argument(
        "-f",
        "--folder",
        type=str,
        default=".",
        help="Carpeta donde crear el proyecto (por defecto: directorio actual)",
    )

    args = parser.parse_args()

    if args.command == "fastapi":
        fastapi(args.folder)
    else:
        parser.print_help()
