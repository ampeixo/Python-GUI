from PyQt5 import QtWidgets
import uic


def principal():
    if formulario.azul.isChecked():
        opcao = "Opção Azul"
        formulario.label_3.setStyleSheet("QLabel {color: rgb(0, 85, 255); font: bold;}")
    elif formulario.vermelho.isChecked():
        opcao = "Opção Vermelho"
        formulario.label_3.setStyleSheet("QLabel {color: rgb(170, 0, 0); font: bold;}")
    elif formulario.verde.isChecked():
        opcao = "Opção Verde"
        formulario.label_3.setStyleSheet("QLabel {color: rgb(0, 85, 0); font: bold;}")
    elif formulario.amarelo.isChecked():
        opcao = "Opção Amarelo"
        formulario.label_3.setStyleSheet("QLabel {color: rgb(203, 203, 0); font: bold;}")
    else:
        opcao = "Nenhuma opção"
        formulario.label_3.setStyleSheet("QLabel {color: rgb(0, 0, 0); font: bold;}")

    formulario.label_3.setText(opcao)


app = QtWidgets.QApplication([])
formulario = uic.loadUi("radio_buttons.ui")
formulario.pushButton.clicked.connect(principal)

formulario.show()
app.exec()
