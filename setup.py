from setuptools import find_packages, setup

setup(
    name="none",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["typer[all]", "pyyaml"],
    entry_points={
        "console_scripts": [
            "none=none.__main__:main",
        ]
    },
)
