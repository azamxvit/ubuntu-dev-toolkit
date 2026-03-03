import click
from rich.console import Console
from components.setup.installer import run_setup
from components.monitor.analyzer import run_monitor
from components.package_deps.analyzer import run_deps

console = Console()

@click.group()
def cli():
    """Ubuntu Dev Toolkit - Swiss Army knife for developers."""
    pass

@cli.command()
def setup():
    """Automated environment setup (VS Code, Docker, Git)."""
    run_setup()

@cli.command()
def monitor():
    """System resources monitoring (CPU, RAM, Network)."""
    run_monitor()
    console.print("[bold blue]📊 Starting system monitoring...[/bold blue]")
    console.print("Graphs and recommendations will be here soon.")

@cli.command()
@click.argument('package_name')
def deps(package_name):
    """Package dependency analysis (Synaptic plugin alternative)."""
    run_deps(package_name)
    console.print(f"[bold yellow]📦 Analyzing dependencies for package:[/bold yellow] [bold white]{package_name}[/bold white]")
    console.print("Dependency tree will be built here soon.")

if name == '__main__':
    cli()