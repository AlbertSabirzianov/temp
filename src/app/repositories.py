import json
import os.path

from .exceptions import TemplateNotExists
from .interfaces import ABCTemplateRepository
from .schema import Directory


class TemplateRepository(ABCTemplateRepository):

    def __write_templates_to_file(self, templates: list[Directory]):
        with open(self.json_file_path, 'w+') as file:
            json.dump(templates, file, indent=4)

    def __init__(
        self,
        main_path: str,
        json_file_name: str
    ):
        self.json_file_path: str = os.path.join(
            main_path,
            json_file_name
        )
        if not os.path.exists(
            self.json_file_path
        ):
            self.__write_templates_to_file([])

    def get_all_templates(self) -> list[Directory]:
        with open(self.json_file_path) as file:
            return json.load(file)

    def save_new_template(self, name: str, temp: Directory) -> None:
        temp['name'] = name
        templates = self.get_all_templates()
        templates.append(temp)
        self.__write_templates_to_file(templates)

    def delete_template(self, name: str) -> None:
        templates = self.get_all_templates()
        for index, temp in enumerate(templates):
            if temp['name'] == name:
                del templates[index]
                self.__write_templates_to_file(templates)
                return
        raise TemplateNotExists

    def get_template(self, name: str) -> Directory:
        templates = self.get_all_templates()
        for index, temp in enumerate(templates):
            if temp['name'] == name:
                return templates[index]
        raise TemplateNotExists
