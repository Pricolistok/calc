import sys
from PyQt5.Qt import *
from logic import work_with_row


class Creator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.windowAboutCreator = QWidget()
        self.windowAboutCreator.setWindowTitle('About creator')
        self.windowAboutCreator.resize(400, 200)
        textboxAboutCreator = QLabel(self.windowAboutCreator)
        textboxAboutCreator.setText("Доколин Георгий ИУ7-22Б")
        textboxAboutCreator.move(50, 60)
        textboxAboutCreator.setFont(QFont('Comfortaa', 18))
        self.windowAboutCreator.show()


class Calc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window_about_prog = QWidget()
        self.window_about_prog.setWindowTitle('About programm')
        self.window_about_prog.resize(500, 200)
        textbox_about_creator = QLabel(self.window_about_prog)
        textbox_about_creator.setText("Приложение умножает, складывает, \nвычитает числа в двоичной "
                                      "\nсистеме счисления")
        textbox_about_creator.move(2, 40)
        textbox_about_creator.setFont(QFont('Comfortaa', 18))
        self.window_about_prog.show()


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.answer = ''
        self.window = QWidget()
        self.window.setWindowTitle('Calculator')
        type_font = 'Comfortaa'
        self.grid = QGridLayout(self.window)
        self.menubar = QMenuBar(self.window)
        self.grid.addWidget(self.menubar)
        inform = self.menubar.addMenu('INFO')
        inform.addAction('About creator').triggered.connect(self.about_creator_func)
        inform.addAction('About programm').triggered.connect(self.about_programm_func)
        font_size = 18
        self.row_for_calc = ''
        size_x, size_y = 60, 60

        self.row_input = QLineEdit()
        self.row_input.setFixedSize(260, 40)
        self.row_input.setFont(QFont(type_font, font_size))
        self.grid.addWidget(self.row_input, 1, 0, 1, 4, alignment=Qt.AlignCenter)

        self.btn_0 = QPushButton('0')
        self.grid.addWidget(self.btn_0, 2, 2, 2, 3, alignment=Qt.AlignCenter)
        self.btn_0.clicked.connect(lambda: self.create_row('0'))
        self.btn_0.setFixedSize(size_x * 2 + 3, size_y)
        self.btn_0.setFont(QFont(type_font, font_size))

        self.btn_1 = QPushButton('1')
        self.grid.addWidget(self.btn_1, 2, 0, 2, 2, alignment=Qt.AlignCenter)
        self.btn_1.clicked.connect(lambda: self.create_row('1'))
        self.btn_1.setFixedSize(size_x * 2 + 5, size_y)
        self.btn_1.setFont(QFont(type_font, font_size))

        self.btn_dot = QPushButton('.')
        self.grid.addWidget(self.btn_dot, 4, 2, alignment=Qt.AlignCenter)
        self.btn_dot.clicked.connect(lambda: self.create_row('.'))
        self.btn_dot.setFixedSize(size_x, size_y)
        self.btn_dot.setFont(QFont(type_font, font_size))

        self.btn_enter = QPushButton('Enter')
        self.grid.addWidget(self.btn_enter, 2, 4, 3, 5, alignment=Qt.AlignCenter)
        self.btn_enter.clicked.connect(self.enter)
        self.btn_enter.setFixedSize(size_x * 2 + 4, size_y * 2)
        self.btn_enter.setFont(QFont(type_font, font_size))

        self.btn_plus = QPushButton('+')
        self.grid.addWidget(self.btn_plus, 4, 0, alignment=Qt.AlignCenter)
        self.btn_plus.clicked.connect(lambda: self.create_row('+'))
        self.btn_plus.setFixedSize(size_x, size_y)
        self.btn_plus.setFont(QFont(type_font, font_size))

        self.btn_minus = QPushButton('-')
        self.grid.addWidget(self.btn_minus, 4, 1, alignment=Qt.AlignCenter)
        self.btn_minus.clicked.connect(lambda: self.create_row('-'))
        self.btn_minus.setFixedSize(size_x, size_y)
        self.btn_minus.setFont(QFont(type_font, font_size))

        self.btn_multiplication = QPushButton('*')
        self.grid.addWidget(self.btn_multiplication, 4, 3, alignment=Qt.AlignCenter)
        self.btn_multiplication.clicked.connect(lambda: self.create_row('*'))
        self.btn_multiplication.setFixedSize(size_x, size_y)
        self.btn_multiplication.setFont(QFont(type_font, font_size))

        self.btn_ac = QPushButton('AC')
        self.grid.addWidget(self.btn_ac, 1, 5)
        self.btn_ac.clicked.connect(lambda: self.clean_row())
        self.btn_ac.setFixedSize(size_x, size_y)
        self.btn_ac.setFont(QFont(type_font, font_size))

        self.btn_delete = QPushButton('<=')
        self.grid.addWidget(self.btn_delete, 1, 6)
        self.btn_delete.clicked.connect(lambda: self.delete_last())
        self.btn_delete.setFixedSize(size_x, size_y)
        self.btn_delete.setFont(QFont(type_font, font_size))

        self.window.show()

    def enter(self):
        from_line = self.row_input.text()
        try:
            if self.row_for_calc != from_line:
                self.answer = work_with_row(from_line)
            else:
                if self.row_for_calc == '':
                    self.answer = 'Error'
                    self.row_for_calc = ''
                else:
                    self.answer = work_with_row(self.row_for_calc)
        except ValueError:
            self.answer = 'Error'
            self.row_for_calc = ''
        self.row_input.setText(self.answer)

    def keyPressEvent(self, event):
        e = event.key()
        if e == Qt.Key_Return:
            print('fghjk')
            self.enter()

    def create_row(self, elem):
        self.row_for_calc = self.row_input.text() + elem
        self.row_input.setText(self.row_for_calc)

    def clean_row(self):
        self.row_for_calc = ''
        self.row_input.setText(self.row_for_calc)

    def delete_last(self):
        self.row_for_calc = self.row_input.text()[0:-1]
        self.row_input.setText(self.row_for_calc)

    def about_creator_func(self):
        self.creator_inform = Creator()

    def about_programm_func(self):
        self.programm_inform = Calc()



def main():
    # Create app and window
    app = QApplication([])
    ex = App()
    ex.setStyle(QStyleFactory.create('CDEstyle'))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
