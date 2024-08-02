from OGE.Task_1.ResourcesOne import *
from bs4 import BeautifulSoup
import random as rnd
import math


class Task1:
    def __init__(self, type_task):
        """
        Получить задание вида task_type:
        1 - Найти вычеркнутое слово
        2 - Определить рзмер предложения
        3 - Определить информационный объём рассказа
        4 - Найти лишнее слово
        5 - Случайное задание
        :param type_task: Тип задания
        """
        self.number = 1
        self.exam = 'OGE'

        if type_task == 1:
            self.text, self.answer = self.__get_task_type_one()
        elif type_task == 2:
            self.text, self.answer = self.__get_task_type_two()
        elif type_task == 3:
            self.text, self.answer = self.__get_task_type_three()
        elif type_task == 4:
            self.text, self.answer = self.__get_task_type_four()
        elif type_task == 5:
            self.text, self.answer = self.__get_random_task()
        else:
            self.text, self.answer = None, None

        if self.text is not None:
            self.text_without_tags = self.__remove_all_tags(self.text)
        else:
            self.text_without_tags = None

    def __remove_all_tags(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

    def __get_words(self, count_words, section):
        words = []
        len_words = []
        while len(words) != count_words:
            word = rnd.choice(sections[section])
            len_word = len(word)
            if len_word not in len_words:
                words.append(word)
                len_words.append(len_word)
        return words

    def __get_form_byte_word(self, bt):
        last_one = bt % 10
        last_two = bt % 100
        if 10 < last_two < 20 or last_one in (0, 1):
            return 'байт'
        elif last_one in (2, 3, 4, 5):
            return 'байта'
        return 'байтов'

    def __get_task_type_one(self):
        bt = rnd.choice(list(encodings_task))
        encoding = rnd.choice(encodings_task[bt])
        name = rnd.choice(names)

        count_words = rnd.randint(5, 8)
        section = rnd.choice(list(sections))

        words = self.__get_words(count_words, section)

        words_text = ', '.join(words)
        ans = rnd.choice(words)

        bit = len(ans) * bt // 8

        text = f'''
        <div>
        <p>В кодировке {encoding} каждый символ кодируется {bt} битами. {name} написал текст (в нем нет лишних пробелов):</p>
        <center><p>«{words_text} — {section}».</p></center>
        <p>Ученик вычеркнул из списка название {forms_words[section][0]}. 
        Заодно он вычеркнул ставшие лишними запятые и пробелы — два пробела не должны идти подряд.</p>
        <p>При этом размер нового предложения в данной кодировке оказался на {bit} {self.__get_form_byte_word(bit)} меньше, 
        чем размер исходного предложения. Напишите в ответе вычеркнутое название {forms_words[section][1]}.</p>
        </div>
        '''

        return text, ans

    def __get_task_type_two(self):
        bt = rnd.choice(list(encodings_task))
        encoding = rnd.choice(encodings_task[bt])

        sentence = rnd.choice(sentences)

        ans = len(sentence) * bt // 8

        text = f'''
        <div>
        <p>
        В кодировке {encoding} каждый символ кодируется {bt} битами. 
        Определите размер в байтах следующего предложения в данной кодировке: 
        <b>{sentence}</b>
        </p>
        </div>
        '''

        return text, ans

    def __get_task_type_three(self):
        bt = rnd.choice(list(encodings_task))
        encoding = rnd.choice(encodings_task[bt])

        pages = rnd.randint(2, 500)
        lines = rnd.randint(27, 50)
        symbols = rnd.randint(40, 60)

        ans = math.ceil((pages * lines * symbols * bt) // (8 * 1024))

        text = f'''
        <div><p>
        Текст, набранный на компьютере, содержит {pages} страниц, на каждой странице {lines} строк, 
        в каждой строке {symbols} символов. Определите информационный объем рассказа в Кбайтах в кодировке {encoding}, 
        в которой каждый символ кодируется {bt} битами.
        </p></div>
        '''

        return text, ans

    def __get_task_type_four(self):
        bt = rnd.choice(list(encodings_task))
        encoding = rnd.choice(encodings_task[bt])

        name = rnd.choice(names)
        poem = rnd.choice(poems)

        clear_poem = poem
        for i in ('.', ',', '!', '?', '-'):
            clear_poem = clear_poem.replace(i, ' ')

        words = clear_poem.split()
        len_words = [len(i) for i in words]
        uwords = [i for i in words if len_words.count(len(i)) == 1 and len(i) > 2]

        ans = rnd.choice(uwords)
        ansb = len(ans) * bt // 8

        b = 'байт'
        if bt == 32:
            b += 'а'

        poem_teg = '<p>«' + poem.replace('\n', '</p><p>') + '»</p>'
        text = f'''
        <div>
        <p>В кодировке {encoding} каждый символ кодируется {bt} битами. 
        {name} хотел написать текст (в нем нет лишних пробелов):</p>
                    <center>{poem_teg}</center>
        <p>Одно из слов ученик написал два раза подряд, поставив между одинаковыми словами один пробел. 
        При этом размер написанного предложения в данной кодировке оказался на {ansb} {b} больше, 
        чем размер нужного предложения. Напишите в ответе лишнее слово.</p>
        </div>
        '''

        return text, ans

    def __get_random_task(self):
        task_type = rnd.randint(1, 4)
        if task_type == 1:
            return self.__get_task_type_one()
        elif task_type == 2:
            return self.__get_task_type_two()
        elif task_type == 3:
            return self.__get_task_type_three()
        elif task_type == 4:
            return self.__get_task_type_four()
