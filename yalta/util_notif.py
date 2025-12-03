"""Notifications for YALTA.

Requires a notification daemon.
"""

import subprocess
from datetime import datetime

from yalta.tasks import Task


def notify(tasks: list[Task]) -> None:
    """Send system notification(s) for active tasks."""
    now = datetime.now().date()
    for task in tasks:
        if task.task_date <= now and not task.is_complete:
            subprocess.run(
                ["notify-send", f'Task ID: {task.id}', task.description]
            )

