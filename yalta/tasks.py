"""Task loading and saving."""

import json
from dataclasses import dataclass
from datetime import date, datetime

from yalta._paths import TASK_PATH


@dataclass
class Task:
    """PyCrastinate task container."""
    id: str
    description: str
    date: str
    status: bool = False

    @property
    def task_id(self) -> int:
        return int(self.id)

    @property
    def task_date(self) -> date:
        return datetime.fromisoformat(self.date).date()

    @property
    def is_complete(self) -> bool:
        return self.status

    def complete_toggle(self) -> None:
        """toggle task completion."""
        self.status = not self.status

    def to_dict(self) -> dict:
        """Convert Task to dictionary as intermediate for saving to JSON."""
        return {
            'description': self.description,
            'date': self.date,
            'status': self.status
        }


def _get_unique_id(tasks: list[Task]) -> int:
    """Calculate the next unique id value."""
    task_ids = sorted(task.task_id for task in tasks)
    next_id = 1
    for id in task_ids:
        if id == next_id:
            next_id += 1
        else:
            break
    return next_id


def add_new_task(description: str, date: date, tasks: list[Task]) -> Task:
    """Prompt the user for a new task."""
    return Task(
        id = str(_get_unique_id(tasks)),
        description = description,
        date = str(date)
    )


def split_tasks(tasks: list[Task]) -> tuple[list[Task], list[Task]]:
    """Split task list into active and inactive lists.

    'active' refers to incomplete and due tasks.
    'inactive' refers to the rest.

    Returns:
        tuple(active_list, inactive_list)
            - active_list: list[Task]
            - inactive_list: list[Task]

    """
    now = datetime.now().date()
    active_tasks = []
    inactive_tasks = []

    for task in tasks:
        if task.task_date <= now and not task.is_complete:
            active_tasks.append(task)
        else:
            inactive_tasks.append(task)

    return active_tasks, inactive_tasks


def load_task_json() -> dict:
    """Load from tasks JSON."""
    try:
        with open(TASK_PATH, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_task_json(tasks: dict) -> None:
    """Save to tasks JSON."""
    with open(TASK_PATH, 'w') as f:
        json.dump(tasks, f, indent=2)

