from utils.shell import run_command
from rich.console import Console

console = Console()

def run_setup():
    """Main function for environment setup."""
    console.print("[bold magenta]🛠 Starting basic Ubuntu setup...[/bold magenta]\n")
    
    run_command("sudo apt-get update", "Updating package lists")
    
    run_command(
        "sudo apt-get install -y git curl wget build-essential", 
        "Installing Git, curl, wget, and build tools"
    )
    
    console.print("[bold green]🎉 Basic setup completed![/bold green]")