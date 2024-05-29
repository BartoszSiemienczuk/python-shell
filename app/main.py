import sys
import os
from app.builtins import BUILTIN_MAP
from app.utils import find_exec


def main():
    while True:
        handle_command()


def handle_command():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    args = input().split()
    command = args[0]

    match command:
        case _ if command in BUILTIN_MAP:
            BUILTIN_MAP[command](args)
        case _ if exec_path := find_exec(command):
            try:
                with os.popen(" ".join([exec_path] + args[1:])) as pipe:
                    print(pipe.read(), end="")
            except Exception as e:
                print(f"{command} failed with error: {e}")
        case _:
            command_not_found(command)


def command_not_found(command):
    print(f"{command}: command not found")


if __name__ == "__main__":
    main()
