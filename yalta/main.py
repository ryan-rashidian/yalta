"""Main module for running YALTA."""

from datetime import datetime

from yalta.core import YALTApp
from yalta.parse_args import parser


def main():
    """Main function for running YALTA in the terminal."""
    args = parser.parse_args()
    app = YALTApp()

    if args.add:
        date = args.date if args.date else datetime.now().date()
        app.add_task(description=args.add, date=date, tasks=app.tasks)

    elif args.list:
        app.list_tasks()

    elif args.mark:
        app.mark_task(args.mark)

    elif args.notif:
        app.notify()

    elif args.remove:
        app.remove_task(args.remove)

    else:
        app.briefing()

