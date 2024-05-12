import argparse
from natural_shell.command_executor import execute_command, fetch_command
from natural_shell.language_model import llm

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

    args.func(args.input, llm.get_language_model())

def print_command(input, language_model):
    command = fetch_command(input, language_model)
    print(command)

def exec_command(input, language_model):
    command, output = execute_command(input, language_model)
    print(f"[+] executing: {command}")
    print(output)

if __name__ == "__main__":
    main()
