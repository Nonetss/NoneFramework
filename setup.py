from setuptools import setup

setup(
    name="none",
    version="0.1",
    packages=["none"],
    install_requires=["typer[all]"],
    entry_points={
        "console_scripts": [
            "none=none.__main__:app",
        ]
    },
)
