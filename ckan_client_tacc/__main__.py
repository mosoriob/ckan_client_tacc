import typer
from rich.console import Console

from ckan_client_tacc import (
    dataset_subcommand,
    organization_subcommand,
    user_subcommand,
    version,
)

app = typer.Typer(
    name="ckan-client-tacc",
    help="CKAN Client TACC is a Python package designed to manage the CKAN instance of TACC",
    add_completion=False,
)

app.add_typer(
    user_subcommand.app,
    name="users",
    help="Manage the users of TACC data discovery",
)

app.add_typer(
    organization_subcommand.app,
    name="organization",
    help="Manage the organizations of TACC data discovery",
)

app.add_typer(
    dataset_subcommand.app,
    name="dataset",
    help="Manage the datasets of TACC data discovery",
)

console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]datafest-archive[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


if __name__ == "__main__":
    app()
