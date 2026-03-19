from PySide6 import QtWidgets, QtCore
from ui_calculadora import Ui_Calculadora as form_class


class Pantalla(QtWidgets.QMainWindow, form_class):
    # 1. Una señal por operación
    sig_suma = QtCore.Signal()
    sig_resta = QtCore.Signal()
    sig_multi = QtCore.Signal()
    sig_division = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 2. Conectar cada botón a su señal
        self.btsuma.clicked.connect(self.sig_suma)
        self.btresta.clicked.connect(self.sig_resta)
        self.btmulti.clicked.connect(self.sig_multi)
        self.btdivi.clicked.connect(self.sig_division)
        # 3. Botón salir
        self.btsalida.clicked.connect(self.close)

    def verificar_entradas(self, operacion=None):
        """
        Checks inputs before the Presenter processes them.
        Returns True if inputs are valid, False otherwise.
        - operacion: pass 'division' to also check for divide-by-zero.
        """
        texto1 = self.entrada1.text().strip()
        texto2 = self.entrada2.text().strip()

        # Check fields are not empty
        if texto1 == "" or texto2 == "":
            self.resultado.setText("Error: campos vacíos")
            return False

        # Check both inputs are valid numbers
        try:
            a = float(texto1)
            b = float(texto2)
        except ValueError:
            self.resultado.setText("Error: solo números")
            return False

        # Check divide by zero
        if operacion == "division" and b == 0:
            self.resultado.setText("Error: división por 0")
            return False

        return True

    def enviar_numeros(self):
        """El Presenter llama esto para obtener los dos operandos."""
        a = float(self.entrada1.text())
        b = float(self.entrada2.text())
        return a, b

    def salida(self, valor):
        """El Presenter llama esto para mostrar el resultado."""
        self.resultado.setText(str(valor))  # CORRECCIÓN: era 'resultado' (variable inexistente)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pantalla = Pantalla()
    pantalla.show()
    sys.exit(app.exec())