import argparse
from natural_shell.command_executor import execute_command
from natural_shell.language_model import get_language_model

def main():
    parser = argparse.ArgumentParser(description="Convert natural language input to shell commands")
    parser.add_argument("input", help="The natural language input")
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to execute")

    print_parser = subparsers.add_parser("print", help="Print the shell command")
    print_parser.set_defaults(func=print_command)

    exec_parser = subparsers.add_parser("exec", help="Execute the shell command")
    exec_parser.set_defaults(func=exec_command)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    llm = get_language_model()
    command = execute_command(args.input, llm)
    if command:
        args.func(command)

def print_command(command):
    print(command)

def exec_command(command):
    import os
    print(f"[+]executing: {command}")
    os.system(command)

if __name__ == "__main__":
    main()
