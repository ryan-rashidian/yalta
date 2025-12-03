"""Parsing for terminal arguments using argparse."""

import argparse

from yalta.util_date import parse_date_str

parser = argparse.ArgumentParser(
    prog = 'YALTA',
    description = 'Schedule a task.'
)

parser.add_argument(
    '-a', '--add',
    type = str,
    help = 'Add a new task to the list.'
)
parser.add_argument(
    '-d', '--date',
    type = parse_date_str,
    help = 'Specify the due date for a new task.'
)
parser.add_argument(
    '-l', '--list',
    action = 'store_true',
    help = 'Output a list of all current tasks.'
)
parser.add_argument(
    '-m', '--mark',
    type = int,
    help = 'Mark a task as complete/incomplete.'
)
parser.add_argument(
    '-n', '--notif',
    action = 'store_true',
    help = 'Send active tasks to Linux system notifications.'
)
parser.add_argument(
    '-rm', '--remove',
    type = int,
    help = 'Remove a task from the list.'
)

