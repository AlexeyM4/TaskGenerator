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

    tasks = tasks_OGE.get_tasks_3(10, 3)
    for task in tasks:
        print(task.text_without_tags)
        print(task.answer)

    # tasks_OGE.to_html(tasks)


