import os
from typing import Union

from .schema import Directory, File
from .enums import ErrorCodes


def print_directory(directory: Directory, indent: int = 0):
    for obj in directory['data']:
        if isinstance(obj['data'], str):
            print(" "*indent + obj['name'])
        else:
            print()
            print(obj['name'])
            print_directory(obj, indent + 4)


def read_file(path: str) -> str:
    with open(path, encoding='utf-8', errors='ignore') as file:
        return file.read()


def write_file(path: str, data_to_write: str) -> None:
    with open(path, 'w+') as file:
        file.write(data_to_write)


def is_directory(data: Union[Directory, File]) -> bool:
    if isinstance(data['data'], list):
        return True
    return False


def create_dir_if_not_exists(path: str) -> None:
    try:
        os.mkdir(path)
    except OSError as e:
        if e.errno == ErrorCodes.DIRECTORY_ALREADY_EXISTS:
            return
        raise

