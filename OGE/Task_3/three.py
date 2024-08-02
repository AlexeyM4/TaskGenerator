from bs4 import BeautifulSoup
import random as rnd


class Task3:
    def __init__(self, task_type: int):

        if task_type == 1:
            self.text, self.answer = self.__get_task_type_one()

        if self.text is not None:
            self.text_without_tags = self.__remove_all_tags(self.text)
        else:
            self.text_without_tags = None

    def __remove_all_tags(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

    def __get_task_type_one(self):

        return 'Some text', 0