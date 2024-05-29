from app.builtins.echo_builtin import echo_builtin
from app.builtins.exit_builtin import exit_builtin
from app.utils import find_exec


def command_map() -> dict:
    return {
        "echo": echo_builtin,
        "exit": exit_builtin,
        "type": type_builtin
    }


def type_builtin(args):
    command = args[1] if len(args) > 1 else ""
    if command in command_map():
        print(f"{command} is a shell builtin")
    elif command_path := find_exec(command):
        print(f"{command} is {command_path}")
    else:
        print(f"{command} not found")


BUILTIN_MAP = command_map()

