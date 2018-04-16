import sys
from PyQt5 import QtWidgets, uic

class Mainwindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = uic.loadUi('main_window.ui')
        self.window.show()


    def start(self):
        self.window.comboBox.activated[str].connect(start_add_printer)
        self.app.exec_()




class AddPrinter:
    def __init__(self):
        self.app1 = QtWidgets.QApplication(sys.argv)
        self.window = uic.loadUi('add_printer.ui')
        self.window.show()
        self.good_fields = {}
        self.error = True
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
        self.window.room_number.editingFinished.connect(self.input_m)
        # старт окна
        self.app1.exec_()
        if self.error:
            self.good_fields = {'error':'error'}
            return self.good_fields
        else:
            return self.good_fields


    def chk_all_right(self, fields):
        self.window.textBrowser.setText('')
        hfields = {'cart_red':'red', 'cart_blue': 'blue', 'cart_yellow':'yellow', 'model': 'Модель принтера', 'serial':'Серийный номер',
                   'cart_black':'black', 'room_number':'Номер комнаты'}
        for field in fields:
            if (field == 'cart_red' or field == 'cart_blue' or field == 'cart_yellow') and not self.window.check_color.isChecked():
                    pass
            else:
                if fields[field] is None:
                    self.error = True
                    self.window.textBrowser.append('Обязательное поле {} не заполнено'.format(hfields[field]))
                    self.window.show()
                    self.app1.exec_()

                else:
                    self.error = False
                    self.good_fields[field] = fields[field]
        # return self.good_fields


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


    def preparing(self):
        if self.window.radioButton_hp.isChecked():
            brand = 'HP'
        else:
            brand = 'XEROX'

        fields = dict.fromkeys(['brand', 'model', 'serial', 'cart_black', 'cart_red', 'cart_blue', 'cart_yellow', 'room_number'])
        fields['brand'] = brand
        fields['model'] = self.window.lineEdit_model.text()
        fields['serial'] = self.window.lineEdit_serial.text()
        fields['cart_black'] = self.window.cart_black.text()
        fields['room_number'] = self.window.room_number.text()
        if self.chk_color():
            fields['cart_red'] = self.window.cart_red.text()
            fields['cart_blue'] = self.window.cart_blue.text()
            fields['cart_yellow'] = self.window.cart_yellow.text()
        else:
            pass
        for field in fields.keys():
            self.fields = self.chk_len(field, fields)
        self.window.close()
        self.chk_all_right(self.fields)

    # функция-заглушка для обработки полей ввода
    def input_m(self):
        pass

    def exit_m(self):
        self.window.close()
        return self.good_fields

def start_add_printer():
    starter = AddPrinter()
    result = starter.start()
    print(result)
    return result



if __name__ == '__main__':
    starter = AddPrinter()

    print('total:', starter.start())
    # mainwindow = Mainwindow()
    # mainwindow.start()
