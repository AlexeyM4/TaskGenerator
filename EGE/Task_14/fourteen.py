from bs4 import BeautifulSoup
import random as rnd


class Task14:
    def __init__(self, task_type: int):
        """
        Получить задание вида task_type:
        1 - Посчитать цифры
        2 - Определить значение числа p-ричной системы
        3 - Найти частное от деления(1 система счисления, 1 неизвестная)
        4 - Найти частное от деления(1 система счисления, 2 неизвестных)
        5 - Найти частное от деления(2 системы счисления, 1 неизвестная)
        6 - Найти частное от деления(2 системы счисления, 2 неизвестных)
        7 - Случайное задание
        :param type_task: Тип задания
        """
        self.__alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.number = 14
        self.exam = 'EGE'

        if task_type == 1:
            self.text, self.answer = self.__get_task_type_one()
        elif task_type == 2:
            self.text, self.answer = self.__get_task_type_two()
        elif task_type == 3:
            self.text, self.answer = self.__get_task_type_three(False, True)
        elif task_type == 4:
            self.text, self.answer = self.__get_task_type_three(True, True)
        elif task_type == 5:
            self.text, self.answer = self.__get_task_type_three(False, False)
        elif task_type == 6:
            self.text, self.answer = self.__get_task_type_three(True, False)
        elif task_type == 7:
            self.text, self.answer = self.__get_random_task()
        else:
            self.text, self.answer = None, None

        if self.text is not None:
            self.text_without_tags = self.text.replace('<sup>', '^').replace('</sup>', '')
            self.text_without_tags = self.__remove_all_tags(self.text_without_tags)
        else:
            self.text_without_tags = None

    def __remove_all_tags(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

    def __tr(self, num, base):
        res = ''
        while num > 0:
            res += self.__alphabet[num % base]
            num //= base
        return res[::-1]

    def __get_task_type_one(self):
        count_nums = rnd.randint(1, 5)

        nums = {rnd.randint(2, 1000): rnd.randint(2, 1000) for _ in range(count_nums)}

        res = sum(i ** nums[i] for i in nums)
        nm = rnd.randint(2, 100)
        zn = rnd.choice(['+', '-'])

        if zn == '-' and (res - nm) < 1:
            zn = '+'

        nums_st = [f'{num}<sup>{nums[num]}</sup>' for num in nums]
        text = ' + '.join(nums_st) + f' {zn} {nm}'

        res += nm
        if zn == '-':
            res -= 2 * nm

        base = rnd.randint(2, 36)
        while base == 10:
            base = rnd.randint(2, 36)

        fnd = rnd.choice(self.__alphabet[:base])
        ans = self.__tr(res, base).count(fnd)

        text_task = f'''
        <div>
        <p>Значение арифметического выражения {text} записали в системе счисления с основанием {base}.</p>
        <p>Сколько цифр {fnd} содержится в этой записи?</p>
        </div>
        '''

        return text_task, ans

    def __get_task_type_two(self):
        fnd = rnd.choice(['xy', 'yx', 'xxy', 'xyx', 'yxx', 'xyy', 'yxy', 'yyx'])

        while True:
            while True:
                base = rnd.randint(3, 36)

                num1 = rnd.randint(10, 400)
                num2 = rnd.randint(10, 400)

                num1b = self.__tr(num1, base)
                num2b = self.__tr(num2, base)

                t = list(set(num1b) & set(num2b))
                if len(t) > 1:
                    break

            num1b = num1b.replace(t[0], 'x').replace(t[1], 'y')
            num2b = num2b.replace(t[0], 'x').replace(t[1], 'y')
            res_b = self.__tr(num1 + num2, base).replace(t[0], 'x').replace(t[1], 'y')

            results = self.__get_answer_for_task_type_two(num1b, num2b, res_b, fnd)
            if len(results) > 0:
                break

        question = rnd.choice(['максимальное возможное значение',
                               'минимальное возможное значение',
                               'количество возможных значений'])

        question_end = ' и запишите это значение в десятичной системе счисления'
        if question == 'количество возможных значений':
            question_end = ''

        if question == 'максимальное возможное значение':
            ans = max(results)
        elif question == 'минимальное возможное значение':
            ans = min(results)
        else:
            ans = len(set(results))

        text_task = f'''
        <div>
        <p>В системе счисления с основанием p (p <= 36) выполняется равенство</p>
                            <p><center>{num1b} + {num2b} = {res_b}.</center></p>
        <p>Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием p.</p>
        <p>Определите {question} числа {fnd}(p){question_end}.</p>
        </div>
        '''

        return text_task, ans

    def __get_answer_for_task_type_two(self, num1b, num2b, res_b, fnd):
        alh = f'{num1b}{num2b}{res_b}'.replace('x', '').replace('y', '')
        if not alh:
            mx = 2
        else:
            mx = max(self.__alphabet.index(sorted(alh)[-1]) + 1, 2)

        ans = []
        for p in range(mx, 36):
            for x in self.__alphabet[:p]:
                for y in self.__alphabet[:p]:
                    nm1 = num1b.replace('x', x).replace('y', y)
                    nm2 = num2b.replace('x', x).replace('y', y)
                    res = res_b.replace('x', x).replace('y', y)

                    if (int(nm1, p) + int(nm2, p)) == int(res, p):
                        fn = int(fnd.replace('x', x).replace('y', y), p)
                        ans.append(fn)
        return ans

    def __get_nums_for_task_type_three(self, one_base):
        ans = rnd.randint(1, 100)
        self.div = rnd.randint(10, 300)

        result = self.div * ans

        num_1 = rnd.randint(1, result - 1)
        num_2 = result - num_1

        c = 0
        while True:
            self.base_1 = rnd.randint(3, 36)
            if one_base:
                self.base_2 = self.base_1
            else:
                self.base_2 = rnd.randint(3, 36)
            c += 1
            if self.base_1 != self.base_2 or one_base:
                self.t1 = self.__tr(num_1, self.base_1)
                self.t2 = self.__tr(num_2, self.base_2)
                t = set(self.t1) & set(self.t2)

                if len(t) > 1:
                    break

            if c == 50:
                return self.__get_nums_for_task_type_three(one_base)
        return list(t)

    def __get_task_type_three(self, tw=False, one_base=False):

        t = self.__get_nums_for_task_type_three(one_base)

        self.t1 = self.t1.replace(t[0], 'x', 1)
        self.t2 = self.t2.replace(t[0], 'x', 1)
        if tw:
            self.t1 = self.t1.replace(t[1], 'y', 1)
            self.t2 = self.t2.replace(t[1], 'y', 1)

        self.r = rnd.choice(['наименьшее', 'наибольшее'])

        text = self.__get_task_text(tw, one_base)
        ans = self.__check(tw)

        return text, ans

    def __get_task_text(self, tw, one_bases):
        text_bases = f'системах счисления с основаниями {self.base_1} и {self.base_2}'
        if one_bases:
            text_bases = f'системе счисления с основанием {self.base_1}'

        text = f'''
        <div>
        <p>Операнды арифметического выражения записаны в {text_bases}:</p>
                        <center><p>{self.t1}<sub>{self.base_1}</sub> + {self.t2}<sub>{self.base_2}</sub>.</p></center>
        <p>В записи чисел переменной x обозначена неизвестная цифра из алфавита десятичной системы счисления.
        Определите {self.r} значение x, при котором значение данного арифметического выражения кратно {self.div}.
        Для найденного значения x вычислите частное от деления значения арифметического выражения на {self.div} и укажите
        его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.</p>
        </div>
        '''
        if tw:
            text = f'''
            <div>
            <p>Операнды арифметического выражения записаны в {text_bases}:</p>
                    <center><p>{self.t1}<sub>{self.base_1}</sub> + {self.t2}<sub>{self.base_2}</sub>.</p></center>
            <p>В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
            Определите значения x и y, при которых значение данного арифметического выражения будет {self.r} и
            кратно {self.div}. Для найденных значений x и y вычислите частное от деления значения арифметического
            выражения на {self.div} и укажите его в ответе в десятичной системе счисления.
            Основание системы счисления в ответе указывать не нужно.</p>
            </div>
            '''

        return text

    def __check(self, tw):
        min_base = min([self.base_1, self.base_2])
        results = []
        for j in range(min_base):
            for i in range(min_base):
                t1 = self.t1.replace('x', self.__alphabet[i])
                t2 = self.t2.replace('x', self.__alphabet[i])

                if tw:
                    t1 = t1.replace('y', self.__alphabet[j])
                    t2 = t2.replace('y', self.__alphabet[j])

                res = int(t1, self.base_1) + int(t2, self.base_2)
                if res % self.div == 0:
                    results.append(res // self.div)
            if not tw:
                break

        results.sort()
        if self.r == 'наименьшее':
            return results[0]
        return results[-1]

    def __get_random_task(self):
        task_type = rnd.randint(1, 3)

        if task_type == 1:
            return self.__get_task_type_one()
        elif task_type == 2:
            return self.__get_task_type_two()
        elif task_type == 3:
            tw = rnd.choice([True, False])
            one_base = rnd.choice([True, False])
            return self.__get_task_type_three(tw=tw, one_base=one_base)
