from enum import nonmember

import _mysql_connector
import mysql.connector
from PySide6.QtWidgets import QApplication, QWidget,QMainWindow
from Interfaces.ui_login import Ui_Login  # Importa la clase generada automáticamente
from Interfaces.ui_menu import Ui_MainWindowMenu as menuPrincipal
from Interfaces.ui_registro import Ui_FormRegistro as registro
from Interfaces.ui_juego import Ui_FormJuego as juego
from Interfaces.ui_estadistica import Ui_FormEstats as estats
from Interfaces.ui_lobby import Ui_FormLobby as lobby

# Conexion a la base de datos:
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Galletas123",
            database="bd_juego"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None




class LoginWindow(QWidget):  # Hereda de QWidget, ya que tu archivo generado es un widget
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)  # Configura la interfaz en esta ventana



class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = registro()
        self.ui.setupUi(self)

class JuegoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = juego()
        self.ui.setupUi(self)

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = menuPrincipal
        self.ui.setupUi(self)

class EstadisticaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = estats
        self.ui.setupUi(self)

class LobbyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = lobby
        self.ui.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = LoginWindow()  # Instancia la ventana de login
    window.show()  # Muestra la ventana
    sys.exit(app.exec())  # Ejecuta la aplicación
