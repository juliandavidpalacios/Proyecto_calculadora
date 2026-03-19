import sys
from PySide6 import QtWidgets
from pantallacalculadora import Pantalla


class MockPresenter:
    """
    Objeto simulado que sustituye al Presenter real.
    Verifica que la Vista emite las señales del contrato.
    """

    def __init__(self, view):
        self.view = view
        # CORRECCIÓN: conectar a las señales (sig_*), no a los botones directamente
        self.view.sig_suma.connect(self.al_recibir_suma)
        self.view.sig_resta.connect(self.al_recibir_resta)
        self.view.sig_multi.connect(self.al_recibir_multiplicacion)
        self.view.sig_division.connect(self.al_recibir_division)
        print("MOCK: Presenter conectado a las 4 señales de la Vista.")

    def al_recibir_suma(self):
        if not self.view.verificar_entradas():
            return
        print("\n[OK] MOCK: Señal de SUMA recibida.")
        print("MOCK: Ordenando a la vista mostrar '99.999'...")
        self.view.salida(99.999)

    def al_recibir_resta(self):
        if not self.view.verificar_entradas():
            return
        print("\n[OK] MOCK: Señal de RESTA recibida.")
        print("MOCK: Ordenando a la vista mostrar '-99.999'...")
        self.view.salida(-99.999)

    def al_recibir_multiplicacion(self):
        if not self.view.verificar_entradas():
            return
        # CORRECCIÓN: había dos métodos con el mismo nombre
        print("\n[OK] MOCK: Señal de MULTIPLICACIÓN recibida.")
        print("MOCK: Ordenando a la vista mostrar '55.999'...")
        self.view.salida(55.999)

    def al_recibir_division(self):
        if not self.view.verificar_entradas("division"):
            return
        # CORRECCIÓN: método renombrado correctamente
        print("\n[OK] MOCK: Señal de DIVISIÓN recibida.")
        print("MOCK: Ordenando a la vista mostrar '-55.999'...")
        self.view.salida(-55.999)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    vista = Pantalla()
    tester = MockPresenter(vista)

    vista.show()
    print("Iniciando prueba... Pulsa cualquier botón de operación en la calculadora.")
    sys.exit(app.exec())