# YALTA (Yet Another Linux To-Do-List App)

Simple to-do-list terminal application using Python standard library and Linux utilities.

---

## Purpose

Because re-inventing the wheel is all I ever wanted to do as a child.

But seriously: This project is for fun/learning purposes, not intended for supporting actual users. I use it mainly for sending system notifications immediately after my DE loads.

## Installation

This app includes a feature that uses the `notify-send` utility - which requires a notification daemon to be installed and enabled on your system. It also uses the `date` utility - which should come pre-installed with most Linux distributions.

### Install with pipx (recommended)

```bash
pipx install git+https://github.com/ryan-rashidian/yalta.git
```

### Manual Installation

```bash
# Clone the repo
git clone https://github.com/ryan-rashidian/yalta.git
cd yalta

# Create a new venv
python -m venv .venv
source .venv/bin/activate

# Make the script executable
chmod +x yalta_script.py

# Add it to PATH (example)
ln -s $(pwd)/yalta_script.py ~/.local/bin/yalta
```

## Usage

YALTA will create a JSON data file: `~/.local/share/yalta/tasks.json` on your
system when it runs for the first time. This is where to-do-list tasks are read
and written from.

```bash
yalta -h # To list command options and descriptions
```

