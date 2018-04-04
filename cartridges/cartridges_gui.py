import sys
from PyQt5 import QtWidgets, uic

class Starter:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = uic.loadUi('add_printer.ui')
        self.window.show()
        self.data = []

    def start(self):

        # Обработка кнопок ОК/Отмена
        self.window.pushOK.clicked.connect(self.preparing)
        self.window.pushCancel.clicked.connect(self.exit_m)

        # Обработка полей ввода
        self.window.lineEdit_model.editingFinished.connect(self.input_m)
        self.window.lineEdit_serial.editingFinished.connect(self.input_m)
        self.window.cart_black.editingFinished.connect(self.input_m)
        self.window.cart_red.editingFinished.connect(self.input_m)
        self.window.cart_blue.editingFinished.connect(self.input_m)
        self.window.cart_yellow.editingFinished.connect(self.input_m)
        self.window.check_color.clicked.connect(self.chk_color)
        # старт окна
        self.app.exec_()
        # sys.exit(self.app.exec_())
        # sys.exit(app.exec_())
        return self.data

    def add(self):
        print(self.preparing())

    def chk_all_right(self):
        pass

    def chk_len(self, field, fields):
        if fields[field]:
            if len(fields[field])>2:
                pass
            else:
                fields[field] = None
            return fields
        else:
            fields[field] = None
            return  fields

    def chk_color(self):
        try:
            if self.window.check_color.isChecked():
                self.window.cart_red.setEnabled(True)
                self.window.cart_blue.setEnabled(True)
                self.window.cart_yellow.setEnabled(True)
                return True
            else:
                self.window.cart_red.setEnabled(False)
                self.window.cart_blue.setEnabled(False)
                self.window.cart_yellow.setEnabled(False)
                return False
        except Exception as e:
            print(e)

    def preparing(self):
        if self.window.radioButton_hp.isChecked():
            brand = 'HP'
        else:
            brand = 'XEROX'

        fields = dict.fromkeys(['brand', 'model', 'serial', 'cart_black', 'cart_red', 'cart_blue', 'cart_yellow'])
        fields['brand'] = brand
        fields['model'] = self.window.lineEdit_model.text()
        fields['serial'] = self.window.lineEdit_serial.text()
        fields['cart_black'] = self.window.cart_black.text()
        if self.chk_color():
            try:
                fields['cart_red'] = self.window.cart_red.text()
                fields['cart_blue'] = self.window.cart_blue.text()
                fields['cart_yellow'] = self.window.cart_yellow.text()
            except Exception as e:
                print(e)
        else:
            pass
        for field in fields.keys():
            self.fields = self.chk_len(field, fields)

        self.exit_m()

    # функция-заглушка для обработки полей ввода
    def input_m(self):
        pass

    def exit_m(self):
        self.window.close()
        print(self.fields)
        return(self.fields)

if __name__ == '__main__':
    starter = Starter()

    starter.start()
    print(starter.fields)
