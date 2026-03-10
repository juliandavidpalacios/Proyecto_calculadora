from PySide6 import QtWidgets
from pantalla import Ui_Dialog as form_class

class PantallaCalculadora(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def opera(self):
        pass
    def verificar(self):
        pass
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = PantallaCalculadora()
    window.show()
    app.exec()