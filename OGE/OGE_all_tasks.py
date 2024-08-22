import TasksHTML
import OGE.Task_1.one as one_task
import OGE.Task_3.three as three_task


class TasksOGE:
    def to_html(self, tasks: list, path='') -> None:
        """
        Создание html файла с заданиями
        :param tasks: Список заданий
        :param path: Путь для сохранения файла
        :return: None
        """
        TasksHTML.TasksHTML().to_html(tasks, path)

    def get_tasks_1(self, k: int, tasks_type: int) -> list:
        """
        Получить список с заданиями вида tasks_type:
        1 - Найти вычеркнутое слово
        2 - Определить рзмер предложения
        3 - Определить информационный объём рассказа
        4 - Найти лишнее слово
        5 - Случайное задание
        :param k: Количество заданий
        :param tasks_type: Тип заданий
        :return: Список заданий
        """
        return [one_task.Task1(tasks_type) for _ in range(k)]

    def get_tasks_3(self, k: int, tasks_type: int) -> list:
        """
        Получить задание вида task_type:
        1 - Высказывание истинно
        2 - Высказывание ложно
        3 - Случайное задание
        :param k: Количество заданий
        :param tasks_type: Тип заданий
        :return: Список заданий
        """
        return [three_task.Task3(tasks_type) for _ in range(k)]