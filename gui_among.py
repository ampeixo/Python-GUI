import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui


class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 350
        self.esquerda = 600
        self.largura = 380
        self.altura = 260
        self.titulo = "Primeiro GUI"

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(30, 200)
        self.caixa_texto.resize(200, 30)
        self.caixa_texto.setToolTip("Digite algo aqui")

        botao1 = QPushButton("Botão 1", self)
        botao1.move(30, 40)
        botao1.resize(120, 30)
        botao1.setStyleSheet("QPushButton {background-color: #2E8B57; font: bold; font-size:15px}")
        botao1.clicked.connect(self.botao1_click)
        botao1.setToolTip("Esse é um: <b>Botão Verde</b>")

        botao2 = QPushButton("Botão 2", self)
        botao2.move(200, 40)
        botao2.resize(120, 30)
        botao2.setStyleSheet("QPushButton {background-color: #CD5C5C; font: bold; font-size:15px}")
        botao2.clicked.connect(self.botao2_click)
        botao2.setToolTip("Esse é um: <b>Botão Vermelho</b>")

        botao3 = QPushButton("Botão 3", self)
        botao3.move(250, 200)
        botao3.resize(80, 30)
        botao3.setStyleSheet("QPushButton {background-color: #4169E1; font: bold; font-size:15px}")
        botao3.clicked.connect(self.botao3_click)
        botao3.setToolTip("Esse é um: <b>Botão Azul</b>")

        self.label1 = QLabel(self)
        self.label1.setText("Esquerdo")
        self.label1.move(30, 10)
        self.label1.setStyleSheet("QLabel {font: bold; font-size: 15px}")
        self.label1.resize(200, 20)

        self.label2 = QLabel(self)
        self.label2.setText("Direito")
        self.label2.move(200, 10)
        self.label2.setStyleSheet("QLabel {font: bold; font-size: 15px}")
        self.label2.resize(200, 20)

        self.label3 = QLabel(self)
        self.label3.setText("Digite algo para teste: ")
        self.label3.move(30, 235)
        self.label3.setStyleSheet("QLabel {font: bold; font-size: 15px}")
        self.label3.resize(200, 20)

        self.among_green = QLabel(self)
        self.among_green.move(30, 80)
        self.among_green.setPixmap(QtGui.QPixmap("among_green_right.png"))
        self.among_green.resize(120, 120)

        self.among_red = QLabel(self)
        self.among_red.move(200, 80)
        self.among_red.setPixmap(QtGui.QPixmap("among_red_left.png"))
        self.among_red.resize(120, 120)

        self.carregajanela()

    def carregajanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print("Botão 1 Pressionado")
        self.label1.setText("Botão 1 Pressionado")
        self.among_green.setPixmap(QtGui.QPixmap("among_green_left.png"))
        self.label1.setStyleSheet("QLabel {color: #2E8B57; font: bold; font-size: 15px}")

    def botao2_click(self):
        print("Botão 2 Pressionado")
        self.label2.setText("Botão 2 Pressionado")
        self.among_red.setPixmap(QtGui.QPixmap("among_red_right.png"))
        self.label2.setStyleSheet("QLabel {color: #CD5C5C; font: bold; font-size: 15px}")

    def botao3_click(self):
        self.among_green.setPixmap(QtGui.QPixmap("among_green_right.png"))
        self.among_red.setPixmap(QtGui.QPixmap("among_red_left.png"))
        self.label1.setText("Esquerdo")
        self.label2.setText("Direito")
        self.label1.setStyleSheet("QLabel {font: bold; font-size: 15px}")
        self.label2.setStyleSheet("QLabel {font: bold; font-size: 15px}")
        conteudo = self.caixa_texto.text()
        self.label3.setText("Você digitou: " + '<b>' + conteudo.upper() + '</b>')
        self.label3.setStyleSheet("QLabel {color: #4169E1; font: italic; font-size: 15px}")


aplicacao = QApplication(sys.argv)
janela = Janela()
sys.exit(aplicacao.exec())
