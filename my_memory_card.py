from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QLayout, QGroupBox, QButtonGroup
from random import shuffle, randint

#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
quest = QLabel('Какой национальности не существует?')
main_win.window_question = -1
btn = QPushButton('Ответить')
question_list = list()
main_win.answer_score = 0
main_win.answer_all = 0



class Quesstion():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q1 = Quesstion('Государственный язык Бразилии?', 'Португальский', 'Японский', 'Питон', 'Итальянский')
q2 = Quesstion('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты')
q3 = Quesstion('afd', 'a', 'b', 'c', 'd')
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
shuffle(question_list)

def ask (vopros: Quesstion):
    RadioGroupBox.hide()
    btn.hide()
    rbtn_1.setText(vopros.right_answer)
    rbtn_2.setText(vopros.wrong1)
    rbtn_3.setText(vopros.wrong2)
    rbtn_4.setText(vopros.wrong3)

    shuffle(answer)
    #Перемешиваем значения
    layout_ver1.addWidget(answer[0])
    layout_ver1.addWidget(answer[1])
    layout_ver2.addWidget(answer[2])
    layout_ver2.addWidget(answer[3])

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

    RadioGroupBox.show()
    quest.setText(vopros.quest)
    btn.show()
    btn.setText('Ответить')

    answear.setText(vopros.right_answer)

def check_answer(): #проверка
    ans_cor = 'Молодец'
    ans_wrong = 'Не угадал'
    ans_mis = 'Надо выбрать вариант ответа'
    btn.setText('Следующий вопрос')
    if rbtn_1.isChecked():
        show_correct(ans_cor)
        rez_ans.setText('Правельный ответ')
        main_win.answer_all += 1
        main_win.answer_score += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        show_correct(ans_wrong)
        main_win.answer_all += 1
        rez_ans.setText('Неправильный ответ')
    else:
        show_correct(ans_mis)
        main_win.answer_all += 1
        rez_ans.setText('Попробуй ещё раз')

def show_correct(res):
    RadioGroupBox.hide()
    grup_ans.hide()

    rez_ans.setText(res)
    
    grup_ans.show()
    btn.setText('Следующий вопрос')

def show_question():
    RadioGroup.show()
    grup_ans.hide()
    quest=setText('Какой национальности не существует?')
    btn.setText('Ответить')
    adioGroupBox.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroupBox.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    grup_ans.show()
    quest.setText('Самый сложный вопрос в мире?')
    btn.setText('Следующий вопрос')
    check_answer()
    
    

def start_test():
    if btn.text() == 'Ответить':
        show_result()
    else:
        show_question()

def next_question():
    grup_ans.hide() 
    main_win.window_question = main_win.window_question + 1
    if len(question_list) == main_win.window_question:
        main_win.window_question = 0
    vopros = question_list[main_win.window_question]
    ask(vopros)

def click_OK():
    if btn.text() == 'Ответить':
        show_result()
    else:
        next_question()

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]# список с кнопками

RadioGroup = QButtonGroup() #группа кнопок
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_gor1 = QHBoxLayout()   
layout_ver1 = QVBoxLayout() 
layout_ver2 = QVBoxLayout()

RadioGroup = QButtonGroup() #групп по функц
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ver1.addWidget(rbtn_1) 
layout_ver1.addWidget(rbtn_2)
layout_ver2.addWidget(rbtn_3) 
layout_ver2.addWidget(rbtn_4)
layout_gor1.addLayout(layout_ver1)
layout_gor1.addLayout(layout_ver2)
layout_ver1.setSpacing(35)
layout_ver2.setSpacing(35)
layout_gor1.setSpacing(35)
RadioGroupBox.setLayout(layout_gor1)

btn = QPushButton('Ответить')     #кнопка ответа
maim_lin_vert = QVBoxLayout()
maim_lin_gor1 = QHBoxLayout()
maim_lin_gor3 = QHBoxLayout()

maim_lin_gor1.addWidget(quest, alignment=Qt.AlignHCenter)   #сбор виджетов и группы
maim_lin_gor3.addStretch(2)
maim_lin_gor3.addWidget(btn, stretch=5)
maim_lin_gor3.addStretch(2)
maim_lin_vert.addLayout(maim_lin_gor1)
maim_lin_vert.addWidget(RadioGroupBox, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))




#ФОРМА окна результата

grup_ans = QGroupBox('Результат ответа')
rez_ans = QLabel('Прав/неправ')
answear = QLabel('Правельный ответ')
boxline_vert = QVBoxLayout()

boxline_vert.addWidget(rez_ans)
boxline_vert.setSpacing(35)
boxline_vert.addWidget(answear, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

grup_ans.setLayout(boxline_vert)


maim_lin_vert.addWidget(grup_ans, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) #сбор виджетов и двух групп

maim_lin_vert.addLayout(maim_lin_gor3)  #сбор виджетов и двух групп
main_win.setLayout(maim_lin_vert)       #сбор виджетов и двух групп


#ask('Государственный язык Бразилии', 'Португальский', 'Японский', 'Питон', 'Итальянский')

btn.clicked.connect(click_OK)

next_question()
RadioGroupBox.show()
grup_ans.hide()
btn.show()

main_win.show()
app.exec_()

reiting = main_win.answer_score/main_win.answer_all * 100

print('Всего вопросов:', main_win.answer_all)
print('Всего ответов:', main_win.answer_score)
print('Статистика:',reiting, '%')