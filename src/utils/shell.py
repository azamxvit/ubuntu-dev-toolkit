import subprocess
from rich.console import Console

console = Console()

def run_command(command: str, description: str) -> bool:
    """Executes a system command and prints the result beautifully."""
    console.print(f"[bold cyan]⏳ {description}...[/bold cyan]")
    try:
        subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        console.print("[bold green]✅ Success![/bold green]\n")
        return True
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]❌ Error:[/bold red] {e.stderr}\n")
        return False