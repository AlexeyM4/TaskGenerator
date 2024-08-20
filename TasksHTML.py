import time
import os


class TasksHTML:
    def to_html(self, tasks: list, path='') -> None:
        """
        Создание html файла с заданиями
        :param tasks: Список заданий
        :param path: Путь для сохранения файла
        :return: None
        """
        number = tasks[0].number
        exam = tasks[0].exam

        text_tasks = ''
        for task in tasks:
            text_tasks += f'{task.text}<hr>\n'

        text = f'''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Информатика</title>
    </head>
    <body>
        {text_tasks}
    </body>
</html>'''

        if not path:
            current_dir_path = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(current_dir_path, exam, 'html_pages')

        current_time_str = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        file_name = f'Task{number}_{current_time_str}.html'

        path = os.path.join(path, file_name)
        with open(path, 'w') as file:
            file.writelines(text)
