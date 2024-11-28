import os
from typing import Optional

from .exceptions import NameRequiredException
from .interfaces import ABSUnitOfWorkService, ABCTemplateService, ABCTemplateRepository
from .schema import Directory, File
from .utils import print_directory, read_file, is_directory, write_file, create_dir_if_not_exists


class TemplateService(ABCTemplateService):

    def get_template_from_absolute_path(self, path: str, name: str) -> Directory:
        current_directory: Directory = Directory(
            name=name,
            data=[]
        )
        for root, dirs, files in os.walk(path):
            for file in files:
                current_directory['data'].append(
                    File(
                        name=file,
                        data=read_file(os.path.join(root, file))
                    )
                )
            for dir in dirs:
                current_directory['data'].append(
                    self.get_template_from_absolute_path(
                        path=os.path.join(root, dir),
                        name=dir
                    )
                )
            return current_directory

    def paste_template_to_path(self, path: str, template: Directory) -> None:
        for obj in template['data']:
            if not is_directory(obj):
                write_file(
                    path=os.path.join(path, obj['name']),
                    data_to_write=obj['data']
                )
            else:
                create_dir_if_not_exists(os.path.join(path, obj['name']))
                self.paste_template_to_path(
                    path=os.path.join(path, obj['name']),
                    template=obj
                )


class CommandUnitOfWork(ABSUnitOfWorkService):

    def __init__(
        self,
        template_repository: ABCTemplateRepository,
        template_service: ABCTemplateService,
        command_path: str,
        name: Optional[str] = None
    ):
        self.template_repository = template_repository
        self.template_service = template_service
        self.command_line_path = command_path
        self.name = name

    def __check_name(self):
        if not self.name:
            raise NameRequiredException()

    def ls(self) -> None:
        temps = self.template_repository.get_all_templates()
        for temp in temps:
            print(temp['name'])

    def see(self) -> None:
        self.__check_name()
        temp = self.template_repository.get_template(self.name)
        print_directory(temp)

    def add(self) -> None:
        self.__check_name()
        new_temp = self.template_service.get_template_from_absolute_path(
            self.command_line_path,
            self.name
        )
        self.template_repository.save_new_template(
            name=self.name,
            temp=new_temp
        )
        print(f"Template {self.name} saved successfully!")

    def rm(self) -> None:
        self.__check_name()
        self.template_repository.delete_template(self.name)
        print(f"Template {self.name} removed successfully!")

    def paste(self) -> None:
        self.__check_name()
        temp = self.template_repository.get_template(self.name)
        self.template_service.paste_template_to_path(
            path=self.command_line_path,
            template=temp
        )
        print(f"Template {self.name} pasted successfully!")
