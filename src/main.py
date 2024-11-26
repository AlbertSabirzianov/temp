"""
 - temp ls
 - temp add <name>
 - temp paste <name>
 - temp rm <name>
 - temp see <name>

 Create templates in json file and paste from it
"""
import argparse

from app.enums import Commands


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Command-line app for working with templates",
        prog="temp"
    )
    parser.add_argument(
        "command",
        choices=Commands.all_commands(),
        help="Command"
    )
    parser.add_argument(
        "name",
        nargs='?',
        help="name of template"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Command {args.command} {type(args.command)}")
    print(f"Name {args.name} {type(args.name)}")


if __name__ == '__main__':
    main()
