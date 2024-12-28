PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout, QVBoxLayout, QButtonGroup
from random import*
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Столица Австрии', 'Вена', 'Париж', 'Вашингтин', 'Хельсинки'))
question_list.append(Question('Сколько звезд на флгае США', '50', '49', '35', '52'))
question_list.append(Question('Какая страна не граничит с Грецией', 'Италия', 'Албания', 'Турция', 'Болгария'))
question_list.append(Question('Какую страну омывают Индийский и Атлантический океан?', 'ЮАР', 'Чили', 'Швеция', 'Канада'))
question_list.append(Question('В какой стране нет верблюдов', 'Дания', 'Казахстан', 'Австралия', 'Египет'))
app = QApplication([])
main = QWidget()
main.setWindowTitle('Memory Card')
answer = QPushButton('ОТВЕТИТЬ')
question = QLabel('Столица Австрии:')
RadioGroupBox = QGroupBox('Варианты ответа')
btn1 = QRadioButton('Вена')
btn2 = QRadioButton('Париж')
btn3 = QRadioButton('Вашингтон')
btn4 = QRadioButton('Хельсинки')
main.score = 0
main.total = -1
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)
layout_card = QVBoxLayout()
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(btn1)
layout_ans2.addWidget(btn2)
layout_ans3.addWidget(btn3)
layout_ans3.addWidget(btn4)
answers = [btn1, btn2, btn3, btn4]
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результаты теста:')
ib_Question = QLabel('2222')
ib_Result = QLabel('123')
ib_Correcr = QLabel('222')
layout_res = QVBoxLayout()
layout_res.addWidget(ib_Result, alignment=(Qt.AlignTop))
layout_res.addWidget(ib_Correcr, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(question)
layout_line3.addWidget(answer)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addLayout(layout_line3, stretch = 1)
AnsGroupBox.hide()
main.cur_question = -1

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('ДАЛЕЕ')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    answer.setText('ОТВЕТИТЬ')

    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    ib_Correcr.setText(q.right_answer)
    show_question()

def show_correct(res):
    ib_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('ПРАВИЛЬНО')
        main.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('НЕВЕРНО')

def next_question():
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    main.total += 1
    if main.total != 0:
        rate = main.score/main.total
        print('РЕЙТИНГ', rate)
        print('ВСЕГО ПОПЫТОК' , main.total)
    ask(q)

def click_OK():
    if answer.text() == 'ОТВЕТИТЬ':
        check_answer()
    else:
        next_question()

answer.clicked.connect(click_OK)
next_question()
main.setLayout(layout_card)
main.show()
app.exec_()