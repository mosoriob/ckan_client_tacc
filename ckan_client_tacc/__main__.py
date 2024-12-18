import typer
from rich.console import Console

from ckan_client_tacc import admin_subcommand, version

app = typer.Typer(
    name="ckan-client-tacc",
    help="CKAN Client TACC is a Python package designed to manage the CKAN instance of TACC",
    add_completion=False,
)

app.add_typer(
    admin_subcommand.app,
    name="admin",
    help="Manage the CKAN instance of TACC",
)

console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]datafest-archive[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


if __name__ == "__main__":
    app()
