"""Format terminal output for YALTA."""

from yalta.tasks import Task


def _print_task(task: Task) -> None:
    """Print a task to the terminal with formatting."""
    empty = '\u2610'
    checked = '\u2611'
    status = checked if task.status else empty
    print(f' {status} | {task.task_id:02d} | {task.date} | {task.description}')


def print_tasks(tasks: list[Task]) -> None:
    """Print all tasks to terminal with formatting."""
    if not tasks:
        print('No tasks.')
        return

    sorted_tasks = sorted(tasks, key=lambda t: t.task_date)
    print(' \u2611 | ID | YYYY-MM-DD | Task')
    print('-' * 28)
    for task in sorted_tasks:
        _print_task(task)
    print('-' * 28)

