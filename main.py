import EGE.EGE_all_tasks as EGE
import OGE.OGE_all_tasks as OGE


if __name__ == '__main__':
    tasks_EGE = EGE.TasksEGE()
    tasks_OGE = OGE.TasksOGE()


    # tasks_fourteen = tasks_EGE.get_tasks_14(2, 6)
    # for task in tasks_fourteen:
    #     print(task.text_without_tags)
    #     print(task.answer)

    # tasks_EGE.to_html(tasks_fourteen)

    # tasks_one = tasks_OGE.get_tasks_3(1, 1)§
    # for task in tasks_one:
    #     print(task.text_without_tags)
    #     print(task.answer)

    # tasks_OGE.to_html(tasks_one)

    tasks22 = tasks_EGE.get_tasks_22(2, 3)
    # for task in tasks22:
    #     print(task.text_without_tags)
    #     print(task.answer)
    # tasks_EGE.to_html(tasks22)

