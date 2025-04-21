from pathlib import Path

import yaml


def load_template(name: str):
    path = Path(__file__).parent / "templates" / f"{name}.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def create_structure(template, base_path="."):
    # Si el usuario pasó "." o una carpeta específica, usamos esa como base directa
    base = Path(base_path)

    for folder in template["folders"]:
        folder_path = base / folder
        folder_path.mkdir(parents=True, exist_ok=True)

    for file_path, content in template["files"].items():
        full_path = base / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"✅ Proyecto creado en: {base.resolve()}")
