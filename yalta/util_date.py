"""Parse plain text -> datetime.date object using Linux `date -d` utility."""

import subprocess
from datetime import date, datetime


def parse_date_str(date_str: str) -> date:
    """Uses 'date -d' Linux utility to parse plain text -> date object."""
    process = subprocess.run(
        ['date', '-d', date_str, '+%Y-%m-%d'],
        capture_output = True,
        text = True
    )
    if process.returncode != 0:
        raise ValueError('Invalid date expression')

    return datetime.fromisoformat(process.stdout.strip()).date()

