import sys


def exit_builtin(args):
    code_arg = args[1] if len(args) > 1 else "0"
    if not code_arg.isdigit():
        print("exit: numeric argument required")
        return
    code = int(code_arg)
    sys.exit(code)

