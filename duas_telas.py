from PyQt5 import QtWidgets
import uic


def chama_tela():
    segunda_tela.show()


def muda_texto():
    segunda_tela.label.setText("Botão Pressionado")


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
primeira_tela.pushButton.clicked.connect(chama_tela)
segunda_tela.pushButton.clicked.connect(muda_texto)

primeira_tela.show()
app.exec()
