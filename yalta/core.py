"""This module contains the core logic for YALTA."""


from yalta.format import print_tasks
from yalta.tasks import (
    Task,
    add_new_task,
    load_task_json,
    save_task_json,
    split_tasks,
)
from yalta.util_notif import notify


class YALTApp:
    """Main class for YALTA."""

    def __init__(self):
        """Initialize task list JSON."""
        self.tasks = [
            Task(id=id, **task) for id, task in load_task_json().items()
        ]

    def _save_tasks(self) -> None:
        """Save current task list."""
        save_task_json({task.id: task.to_dict() for task in self.tasks})

    def add_task(self, **kwargs) -> None:
        """Add a task to the list."""
        self.tasks.append(add_new_task(**kwargs))
        self._save_tasks()

    def briefing(self) -> None:
        """Output a briefing of current tasks to the terminal."""
        active_tasks, _ = split_tasks(self.tasks)
        print(
            f'{len(active_tasks)} active tasks. | '
            f'{len(self.tasks)} total tasks.'
        )

    def list_tasks(self) -> None:
        """List all current tasks."""
        print_tasks(self.tasks)

    def notify(self) -> None:
        """Send system notification(s) for active tasks."""
        notify(self.tasks)

    def remove_task(self, id: int) -> None:
        """Remove a task from the list."""
        for task in self.tasks:
            if task.task_id == id:
                self.tasks.remove(task)
                self._save_tasks()

    def mark_task(self, id: int) -> None:
        """Mark a task complete/incomplete."""
        for task in self.tasks:
            if task.task_id == id:
                task.complete_toggle()
                self._save_tasks()

