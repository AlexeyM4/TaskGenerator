import codecs

class ToMoodle:
	
	def __init__(self, category):
		self.number = 0
		
		self.xmltext = f'''
		<?xml version="1.0" encoding="UTF-8"?>
		<quiz>
		<!-- question: 0  -->
		  <question type="category">
			<category>
			  <text><![CDATA[$course$/top/По умолчанию для ОГЭ/{category}]]></text>
			</category>
			<info format="html">
			  <text></text>
			</info>
			<idnumber></idnumber>
		  </question>
		'''
		
	def addvopros(self, voprosname, vopros, otvet):
		# voprosname - название вопроса, которое отображается в банке вопросов, ученик не видит
		self.number += 1
		
		self.xmltext += f'''
			<question type="shortanswer">
				<name>
				  <text>{voprosname} {self.number}</text>
				</name>
				<questiontext format="html">
				  <text><![CDATA[''' + vopros + ''']]></text>
				</questiontext>
				<generalfeedback format="html">
				  <text></text>
				</generalfeedback>
				<defaultgrade>1.0000000</defaultgrade>
				<penalty>0.3333333</penalty>
				<hidden>0</hidden>
				<idnumber></idnumber>
				<usecase>0</usecase>
				<answer fraction="100" format="moodle_auto_format">
				  <text>''' + otvet + '''</text>
				  <feedback format="html">
					<text></text>
				  </feedback>
				</answer>
			  </question>
			'''
		print('добавление вопроса' , self.number )
		
		
	def end(self,filename):
		self.xmltext += '</quiz>'
		fail = codecs.open(filename,'w', "utf-8")
		fail.write(self.xmltext)
		fail.close()
		print('Сгенерировано и записано')



# #один параметр: номер задания и его версия (если есть). Например: задание 10 три числа, задание 5,
# tratata = ToMoodle('Задание 99')
#
# #три параметра: название вопроса (тематика вопроса, в пару слов), текст вопроса (с html-тегами), правильный ответ
# tratata.addvopros('объ чомъто', 'Доколе?', 'Да')
# tratata.addvopros('объ чомъто', 'Кому на руси жить хорошо?', 'Это не я оно само')
# tratata.addvopros('объ чомъто', 'Перкеле?', '42')
#
# #один параметр: имя файла xml
# tratata.end('zad99.xml')

