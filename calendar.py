from PyQt5 import QtWidgets
import uic


def pegar_data():
    data = str(tela.calendarWidget.selectedDate())
    # print(data)
    data_tratada = data[18:]
    print(data_tratada)
    # dia = data[23:]
    # mes = data[23:]
    # ano = data[19:23]
    # print(dia, mes, ano)
    tela.label_2.setText(data_tratada)


app = QtWidgets.QApplication([])
tela = uic.loadUi("calendar.ui")

tela.calendarWidget.clicked.connect(pegar_data)

tela.show()
app.exec()
