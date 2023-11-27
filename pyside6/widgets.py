import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Sistema')

botao1 = QPushButton('Salvar')
botao1.setStyleSheet('font-size: 40px; color: green')

botao2 = QPushButton('Cancelar')
botao2.setStyleSheet('font-size: 40px; color: red')

botao3 = QPushButton('Sair')
botao3.setStyleSheet('font-size: 40px; color: gray')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 2, 1, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 1)

def slot_example(status_bar):
    status_bar.showMessage('Slot Executado')

status_bar = window.statusBar()
status_bar.showMessage('Mensagem')

menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
acao_1 = primeiro_menu.addAction('Primeira Ação')
acao_1.triggered.connect(lambda sb: slot_example(status_bar))

window.show()
app.exec()