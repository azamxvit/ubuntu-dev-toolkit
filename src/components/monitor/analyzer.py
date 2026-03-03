import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def get_color(percent: float) -> str:
    """Returns color based on resource load."""
    if percent < 60:
        return "green"
    elif percent < 85:
        return "yellow"
    else:
        return "red"

def generate_bar(percent: float, length: int = 20) -> str:
    """Generates a text-based progress bar."""
    filled = int(length * percent // 100)
    bar = "█" * filled + "░" * (length - filled)
    return f"[{get_color(percent)}]{bar}[/] {percent}%"

def get_advice(cpu: float, ram: float, disk: float) -> str:
    """Generates system recommendations based on metrics."""
    advice = []
    if cpu > 85:
        advice.append("[bold red]⚠️ CPU Overloaded![/bold red] Check heavy background processes (Docker, compilation).")
    if ram > 85:
        advice.append("[bold red]⚠️ Critical RAM shortage![/bold red] Close heavy IDEs or browser tabs.")
    if disk > 90:
        advice.append("[bold red]⚠️ Disk is almost full![/bold red] Run 'sudo apt autoremove' and clear cache.")
        
    if not advice:
        advice.append("[bold green]✅ System is running smoothly. No issues detected![/bold green]")
        
    return "\n".join(advice)

def run_monitor():
    """Main function to run system monitoring."""
    console.print("[bold blue]📊 Analyzing system resources...[/bold blue]\n")
    

    cpu_percent = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Resource", style="cyan", width=12)
    table.add_column("Usage", width=30)
    table.add_column("Details", justify="right")
    
    table.add_row(
        "CPU", 
        generate_bar(cpu_percent), 
        f"{psutil.cpu_count(logical=True)} Cores"
    )
    table.add_row(
        "RAM", 
        generate_bar(ram.percent), 
        f"{ram.used // (1024**2)}MB / {ram.total // (1024**2)}MB"
    )
    table.add_row(
        "Disk (/)", 
        generate_bar(disk.percent), 
        f"{disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB"
    )

    console.print(table)
    
    console.print("\n")
    advice_text = get_advice(cpu_percent, ram.percent, disk.percent)
    console.print(Panel(advice_text, title="💡 System Advice", expand=False, border_style="blue"))