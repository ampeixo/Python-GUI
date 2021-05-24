import sys
import uic
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem


class ListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("list_widget.ui")

        self.itemDoubleClicked.connect(self.get_item)

    def get_item(self, lstitem):
        print(self.currentItem().text())
        print(lstitem.text())
        print(self.currentRow())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    formulario = ListWidget()
    formulario.show()

    sys.exit(app.exec_())
