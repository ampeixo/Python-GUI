from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import uic
import sys


def preenche_lista_inicial():
    jan = 'Janaury'
    feb = 'February'
    mar = 'March'
    apr = 'April'
    may = 'May'
    jun = 'June'

    formulario.listWidget.addItem(jan)
    formulario.listWidget.addItem(feb)
    formulario.listWidget.addItems([apr, jun])
    formulario.listWidget.insertItem(2, mar)
    formulario.listWidget.insertItem(4, may)


def preenche_lista():
    meses = ['Janaury', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
             'September', 'October', 'November', 'December']
    for mes in meses:
        formulario.listWidget.addItem(mes)


def envia_dado():
    dado = formulario.lineEdit.text()
    if dado != "":
        formulario.listWidget.addItem(dado)
        formulario.lineEdit.setText("")
    else:
        print("insira algum dado")
        formulario.lineEdit.setText("")


def limpa_dados():
    formulario.listWidget.clear()


def deleta_item():
    formulario.listWidget.takeItem(formulario.listWidget.currentRow())


def get_item():
    try:
        item = formulario.listWidget.currentItem().text()
        print(item)
        QMessageBox.about(formulario, "Info", item)
    except AttributeError:
        print("selecione uma opção")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    formulario = uic.loadUi("list_widget.ui")
    formulario.show()

    preenche_lista_inicial()

    formulario.listWidget.itemDoubleClicked.connect(get_item)
    formulario.pushButton.clicked.connect(envia_dado)
    formulario.pushButton_2.clicked.connect(limpa_dados)
    formulario.pushButton_3.clicked.connect(deleta_item)
    formulario.pushButton_4.clicked.connect(get_item)
    formulario.pushButton_5.clicked.connect(preenche_lista)

    app.exec()
