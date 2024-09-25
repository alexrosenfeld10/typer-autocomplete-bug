from typing import Optional

import typer
from typing_extensions import Annotated

app = typer.Typer()

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise typer.Exit()


def complete_name(incomplete: str):
    valid_names = [
        "start-test-exmpl",
        "start1234-other-exmpl",
        "start1234-test-exmpl",
    ]
    return [name for name in valid_names if name.startswith(incomplete)]


@app.command()
def main(
    name: Annotated[
        str, typer.Option(help="The name to say hi to.", autocompletion=complete_name)
    ] = "World",
    version: Annotated[
        Optional[bool], typer.Option("--version", callback=version_callback)
    ] = None,
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
