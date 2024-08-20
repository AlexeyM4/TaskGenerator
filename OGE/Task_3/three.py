from bs4 import BeautifulSoup
import random as rnd


class Task3:
    def __init__(self):
        self.number = 3
        self.exam = 'OGE'

        self.text, self.answer = self.__get_task_type_one()

        if self.text is not None:
            self.text_without_tags = self.__remove_all_tags(self.text)
        else:
            self.text_without_tags = None

    def __remove_all_tags(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

    def __get_task_type_one(self):
        a = rnd.randint(2, 100)
        b = rnd.randint(2, 100)
        cond_bool = rnd.choice(['истинно', 'ложно'])

        expression = self.__get_expression()
        expc = f'НЕ ({expression})' if cond_bool == 'ложно' else expression
        nums = self.__get_nums_for_task_type_one(expc, a, b)

        while len(nums) == 0:
            a = rnd.randint(2, 100)
            b = rnd.randint(2, 100)
            cond_bool = rnd.choice(['истинно', 'ложно'])

            expression = self.__get_expression()
            expc = f'НЕ ({expression})' if cond_bool == 'ложно' else expression
            nums = self.__get_nums_for_task_type_one(expc, a, b)

        expression = expression.replace('a', str(a)).replace('b', str(b))
        que = [f'Напишите наименьшее целое число, для которого {cond_bool} высказывание']
        if nums[-1] <= 100:
            que.append(f'Напишите количество целых чисел, для которых {cond_bool} высказывание')
            if 'число делится' not in expression:
                que.append(f'Напишите наибольшее целое число, для которого {cond_bool} высказывание')

        cond = rnd.choice(que)
        if 'наименьшее' in cond:
            ans = min(nums)
        elif 'количество' in cond:
            ans = len(nums)
        else:
            ans = max(nums)

        text = f'<div><p>{cond}:</p> {expression}</div>'
        text = text.replace('НЕ', '<b>НЕ</b>')
        text = text.replace('ИЛИ', '<b>ИЛИ</b>')
        text = text.replace('И', '<b>И</b>')
        text = text.replace('(', '<i>(')
        text = text.replace(')', ')</i>')

        return text, ans

    def __get_nums_for_task_type_one(self, expression, a, b):
        lmd = self.__string_to_lambda(expression)
        return [x for x in range(1, 150+1) if lmd(x, a, b)]

    def __get_expression(self):
        nts = ['', 'НЕ ', '']
        logs = ['И', 'ИЛИ']
        ners = ['>=', '<=', '>', '<']

        yca = [f'X {rnd.choice(ners)} a', f'X {rnd.choice(ners)} a', 'Х четное', 'Х нечетное', 'число делится на a']
        ycb = [f'X {rnd.choice(ners)} b', f'X {rnd.choice(ners)} b', 'Х четное', 'Х нечетное', 'число делится на b']

        nt1 = rnd.choice(nts)
        nt2 = rnd.choice(nts)
        log = rnd.choice(logs)

        yc1 = rnd.choice(yca)
        yc2 = rnd.choice(ycb)

        not_yc = ['Х четное', 'Х нечетное', 'число делится на a', 'число делится на b']
        if (yc1 in not_yc) and (yc2 in not_yc):
            yc2 = ycb[0]

        exp = f'{nt1}({yc1}) {log} {nt2}({yc2})'

        if rnd.choice([True, False, False]):
            exp = f'НЕ ({exp})'

        return exp

    def __string_to_lambda(self, expression: str):
        expression = self.__remove_all_tags(expression)
        changes = {
            'ИЛИ': 'or',
            'И': 'and',
            'НЕ': 'not',
            'Х четное': 'x % 2 == 0',
            'Х нечетное': 'x % 2 != 0',
            'число делится на b': 'x % b == 0',
            'число делится на a': 'x % a == 0'
        }
        for old, new in changes.items():
            expression = expression.replace(old, new)

        return eval(f"lambda x, a, b: {expression.lower()}")
    