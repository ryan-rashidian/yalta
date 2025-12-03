"""This module contains filesystem path(s) used by this application."""

from pathlib import Path

APP_NAME = 'yalta'
DATA_FILE = 'tasks.json'


def ensure_file_exists(file_path: Path) -> None:
    """Checks if the data file exists. If not, it creates one."""
    if not file_path.exists():
        print(f'Creating new task file at: {file_path}')
        file_path.write_text('{}', encoding='UTF-8')


TASK_PATH = Path.home() / '.local' / 'share' / APP_NAME / DATA_FILE
ensure_file_exists(TASK_PATH)

