from PyQt5 import QtWidgets
import uic


def aumenta_valor():
    global valor
    if valor <= 90:
        valor = valor + 10
        tela.progressBar.setValue(valor)
        print(valor)
    else:
        print("Atingiu valor limite superior")


def diminiu_valor():
    global valor
    if valor > 0:
        valor = valor - 10
        tela.progressBar.setValue(valor)
        print(valor)
    else:
        print("Atingiu valor limite inferior")


def zera_valor():
    global valor
    valor = 0
    tela.progressBar.setValue(valor)


app = QtWidgets.QApplication([])
tela = uic.loadUi("progress_bar.ui")

tela.pushButton.clicked.connect(aumenta_valor)
tela.pushButton_2.clicked.connect(diminiu_valor)
tela.pushButton_3.clicked.connect(zera_valor)

valor = 0


tela.show()
app.exec()
