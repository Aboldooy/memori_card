'''
Файл, в якому відтворено інтерфейс головного вікна
'''

from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

window_main = QWidget()#вікно головного меню
window_layout = QVBoxLayout()#лейаут для вікна головного меню

#ВІДЖЕТИ ВІКНА#

menu_pbtn = QPushButton("Налаштування")
rest_pbtn = QPushButton("Відпочинок")
give_answer_pbtn = QPushButton("Відповісти")

rest_sbox = QSpinBox()
rest_sbox.setValue(30)

ans1_rbtn = QRadioButton("Answer 1")
ans2_rbtn = QRadioButton("Answer 2")
ans3_rbtn = QRadioButton("Answer 3")
ans4_rbtn = QRadioButton("Answer 4")

question_lbl = QLabel("Question")
minutes_lbl = QLabel(" хвилин")
result_lbl = QLabel("Правильна відповідь")

answers_gbox = QGroupBox()
result_gbox = QGroupBox()

#ЛЕЙАУТИ ВІКНА#

header_layout = QHBoxLayout()
answers_gbox_layout = QVBoxLayout()
result_gbox_layout = QVBoxLayout()

answer_buttons_row1_layout = QHBoxLayout()
answer_buttons_row2_layout = QHBoxLayout()

#Розташовуємо віджети у лейаутах#

header_layout.addWidget(menu_pbtn)
header_layout.addWidget(rest_pbtn)
header_layout.addWidget(rest_sbox)
header_layout.addWidget(minutes_lbl)
window_layout.addLayout(header_layout)


#додали текст із питаннями у головний лейаут
window_layout.addWidget(question_lbl)

#додаємо віджети у лейаут answers_gbox_layout, вставляєм його до answers_gbox
answer_buttons_row1_layout.addWidget(ans1_rbtn)
answer_buttons_row1_layout.addWidget(ans2_rbtn)

answer_buttons_row2_layout.addWidget(ans3_rbtn)
answer_buttons_row2_layout.addWidget(ans4_rbtn)

answers_gbox_layout.addLayout(answer_buttons_row1_layout)
answers_gbox_layout.addLayout(answer_buttons_row2_layout)

answers_gbox.setLayout(answers_gbox_layout)
window_layout.addWidget(answers_gbox)

#додаємо віджети у лейаут result_gbox_layout, вставлєм його до result_gbox
result_gbox_layout.addWidget(result_lbl)
result_gbox.setLayout(result_gbox_layout)
window_layout.addWidget(result_gbox)

#Вставляємо до головного лейаута кнопку "Відповісти"
window_layout.addWidget(give_answer_pbtn)

window_main.setLayout(window_layout)#вставляємо для вікна його лейаут
