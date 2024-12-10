import pymysql
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from Interfaces.ui_login import Ui_Login  # Importa la clase generada automáticamente
from Interfaces.ui_menu import Ui_Menu as menuPrincipal
from Interfaces.ui_registro import Ui_FormRegistro as registro
from Interfaces.ui_juego import Ui_FormJuego
from Interfaces.ui_estadistica import Ui_FormEstats as estats
from Interfaces.ui_lobby import Ui_FormLobby as lobby


class MenuPrincipal(QMainWindow):  # Cambiar QWidget a QMainWindow
    def __init__(self):
        super().__init__()
        self.ui = menuPrincipal()
        self.ui.setupUi(self)
        self.ui.btnJugar.clicked.connect(self.abrir_ventana_lobby)


    def abrir_ventana_lobby(self):
        self.lobby_ventana = LobbyWindow()
        self.lobby_ventana.show()


# Ventana Login
class LoginWindow(QWidget):  # Hereda de QWidget, ya que tu archivo generado es un widget
    def __init__(self):
        super().__init__()
        self.registro_ventana = RegisterWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self)  # Configura la interfaz en esta ventana
        self.ui.btnRegistro.clicked.connect(self.abrir_ventana_registro)
        self.ui.btnLogin.clicked.connect(self.login_usuario)  # Conectar el botón de login a la función

    def abrir_ventana_registro(self):
        self.registro_ventana.show()

    def login_usuario(self):
        usuario = self.ui.txtUsuario.text()
        password = self.ui.txtPass.text()

        if usuario and password:
            try:
                connection = pymysql.connect(
                    charset="utf8mb4",
                    connect_timeout=10,
                    cursorclass=pymysql.cursors.DictCursor,
                    db="defaultdb",
                    host="mysql-proyecto-lenguajes-proyectolenguajes.d.aivencloud.com",
                    password="AVNS_s86R96S1f5nR-YxSrxF",
                    read_timeout=10,
                    port=24276,
                    user="avnadmin",
                    write_timeout=10,
                )
                cursor = connection.cursor()
                # Consultar si el usuario existe y la contraseña es correcta
                cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s AND contraseña = %s",
                               (usuario, password))
                result = cursor.fetchone()
                cursor.close()
                connection.close()

                if result:
                    QMessageBox.information(self, "Login", "Inicio de sesión exitoso.")
                    self.abrir_menu_principal()
                else:
                    QMessageBox.warning(self, "Login", "Usuario o contraseña incorrectos.")
            except pymysql.MySQLError as err:
                QMessageBox.critical(self, "Error", f"No se pudo iniciar sesión: {err}")
                print(f"Error: {err}")
        else:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")

    def abrir_menu_principal(self):
        self.menu_ventana = MenuPrincipal()  # Instanciar MenuPrincipal
        self.menu_ventana.show()


# Ventana Registro
class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = registro()
        self.ui.setupUi(self)
        self.ui.btnCrearUsr.clicked.connect(self.registrar_usuario)

    def registrar_usuario(self):
        usuario = self.ui.txtUsuario.text()
        password = self.ui.txtPass.text()

        if usuario and password:
            try:
                # Establecer la conexión con pymysql
                connection = pymysql.connect(
                    charset="utf8mb4",
                    connect_timeout=10,
                    cursorclass=pymysql.cursors.DictCursor,
                    db="defaultdb",
                    host="mysql-proyecto-lenguajes-proyectolenguajes.d.aivencloud.com",
                    password="AVNS_s86R96S1f5nR-YxSrxF",
                    read_timeout=10,
                    port=24276,
                    user="avnadmin",
                    write_timeout=10,
                )
                cursor = connection.cursor()
                # Insertar nuevo usuario en la base de datos
                cursor.execute("INSERT INTO usuarios (nombre_usuario, contraseña) VALUES (%s, %s)",
                               (usuario, password))
                connection.commit()
                cursor.close()
                connection.close()
                QMessageBox.information(self, "Registro", "Usuario registrado exitosamente.")
                self.close()  # Cerrar la ventana de registro
            except pymysql.MySQLError as err:
                QMessageBox.critical(self, "Error", f"No se pudo registrar el usuario: {err}")
                print(f"Error: {err}")
        else:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")


class JuegoWindow(QWidget, Ui_FormJuego):  # Este bloque 'class JuegoWindow' ahora está en la indentación correcta
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz con los widgets

        # Variables de juego
        self.turn = 0
        self.times = 0

        self.buttons = [
            [self.pushButton, self.pushButton_2, self.pushButton_3],
            [self.pushButton_4, self.pushButton_5, self.pushButton_6],
            [self.pushButton_7, self.pushButton_8, self.pushButton_9],
        ]

        # Conectar botones a sus funciones
        for row in self.buttons:
            for button in row:
                button.clicked.connect(self.button_clicked)

        # Configurar botones de reinicio y salida
        self.btnReiniciar.clicked.connect(self.reset_game_action)
        self.btnSalir.clicked.connect(self.close)

    def button_clicked(self):
        button = self.sender()
        if button.isEnabled():
            button.setEnabled(False)
            button.setText("X" if self.turn == 0 else "O")
            self.turn = 1 - self.turn
            self.times += 1

            if self.check_winner():
                self.lblGanador.setText(f"{'O' if self.turn == 0 else 'X'} Ganó")
                self.disable_all_buttons()
            elif self.times == 9:
                self.lblGanador.setText("Empate")

    def disable_all_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

    def reset_game_action(self):
        self.turn = 0
        self.times = 0
        self.lblGanador.setText("")

        for row in self.buttons:
            for button in row:
                button.setEnabled(True)
                button.setText("")

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != "":
                return True
            if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != "":
                return True

        # Check diagonals
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != "":
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != "":
            return True

        return False


class EstadisticaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = estats()
        self.ui.setupUi(self)


class LobbyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = lobby()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = LoginWindow()  # Instancia la ventana de login
    window.show()  # Muestra la ventana
    sys.exit(app.exec())  # Ejecuta la aplicación
