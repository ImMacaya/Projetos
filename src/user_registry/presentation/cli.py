import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from user_registry.repository.sqlite_repo import SQLiteUserRepository
from user_registry.service.user_service import UserService

app = typer.Typer(help="Cadastro de Usuários — SQLite + Typer + Rich")
console = Console()

def _service() -> UserService:
    repo = SQLiteUserRepository()
    return UserService(repo)

@app.command()
def create(
    name: str = typer.Option(..., "--name", "-n", help="Nome completo"),
    email: str = typer.Option(..., "--email", "-e", help="Email do usuário"),
    password: str = typer.Option(None, "--password", "-p", help="Senha (se não informar, será perguntada)"),
):
    """Cria um novo usuário."""
    svc = _service()
    try:
        if password is None:
            password = Prompt.ask("Senha", password=True)
        svc.create_user(name=name, email=email, password=password)
        console.print(Panel.fit("✅ Usuário criado com sucesso!", title="create", border_style="green"))
    except Exception as ex:
        console.print(Panel.fit(f"❌ Erro: {ex}", title="create", border_style="red"))
        raise typer.Exit(code=1)

@app.command("list")
def list_users():
    """Lista usuários cadastrados."""
    svc = _service()
    users = svc.list_users()
    table = Table(title="Usuários", header_style="bold cyan")
    table.add_column("Nome")
    table.add_column("Email")
    table.add_column("Ativo", justify="center")
    table.add_column("Criado em")

    for u in users:
        table.add_row(u.name, u.email, "✅" if u.is_active else "⛔", u.created_at)

    console.print(table)

@app.command()
def show(email: str = typer.Option(..., "--email", "-e", help="Email do usuário")):
    """Mostra detalhes de um usuário."""
    svc = _service()
    user = svc.repo.get_by_email(email.strip().lower())
    if not user:
        console.print(Panel.fit("❌ Usuário não encontrado.", title="show", border_style="red"))
        raise typer.Exit(code=1)

    console.print(Panel.fit(
        f"[bold]Nome:[/bold] {user.name}\n"
        f"[bold]Email:[/bold] {user.email}\n"
        f"[bold]Ativo:[/bold] {'Sim' if user.is_active else 'Não'}\n"
        f"[bold]Criado em:[/bold] {user.created_at}\n"
        f"[bold]Atualizado em:[/bold] {user.updated_at}",
        title="Detalhes do Usuário",
        border_style="blue",
    ))

@app.command()
def update(
    email: str = typer.Option(..., "--email", "-e", help="Email do usuário"),
    name: str = typer.Option(..., "--name", "-n", help="Novo nome"),
):
    """Atualiza o nome do usuário."""
    svc = _service()
    try:
        svc.update_name(email=email, new_name=name)
        console.print(Panel.fit("✅ Nome atualizado!", title="update", border_style="green"))
    except Exception as ex:
        console.print(Panel.fit(f"❌ Erro: {ex}", title="update", border_style="red"))
        raise typer.Exit(code=1)

@app.command()
def deactivate(email: str = typer.Option(..., "--email", "-e", help="Email do usuário")):
    """Desativa um usuário."""
    svc = _service()
    try:
        svc.deactivate(email=email)
        console.print(Panel.fit("✅ Usuário desativado.", title="deactivate", border_style="yellow"))
    except Exception as ex:
        console.print(Panel.fit(f"❌ Erro: {ex}", title="deactivate", border_style="red"))
        raise typer.Exit(code=1)

@app.command()
def activate(email: str = typer.Option(..., "--email", "-e", help="Email do usuário")):
    """Ativa um usuário."""
    svc = _service()
    try:
        svc.activate(email=email)
        console.print(Panel.fit("✅ Usuário ativado.", title="activate", border_style="green"))
    except Exception as ex:
        console.print(Panel.fit(f"❌ Erro: {ex}", title="activate", border_style="red"))
        raise typer.Exit(code=1)

@app.command()
def login(
    email: str = typer.Option(..., "--email", "-e", help="Email do usuário"),
    password: str = typer.Option(None, "--password", "-p", help="Senha (se não informar, será perguntada)"),
):
    """Valida login (MVP): retorna OK ou erro."""
    svc = _service()
    if password is None:
        password = Prompt.ask("Senha", password=True)

    ok = svc.login(email=email, password=password)
    if ok:
        console.print(Panel.fit("✅ Login OK", title="login", border_style="green"))
    else:
        console.print(Panel.fit("❌ Credenciais inválidas ou usuário inativo.", title="login", border_style="red"))
        raise typer.Exit(code=1)