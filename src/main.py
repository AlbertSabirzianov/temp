"""
 - temp ls
 - temp add <name>
 - temp paste <name>
 - temp rm <name>
 - temp see <name>

 Create templates in json file and paste from it
"""
import argparse
import os
from typing import Callable

from app.enums import Commands
from app.interfaces import ABSUnitOfWorkService
from app.services import CommandUnitOfWork, TemplateService
from app.repositories import TemplateRepository
from app.exceptions import TemplateNotExists, NameRequiredException


COMMAND_LINE_PATH = os.getcwd()
MAIN_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_FILE_NAME = "temps_data.json"


def get_command_func_dict(
    unit_of_work: ABSUnitOfWorkService
) -> dict[Commands, Callable]:
    return {
        Commands.LS.value: unit_of_work.ls,
        Commands.ADD.value: unit_of_work.add,
        Commands.PASTE.value: unit_of_work.paste,
        Commands.RM.value: unit_of_work.rm,
        Commands.SEE.value: unit_of_work.see
    }


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

    template_service = TemplateService()
    template_repository = TemplateRepository(
        main_path=MAIN_PATH,
        json_file_name=JSON_FILE_NAME
    )

    unit_of_work = CommandUnitOfWork(
        template_repository=template_repository,
        template_service=template_service,
        command_path=COMMAND_LINE_PATH,
        name=args.name
    )

    command_dict = get_command_func_dict(unit_of_work)
    try:
        command_dict[args.command]()
    except NameRequiredException:
        print("name argument is required!")
    except TemplateNotExists:
        print(f"template with name {args.name} does not exists!")
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
