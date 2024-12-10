from PySide6.QtWidgets import QApplication, QWidget
from Interfaces.ui_login import Ui_Login  # Importa la clase generada automáticamente
from Interfaces.ui_menu import Ui_MainWindowMenu as Menu
from Interfaces.ui_registro import Ui_FormRegistro
from Interfaces.ui_juego import Ui_FormJuego
from Interfaces.ui_estadistica import Ui_FormEstats

class LoginWindow(QWidget):  # Hereda de QWidget, ya que tu archivo generado es un widget
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)  # Configura la interfaz en esta ventana

        # Conecta los botones a funciones específicas
        self.ui.btnLogin.clicked.connect(self.handle_login)
        self.ui.btnRegistro.clicked.connect(self.handle_register)

    def handle_login(self):
        # Obtén los textos de los campos de usuario y contraseña
        username = self.ui.textEdit.toPlainText()
        password = self.ui.textEdit_2.toPlainText()
        # Realiza alguna lógica de validación (ejemplo)
        if username == "admin" and password == "1234":
            print("Login exitoso")
        else:
            print("Usuario o contraseña incorrectos")

    def handle_register(self):
        print("Registro de nuevo usuario")





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = LoginWindow()  # Instancia la ventana de login
    window.show()  # Muestra la ventana
    sys.exit(app.exec())  # Ejecuta la aplicación
