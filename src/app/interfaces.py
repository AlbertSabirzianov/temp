from abc import ABC, abstractmethod

from .schema import Directory


class ABCTemplateRepository(ABC):

    @abstractmethod
    def get_all_templates(self) -> list[Directory]:
        raise NotImplementedError

    @abstractmethod
    def save_new_template(self, name: str, temp: Directory) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete_template(self, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_template(self, name: str) -> Directory:
        raise NotImplementedError


class ABCTemplateService(ABC):

    @abstractmethod
    def get_template_from_absolute_path(self, path: str, name: str) -> Directory:
        raise NotImplementedError

    @abstractmethod
    def paste_template_to_path(self, path: str, template: Directory) -> None:
        raise NotImplementedError


class ABSUnitOfWorkService(ABC):

    @abstractmethod
    def ls(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def see(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def add(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rm(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def paste(self) -> None:
        raise NotImplementedError
