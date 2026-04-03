import os
import time
import subprocess
import threading
from datetime import datetime
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ======= CONFIG =======
DEBOUNCE_SECONDS = 2.0          # espera um pouco após o último save
AUTO_PUSH = True               # True: já faz push pro GitHub
BRANCH = None                  # None: usa branch atual | "autosave": força branch
COMMIT_PREFIX = "autosave"     # prefixo do commit
# ======================

IGNORED_DIRS = {".git", ".venv", "venv", "__pycache__", "build", "dist"}
IGNORED_SUFFIXES = {".pyc", ".pyo", ".log"}
IGNORED_FILES = {"Thumbs.db"}

def run(cmd):
    """Executa comando e retorna (returncode, stdout)."""
    p = subprocess.run(cmd, capture_output=True, text=True, shell=False)
    return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()

def in_repo_root():
    code, out, err = run(["git", "rev-parse", "--is-inside-work-tree"])
    return code == 0 and out.strip() == "true"

def has_staged_changes():
    # returncode 1 => há diferenças staged, 0 => não há
    code, _, _ = run(["git", "diff", "--cached", "--quiet"])
    return code == 1

def has_worktree_changes():
    code, out, _ = run(["git", "status", "--porcelain"])
    return code == 0 and bool(out.strip())

def checkout_branch_if_needed():
    if BRANCH:
        # cria branch se não existir
        run(["git", "checkout", "-B", BRANCH])

def do_commit_and_push(changed_path=None):
    if not in_repo_root():
        return

    # Se não houver mudanças no working tree, nem faz add
    if not has_worktree_changes():
        return

    checkout_branch_if_needed()

    run(["git", "add", "-A"])

    if not has_staged_changes():
        return

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_hint = f" ({Path(changed_path).name})" if changed_path else ""
    msg = f"{COMMIT_PREFIX}: {ts}{file_hint}"

    run(["git", "commit", "-m", msg])

    if AUTO_PUSH:
        run(["git", "push"])

class DebouncedHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self._timer = None
        self._lock = threading.Lock()
        self._last_path = None

    def _schedule(self):
        with self._lock:
            if self._timer:
                self._timer.cancel()
            self._timer = threading.Timer(DEBOUNCE_SECONDS, do_commit_and_push, args=(self._last_path,))
            self._timer.daemon = True
            self._timer.start()

    def on_any_event(self, event):
        if event.is_directory:
            return

        src = event.src_path.replace("\\", "/")

        # Ignora arquivos temporários e coisas comuns do Windows/editores
        name = os.path.basename(src)
        if name in IGNORED_FILES:
            return
        if any(src.endswith(suf) for suf in IGNORED_SUFFIXES):
            return
        if "/.git/" in src or src.endswith("/.git"):
            return
        if any(f"/{d}/" in src for d in IGNORED_DIRS):
            return

        # Guarda o último caminho alterado (apenas para mensagem)
        self._last_path = src

        # Agenda commit/push com debounce
        self._schedule()

def main():
    if not in_repo_root():
        print("❌ Este diretório não parece ser um repositório git. Rode dentro do seu projeto.")
        return

    print("✅ Monitorando mudanças. Salvou arquivo → commit → push (com debounce).")
    print(f"   Debounce: {DEBOUNCE_SECONDS}s | Auto push: {AUTO_PUSH} | Branch: {BRANCH or '(atual)'}")
    print("   Pressione Ctrl+C para parar.")

    observer = Observer()
    handler = DebouncedHandler()
    observer.schedule(handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()