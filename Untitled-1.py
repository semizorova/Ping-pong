from pygame import*
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,QGroupBox,QRadioButton,QButtonGroup
from random import shuffle,randint
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,Player_speed,width,height):
        super().__init__()
        self.image =  transform.scale(image.load(player_image),(width,height))
        self.speed = Player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys= key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys= key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

game = True
finish = False
width = 600
height = 500
window = display.set_mode((width,height))
back = (200,250,250)
window.fill(back)

def qvest():
    app = QApplication([])
    main_win = QWidget()
    main_win.setWindowTitle("Memory Card")
    text = QLabel('Первое професиональное соревнование в:')#надпись
    btn = QPushButton('Ответить')
    RadioGroupBox = QGroupBox("Варианты ответов" )
    rbtn_1 = QRadioButton( '1900' )
    rbtn_2 = QRadioButton( '1901' )
    rbtn_3 = QRadioButton( '1910' )
    rbtn_4 = QRadioButton(' 1905' )
    RadioGroup = QButtonGroup()
    RadioGroup.addButton(rbtn_1)
    RadioGroup.addButton(rbtn_2)
    RadioGroup.addButton(rbtn_3)
    RadioGroup.addButton(rbtn_4)
    AnswerGroupBox = QGroupBox("Результат теста" )
    rbtne_1 = QLabel( 'Правильно/Неправильно' )
    rbtne_2 = QLabel( 'Правильный ответ' )
    layout_ans4 = QVBoxLayout()
    layout_ans4.addWidget(rbtne_1)
    layout_ans4.addWidget(rbtne_2)
#расположение виджетов по лэйаутам
    layout_main = QVBoxLayout() 
    line1 = QHBoxLayout()#разметка
    line2 = QHBoxLayout()
    line3 = QHBoxLayout()
#Группа по лэйаутам
    layout_ans1=QHBoxLayout()
    layout_ans2=QVBoxLayout()
    layout_ans3 =QVBoxLayout()
    layout_ans2.addWidget(rbtn_1)
    layout_ans2.addWidget(rbtn_2)
    layout_ans3.addWidget(rbtn_3)
    layout_ans3.addWidget(rbtn_4)
    layout_ans1.addLayout(layout_ans2)
    layout_ans1.addLayout(layout_ans3)
    RadioGroupBox. setLayout (layout_ans1)
    AnswerGroupBox. setLayout (layout_ans4)
    line1.addWidget(text, alignment = Qt.AlignCenter)
    line2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
    line2.addWidget(AnswerGroupBox, alignment = Qt.AlignCenter)
    line3.addWidget(btn)
    layout_main.addLayout(line1)
    layout_main.addLayout(line2)
    layout_main.addLayout(line3)
#обработка нажатий на переключатели
    def show_result():
        RadioGroupBox.hide()
        AnswerGroupBox.show()
        btn.setText("К игре")
    def show_question():
        RadioGroupBox.show()
        AnswerGroupBox.hide()
        btn.setText("Ответить")
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)
    def start_test():
        if btn.text()=="Ответить":
            show_result()
        else:
            show_question()
    class Question():
        def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2= wrong2
            self.wrong3 = wrong3
    answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
    def ask(q):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        text.setText(q.question)
        rbtne_2.setText(q.right_answer)
        show_question()
    q = Question('Первое професиональное соревнование в:','1900','1901','1910','1905')
    ask(q)
    question_list = []
    q1 = Question(
        'Самая длинная партия в пинг-понг:(часы)','146',
        '140','136','112')
    q2 = Question(
        'Во время игры шар может разгоняться до:','170 км/ч',
        '100 км/ч','120 км/ч',' 150 км/ч')
    q3 = Question(
        'Этот вид спорта внесён в список Олимпийских игр с:','1988',
        '1950','1910','1998')

    question_list.append(q1)
    question_list.append(q2)
    question_list.append(q3)
    def show_correct(res):
        rbtne_1.setText(res)
        show_result()
    def check_answer():
        if answers[0].isChecked():
            show_correct('Правильно!')
            main_win.score += 1
        else:
            if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                show_correct('Неверно!')
    def click_ok():
        if btn.text()=="Ответить":
            check_answer()
        else:
            next_question()
    def next_question():
        main_win.total += 1
        main_win.hide()
        cur_question = randint(0,len(question_list) - 1)
        ask(question_list[cur_question])

    btn.clicked.connect(click_ok)
    main_win.total = 0 
    main_win.score = 0 
    #отображение окна приложения
    main_win.setLayout(layout_main)
    main_win.show()
    AnswerGroupBox.hide()
    app.exec_()

speed_x = 3
speed_y = 3
score1 = 0
score2 = 0
clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont(None, 70)
font2 = font.SysFont(None, 50)
text1 = font2.render(str(score1)+":",1,(255,0,0))
text2 = font2.render(str(score2),1,(255,0,0))
pin = GameSprite("ball.png",200,200,4,50,50)
rack_1 = Player("fon.jpg",30,200,4,30,150)
rack_2 = Player("fon.jpg",520,200,4,30,150)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        rack_1.update_l()
        rack_2.update_r()
        
        pin.rect.x += speed_x
        pin.rect.y += speed_y
        window.blit(text1,(265,80))
        window.blit(text2,(295,80))

        pin.reset()
        rack_1.reset()
        rack_2.reset()
        if sprite.collide_rect(rack_1, pin) or sprite.collide_rect(rack_2, pin):
            speed_x *= -1
        if pin.rect.y > 450 or pin.rect.y < 0:
            speed_y *= -1
        if pin.rect.x > 600:
            qvest()
            score2 += 1
            pin.kill()
            pin.reset()
        if pin.rect.x < -50:
            qvest()
            score1 += 1
            pin.kill()
            pin.reset()
    display.update()
    clock.tick(FPS)