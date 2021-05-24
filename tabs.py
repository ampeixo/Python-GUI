from PyQt5 import QtWidgets
import uic


def metodo():
    tela.statusBar.showMessage("Click")


app = QtWidgets.QApplication([])
tela = uic.loadUi("tabs.ui")

tela.statusBar.showMessage("Aplicação Iniciada")
tela.tabWidget.tabBarClicked.connect(metodo)


tela.show()
app.exec()
