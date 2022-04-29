#создай приложение для запоминания информации
#подключение модулей
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self,question, right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q_list = []
q1 = Question('Государственный язык Бразилии','Португальский','Итальянский','Испанский','Бразильский ')
q_list.append(q1)
q2 = Question('Какой гормон вырабатывает поджелудочная железа?','инсулин','адреналин','норадреналин','мелатонин')
q_list.append(q2)
q3 = Question('На каком(их) языке(ах) говорят в Канаде?','Французский и Английский','Итальянский и Английский','Английский','Французский')
q_list.append(q3)
q4 = Question('Как называется болезнь щитовидной железы при нехватке йода?','Зоб','Базедова болезнь','Карликовость','Несахарный диабет')
q_list.append(q4)
q5 = Question('Как называется водная оболочка земли?','Гидросфера','Атмосфера','Литосфера','Мантия')
q_list.append(q5)
q6 = Question('Какая формула Q существует?','Q = qm','Q = cmV','Q = mt','Q = Rm')
q_list.append(q6)
q7 = Question('Какая железа относится к железам смешанной секреции?','Поджелудочная','Гипофиз','Эпифиз','Щитовидная железа')
q_list.append(q7)
q8 = Question('Как переводится на английский слово цирк?','circus','circle','circ','cirk')
q_list.append(q8)
q9 = Question('Как называется столица Китая?','Пекин','Сеул','Пхеньян','Токио')
q_list.append(q9)
q10 = Question('Как переводится на английский слово возможно','possible','posible','posibl','point')
q_list.append(q10)
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.resize(400,300)
main_win.setWindowTitle('Memory Card')
#создание виджетов 
question = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')
#добавление виджетов и линий к главной линии
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line1.addWidget(rbtn1)
line1.addWidget(rbtn2)
line2.addWidget(rbtn3)
line2.addWidget(rbtn4)
line3 = QHBoxLayout()
line3.addLayout(line1)
line3.addLayout(line2)
RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroupBox.setLayout(line3)

line4 = QHBoxLayout()
line5 = QHBoxLayout()
line4.addWidget(question,alignment = Qt.AlignHCenter)
line5.addWidget(button, alignment = Qt.AlignHCenter)
line6 = QVBoxLayout()
line7 = QHBoxLayout()
line7.addWidget(RadioGroupBox)
line6.addLayout(line4)
line6.addLayout(line7)
line6.addLayout(line5)

#скрытие радиогруппы
#RadioGroupBox.hide()
#создание радиогруппы с ответом
text = QLabel('-----')
answer = QLabel('------')
line8 = QVBoxLayout()
line8.addWidget(text,alignment= Qt.AlignLeft)
line8.addWidget(answer, alignment = Qt.AlignCenter)
AnsRadioGroupBox = QGroupBox('Результат теста')
AnsRadioGroupBox.setLayout(line8)
line7.addWidget(AnsRadioGroupBox)
AnsRadioGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

def show_result():
    RadioGroupBox.hide()
    AnsRadioGroupBox.show()
    button.setText('Следующий вопрос')
def show_question():
    AnsRadioGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    answer.setText(q.right_answer)
    show_question()

def show_correct(res):
    text.setText(res)
    show_result()
 
main_win.total = 0
main_win.score = 0 
def check_answer():
    if answers[0].isChecked(): 
        show_correct('Правильно')
        main_win.score += 1
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно')
    print('Статистика\n - Всего вопросов:', main_win.total, '\n - Правильных ответов:',main_win.score,'\n Рейтинг:', main_win.score/main_win.total *100, '%')
main_win.cur_question = -1

def next_question():
    main_win.total += 1
    cur_question = randint(0,len(q_list)-1)
    q = q_list[cur_question]
    ask(q)
def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else: 
        next_question()

button.clicked.connect(click_OK)
next_question()
#отображение окна 
main_win.setLayout(line6)
main_win.show()
app.exec_()