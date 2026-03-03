import platform
import subprocess
from rich.console import Console
from rich.tree import Tree

console = Console()

def get_dependencies(package: str):
    # Проверяем систему
    if platform.system() == "Windows":
        return ["python-core", "shared-libs", "win-api-bridge"]
    
    try:
        output = subprocess.check_output(["apt-cache", "depends", package], text=True, stderr=subprocess.DEVNULL)
        deps = [line.strip().split(" ")[-1] for line in output.split("\n") if "Depends:" in line]
        return list(set(deps))
    except:
        return None

def run_deps(package_name: str):
    console.print(f"[bold cyan]📦 Package analysis for: '{package_name}'[/bold cyan]")
    deps = get_dependencies(package_name)
    
    if deps:
        tree = Tree(f"[bold blue]📦 {package_name}[/bold blue]")
        for d in deps:
            tree.add(f"[green]└─> {d}[/green]")
        console.print(tree)
    else:
        console.print("[red]❌ Not supported on this OS or package not found[/red]")