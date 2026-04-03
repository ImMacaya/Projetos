import typer
from rich.console import Console
from rich.panel import Panel

app = typer.Typer(help="Sistema de Cadastro de Usuários (CLI) — SQLite + Typer + Rich")
console = Console()

@app.command()
def hello():
    """Comando de teste para validar o CLI."""
    console.print(Panel.fit("✅ CLI funcionando!", title="user-registry", border_style="green"))

def app_entry():
    app()

# Para permitir import seguro em __main__.py:
app = app