from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QButtonGroup, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle, randint

class Question():
    def __init__(self, question, righ_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.righ_answer = righ_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list =[]
questions_list.append(Question('Топ шутер из стима','CS GO','stendoff 2','DOTA 2','Бравол старс'))
questions_list.append(Question('Топ шутр на телифон','Stendoff 2','clash Royale','Пабг','Фри фаер'))
questions_list.append(Question('спорт в котором надо пинать мачь','футбол','регби','гольф','боулинг'))
questions_list.append(Question('игровой девайс на котором есть клавешы','ПК','телефон','Плейстейшин','IX бокс'))
questions_list.append(Question('Жив ли мистор бист','Да','нет','незнаю','незнаю кто это'))
questions_list.append(Question('сколько пк у нас в классе ','11',' 5','23',' 13'))
questions_list.append(Question('кто добрея илон маск или мистор бист','мистор бист',' илон маск','оба',' не кто'))
questions_list.append(Question('Топ хорор игор на телифон','Fnaf ',' грени 3','метель',' грени 2'))
questions_list.append(Question('сколько стоит самый дорогой ПК','1 620 000',' 2 000 000',' 1 000 000',' 1 619 149'))
questions_list.append(Question('сколько стоит самый дорогой телефон ','$48,5млн',' $40,2млн','$38,4млн','$10,5млн'))
questions_list.append(Question('сколько стоит самый дорогой дом в мире','$12млн','$1млн ',' $10млн',' $2млн'))
questions_list.append(Question('гдеможно играть в игры не скачевая их в',' VK','Яндекс играх','просто в играх','или просто найти в инете'))
app=QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)



AnsGroupBox = QGroupBox("Результаты текста")
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

RadioGeoup = QButtonGroup()
RadioGeoup.addButton(rbtn_1)
RadioGeoup.addButton(rbtn_2)
RadioGeoup.addButton(rbtn_3)
RadioGeoup.addButton(rbtn_4)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGeoup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGeoup.setExclusive(True)

def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.righ_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.righ_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total,'\n-Правельных ответов:',window.score)
        print('Рейтинг', (window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг', (window.score/window.total*100),'%')

def next_question():
    window.total+=1
    
    print('Статистика\n-Всего вопросов:', window.total,'\n-Правельных ответов:',window.score)
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
        
    ask(q)
def click_OK():
    if btn_OK.text() =='Ответить':
        check_answer()
    else:
        next_question()
window = QWidget()
window.setWindowTitle('Memo Card')
window.setLayout(layout_card)
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.score=0
window.total=0
next_question()
window.show()
app.exec()
window = QWidget()



