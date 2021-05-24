from PyQt5 import QtWidgets
import uic


def menu_azul():
    tela.label.setStyleSheet("color: blue")
    tela.statusBar.showMessage("Selecionada a cor Azul")


def menu_verde():
    tela.label.setStyleSheet("color: green")
    tela.statusBar.showMessage("Selecionada a cor Verde")


def menu_vermelho():
    tela.label.setStyleSheet("color: red")
    tela.statusBar.showMessage("Selecionada a cor Vermelha")


app = QtWidgets.QApplication([])
tela = uic.loadUi("menu.ui")

tela.statusBar.showMessage("Aplicação Iniciada")

tela.actionAzul.triggered.connect(menu_azul)
tela.actionVerde.triggered.connect(menu_verde)
tela.actionVermelho.triggered.connect(menu_vermelho)


tela.show()
app.exec()
