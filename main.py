import typer
from typing_extensions import Annotated

app = typer.Typer()


def complete_name(incomplete: str):
    valid_names = [
        "start-test-exmpl",
        "start1234-other-exmpl",
        "start1234-test-exmpl",
    ]
    return [name for name in valid_names if name.startswith(incomplete)]

@app.command()
def main(name: Annotated[str, typer.Option(
    help="The name to say hi to.",
    autocompletion=complete_name
)] = "World"):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
