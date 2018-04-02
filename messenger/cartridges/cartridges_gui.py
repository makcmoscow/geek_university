import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('add_printer.ui')
print(window.add_new_model_printer)
window.show()
def add():
    print('добавлено')

sys.exit(app.exec_())


