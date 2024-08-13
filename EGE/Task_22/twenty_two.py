from bs4 import BeautifulSoup
import random as rnd
import pandas as pd


class Task22:
    def __init__(self, task_type: int):
        """
        Получить задание вида task_type:
        1 - Определить минимальоне время при параллельном выполнении процессов
        2 - Определить максимальное время выполнения всех процессов
        3 - Определить минимальоне время при наличии задержки между процессами
        4 -
        :param task_type: Тип задания
        """
        self.number = 22
        self.exam = 'EGE'
        self.__end = {}
        self.__df = pd.DataFrame()
        self.__wait = 0


        if task_type == 1:
            self.text, self.answer = self.__get_task_type_one()
        elif task_type == 2:
            self.text, self.answer = self.__get_task_type_two()
        elif task_type == 3:
            self.__wait = rnd.randint(1, 5)
            self.text, self.answer = self.__get_task_type_three()

        if self.text is not None:
            self.text_without_tags = self.__remove_all_tags(self.text)
        else:
            self.text_without_tags = None

        print(self.text_without_tags)
        print(self.__df)
        print(self.answer)
        print(self.__end)

    def __remove_all_tags(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

    def __get_data(self):
        data = []
        for i in range(1, 11):

            c = rnd.randint(1, 2) if i > 2 else 0
            z = ['0']
            if c == 1:
                z = [str(rnd.randint(1, i - 1))]
            elif c == 2:
                z = sorted(map(str, rnd.sample(list(range(1, i)), 2)))

            tm = rnd.randint(1, 10)
            self.__get_end(i, tm, z)
            data.append({'ID процесса B': i,
                         'Время выполнения процесса B (мс)': tm,
                         'ID процесса(ов) A': ', '.join(z)})
        return data

    def __get_task_type_one(self):
        data = self.__get_data()

        self.__df = pd.DataFrame(data)

        text = self.__get_text_for_task_type_one_and_two('минимальное')
        answer = self.__get_answer_for_task_type_one()

        return text, answer

    def __get_end(self, proces, tm, z):
        self.__end[proces] = [0, tm]
        if len(z) == 1:
            if z[0] != '0':
                self.__end[proces][1] += self.__end[int(z[0])][1] + self.__wait
                self.__end[proces][0] = self.__end[int(z[0])][1]
        else:
            mx = 0
            pr = 0
            for i in z:
                i = int(i)
                if self.__end[i][1] > mx:
                    mx = self.__end[i][1]
                    pr = i

            self.__end[proces][1] += self.__end[pr][1] + self.__wait
            self.__end[proces][0] = self.__end[pr][1]

    def __get_text_for_task_type_one_and_two(self, cnd):

        text = f'''
        <div>
<p>В файле содержится информация о совокупности N вычислительных процессов, которые могут выполняться параллельно или 
последовательно. Будем говорить, что процесс B зависит от процесса A, если для выполнения процесса B необходимы 
результаты выполнения процесса A. В этом случае процессы могут выполняться только последовательно.</p>
<p>Информация о процессах представлена в файле в виде таблицы. В первом столбце таблицы указан идентификатор процесса (ID), 
во втором столбце таблицы — время его выполнения в миллисекундах, 
в третьем столбце перечислены с разделителем «;» ID процессов, от которых зависит данный процесс. 
Если процесс является независимым, то в таблице указано значение 0.</p>
<p><i>Типовой пример организации данных в файле:</i></p>
<div>
<table>
    <tr>
        <th>ID процесса <i>B</i></th>
        <th>Время выполнения процесса <i>B</i> (мс)</th>
        <th>ID процесса(ов) <i>A</i></th>
    </tr>
    <tr><td>1</td> <td>4</td> <td>0</td></tr>
    <tr><td>2</td> <td>3</td> <td>0</td></tr>
    <tr><td>3</td> <td>1</td> <td>1; 2</td></tr>
    <tr><td>4</td> <td>7</td> <td>3</td></tr>
</table>
</div>
<p>Определите {cnd} время, через которое завершится выполнение всей совокупности процессов, при условии, 
что все независимые друг от друга процессы могут выполняться параллельно.</p>
<p>Выполните задания, используя данные из файла ниже:</p>
</div>'''

        return text

    def __get_answer_for_task_type_one(self):
        return max([i[1] for i in self.__end.values()])

    def __get_task_type_two(self):
        data = self.__get_data()

        self.__df = pd.DataFrame(data)
        text = self.__get_text_for_task_type_one_and_two('максимальное')
        answer = self.__get_answer_for_task_type_two()

        return text, answer

    def __get_answer_for_task_type_two(self):
        return sum(self.__df['Время выполнения процесса B (мс)'])


    def __get_task_type_three(self):
        data = self.__get_data()

        self.__df = pd.DataFrame(data)

        text = self.__get_text_for_task_type_three()
        answer = self.__get_answer_for_task_type_three()
        return text, answer

    def __get_text_for_task_type_three(self):

        text = f'''
<div>
<p>В компьютерной системе необходимо выполнить некоторое количество вычислительных процессов, которые могут выполняться 
параллельно или последовательно. Для запуска некоторых процессов необходимы данные, которые получаются как результаты 
выполнения одного или двух других процессов — поставщиков данных. Независимые процессы 
(не имеющие поставщиков данных) можно запускать в любой момент времени. Если процесс B (зависимый процесс) получает 
данные от процесса A (поставщика данных), то процесс B может начать выполнение не раньше чем через {self.__wait}мс после 
завершения процесса A. Любые процессы, готовые к выполнению, можно запускать параллельно, при этом количество 
одновременно выполняемых процессов может быть любым, длительность процесса не зависит от других параллельно 
выполняемых процессов.
</p>
<div>
<table>
    <tr>
        <th>ID процесса <i>B</i></th>
        <th>Время выполнения процесса <i>B</i> (мс)</th>
        <th>ID процесса(ов) <i>A</i></th>
    </tr>
    <tr><td>1</td> <td>6</td> <td>0</td></tr>
    <tr><td>2</td> <td>2</td> <td>0</td></tr>
    <tr><td>3</td> <td>10</td> <td>2</td></tr>
    <tr><td>4</td> <td>4</td> <td>1; 3</td></tr>
</table>
</div>
<p>
В таблице представлены идентификатор (ID) каждого процесса, его длительность и ID поставщиков данных для зависимых процессов.</p>
<p>
Определите, за какое минимальное время можно выполнить все процессы. В ответе запишите целое число — минимальное время в мс.
</p>
</div>
'''
        return text

    def __get_answer_for_task_type_three(self):
        return max([i[1] for i in self.__end.values()])