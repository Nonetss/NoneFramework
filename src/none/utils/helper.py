from pathlib import Path

import yaml


def load_template(name: str):
    path = Path(__file__).parent.parent / "templates" / f"{name}.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def create_structure(template, base_path="."):
    base = Path(base_path)
    # creamos carpetas
    for folder in template["folders"]:
        (base / folder).mkdir(parents=True, exist_ok=True)
    # creamos archivos con contenido
    for file_path, content in template["files"].items():
        full = base / file_path
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(content, encoding="utf-8")
    print(f"✅ Proyecto creado en: {base.resolve()}")
