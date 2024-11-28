from enum import Enum


class Commands(Enum):
    LS = "ls"
    ADD = "add"
    PASTE = "paste"
    RM = "rm"
    SEE = "see"

    @classmethod
    def all_commands(cls) -> list[str]:
        return [command.value for command in cls]


class ErrorCodes(Enum):
    DIRECTORY_ALREADY_EXISTS = 17
