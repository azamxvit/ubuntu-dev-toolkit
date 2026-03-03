import os
from utils.shell import run_command
from rich.console import Console

console = Console()

def run_setup():
    """Main function for environment setup."""
    console.print("[bold magenta]🛠 Starting comprehensive Ubuntu setup...[/bold magenta]\n")
    
    run_command("sudo apt-get update", "Updating package lists")
    
    run_command(
        "sudo apt-get install -y git curl wget build-essential apt-transport-https ca-certificates", 
        "Installing core tools (Git, curl, wget, build-essential)"
    )
    run_command("sudo apt-get install -y docker.io", "Installing Docker")
    
    current_user = os.environ.get('USER', 'root')
    run_command(f"sudo usermod -aG docker {current_user}", f"Adding {current_user} to docker group")
    run_command("sudo systemctl enable --now docker", "Starting Docker service")
    
    run_command("sudo snap install --classic code", "Installing Visual Studio Code")
    
    console.print("\n[bold green]🎉 Environment setup successfully completed![/bold green]")
    console.print("[yellow]Note: You might need to restart your terminal or log out/log in for Docker group changes to take effect.[/yellow]")