import TasksHTML
import EGE.Task_14.fourteen as fourteen_task
import EGE.Task_22.twenty_two as twenty_two


class TasksEGE:
    def to_html(self, tasks: list, path='') -> None:
        """
        Создание html файла с заданиями
        :param tasks: Список заданий
        :param path: Путь для сохранения файла
        :return: None
        """
        TasksHTML.TasksHTML().to_html(tasks, path)

    def get_tasks_14(self, k: int, tasks_type: int) -> list:
        """
        Получить список с заданиями вида task_type:
        1 - Посчитать цифры
        2 - Определить значение числа p-ричной системы
        3 - Найти частное от деления(1 система счисления, 1 неизвестная)
        4 - Найти частное от деления(1 система счисления, 2 неизвестных)
        5 - Найти частное от деления(2 системы счисления, 1 неизвестная)
        6 - Найти частное от деления(2 системы счисления, 2 неизвестных)
        7 - Случайные задания
        :param k: Количество заданий
        :param tasks_type: Тип заданий
        :return: Список заданий
        """
        return [fourteen_task.Task14(tasks_type) for _ in range(k)]

    def get_tasks_22(self, k: int, tasks_type: int) -> list:
        """
        Получить список с заданиями вида task_type:
        1 - Определить минимальоне время при параллельном выполнении процессов
        2 - Определить максимальное время выполнения всех процессов
        3 - Определить минимальоне время при наличии задержки между процессами
        4 -
        :param k: Количество заданий
        :param tasks_type: Тип заданий
        :return: Список заданий
        """
        return [twenty_two.Task22(tasks_type) for _ in range(k)]
