from typing import TypedDict, Union


class NamedDict(TypedDict):
    name: str


class File(NamedDict):
    data: str


class Directory(NamedDict):
    data: list[Union[File, "Directory"]]



