import pymysql
import socket
import netifaces
import threading
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QInputDialog
from Interfaces.ui_login import Ui_Login
from Interfaces.ui_menu import Ui_Menu as MenuPrincipalUI
from Interfaces.ui_registro import Ui_FormRegistro as UiRegistro
from Interfaces.ui_juego import Ui_FormJuego
from Interfaces.ui_estadistica import Ui_FormEstats as UiEstats
from Interfaces.ui_lobby import Ui_FormLobby as UiLobby

# Configuración de la base de datos
DB_CONFIG = {
    "charset": "utf8mb4",
    "connect_timeout": 10,
    "cursorclass": pymysql.cursors.DictCursor,
    "db": "defaultdb",
    "host": "mysql-proyecto-lenguajes-proyectolenguajes.d.aivencloud.com",
    "password": "AVNS_s86R96S1f5nR-YxSrxF",
    "read_timeout": 10,
    "port": 24276,
    "user": "avnadmin",
    "write_timeout": 10,
}


class MenuPrincipal(QMainWindow):
    """Ventana principal del menú después de iniciar sesión."""

    def __init__(self):
        super().__init__()
        self.ui = MenuPrincipalUI()
        self.ui.setupUi(self)
        self.ui.btnJugar.clicked.connect(self.abrir_ventana_lobby)

    def abrir_ventana_lobby(self):
        """Abre la ventana de lobby."""
        self.lobby_ventana = LobbyWindow()
        self.lobby_ventana.show()


class LoginWindow(QWidget):
    """Ventana de inicio de sesión."""

    def __init__(self):
        super().__init__()
        self.registro_ventana = RegisterWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.btnRegistro.clicked.connect(self.abrir_ventana_registro)
        self.ui.btnLogin.clicked.connect(self.login_usuario)

    def abrir_ventana_registro(self):
        """Abre la ventana de registro."""
        self.registro_ventana.show()

    def login_usuario(self):
        """Intenta iniciar sesión con las credenciales proporcionadas."""
        usuario = self.ui.txtUsuario.text()
        password = self.ui.txtPass.text()

        if usuario and password:
            self._try_login(usuario, password)
        else:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")

    def _try_login(self, usuario, password):
        """Valida el inicio de sesión contra la base de datos."""
        connection = self._get_db_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s AND contraseña = %s",
                           (usuario, password))
            result = cursor.fetchone()

            if result:
                QMessageBox.information(self, "Login", "Inicio de sesión exitoso.")
                self.abrir_menu_principal()
            else:
                QMessageBox.warning(self, "Login", "Usuario o contraseña incorrectos.")

    def abrir_menu_principal(self):
        """Abre el menú principal."""
        self.menu_ventana = MenuPrincipal()
        self.menu_ventana.show()

    def _get_db_connection(self):
        """Devuelve una conexión a la base de datos usando pymysql."""
        return pymysql.connect(**DB_CONFIG)


class RegisterWindow(QWidget):
    """Ventana para la creación de nuevos usuarios."""

    def __init__(self):
        super().__init__()
        self.ui = UiRegistro()
        self.ui.setupUi(self)
        self.ui.btnCrearUsr.clicked.connect(self.registrar_usuario)

    def registrar_usuario(self):
        """Registra un nuevo usuario en la base de datos."""
        usuario = self.ui.txtUsuario.text()
        password = self.ui.txtPass.text()

        if usuario and password:
            connection = pymysql.connect(**DB_CONFIG)
            try:
                with connection:
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO usuarios (nombre_usuario, contraseña) VALUES (%s, %s)",
                                   (usuario, password))
                    connection.commit()
                    QMessageBox.information(self, "Registro", "Usuario registrado exitosamente.")
                    self.close()
            except pymysql.MySQLError as err:
                QMessageBox.critical(self, "Error", f"No se pudo registrar el usuario: {err}")
        else:
            QMessageBox.warning(self, "Campos vacíos", "Por favor, complete todos los campos.")


class JuegoWindow(QWidget, Ui_FormJuego):
    """Ventana para el juego Tic-Tac-Toe."""

    def __init__(self, socket_instance=None, is_host=False):
        super().__init__()
        self.setupUi(self)
        self.turn = 0
        self.times = 0
        self.buttons = [
            [self.pushButton, self.pushButton_2, self.pushButton_3],
            [self.pushButton_4, self.pushButton_5, self.pushButton_6],
            [self.pushButton_7, self.pushButton_8, self.pushButton_9],
        ]
        self.btnReiniciar.clicked.connect(self.reset_game_action)
        self.btnSalir.clicked.connect(self.close)
        self.socket_instance = socket_instance
        self.is_host = is_host
        self.my_turn = is_host

        for row in self.buttons:
            for button in row:
                button.clicked.connect(self.button_clicked)

        if self.socket_instance:
            threading.Thread(target=self.receive_data, daemon=True).start()

    def button_clicked(self):
        if not self.my_turn:
            QMessageBox.warning(self, "Turno", "Espera tu turno.")
            return

        button = self.sender()
        if button.isEnabled():
            self.handle_turn(button)
            self.send_move(button)

    def handle_turn(self, button):
        button.setEnabled(False)
        button.setText("X" if self.turn == 0 else "O")
        self.turn = 1 - self.turn
        self.times += 1
        self.my_turn = False

        if self.check_winner():
            self.lblGanador.setText(f"{'O' if self.turn == 0 else 'X'} Ganó")
            self.disable_all_buttons()
        elif self.times == 9:
            self.lblGanador.setText("Empate")

    def send_move(self, button):
        try:
            index = [(row.index(button), col) for col, row in enumerate(self.buttons) if button in row][0]
            self.socket_instance.sendall(f"{index[0]},{index[1]}".encode())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo enviar el movimiento: {e}")

    def receive_data(self):
        while True:
            try:
                data = self.socket_instance.recv(1024)
                if data:
                    row, col = map(int, data.decode().split(","))
                    button = self.buttons[row][col]
                    self.handle_turn(button)
                    self.my_turn = True
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al recibir datos: {e}")
                break

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
        self.my_turn = self.is_host

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != "":
                return True
            if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != "":
                return True

        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != "":
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != "":
            return True
        return False


class LobbyWindow(QWidget):
    """Ventana del lobby del juego."""

    def __init__(self):
        super().__init__()
        self.ui = UiLobby()
        self.ui.setupUi(self)
        self.ui.btnCrearPartida.clicked.connect(self.crear_partida)
        self.ui.btnUnirse.clicked.connect(self.unirse_a_partida)
        self.ui.pushButton.clicked.connect(self.iniciar_juego_host)
        self.server_socket = None
        self.client_socket = None
        self.connection_accepted = False
        self.fixed_port = 5051

    def crear_partida(self):
        try:
            interfaces = self.obtener_interfaces_de_red()
            if not interfaces:
                raise Exception("No se encontraron interfaces de red activas con direcciones IPv4 válidas.")

            interface_names = [f"{name} ({ip})" for name, ip in interfaces.items()]
            selected_interface, ok = QInputDialog.getItem(
                self, "Seleccionar Interfaz de Red",
                "Seleccione una interfaz para iniciar el servidor:",
                interface_names, 0, False
            )

            if ok and selected_interface:
                ip_address = selected_interface.split("(")[-1].strip(" )")
                if not ip_address or ip_address == '0.0.0.0':
                    raise Exception("Seleccionaste una interfaz sin una dirección IP válida.")

                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.server_socket.bind((ip_address, self.fixed_port))
                self.server_socket.listen(1)

                self.ui.lbIdGenerado.setText(f"{ip_address}:{self.fixed_port}")
                QMessageBox.information(self, "Servidor",
                                        f"Servidor iniciado en:\nIP: {ip_address}\nPuerto: {self.fixed_port}")

                threading.Thread(target=self.aceptar_conexion, daemon=True).start()
            else:
                QMessageBox.warning(self, "Advertencia", "No seleccionaste ninguna interfaz.")
        except Exception as e:
            QMessageBox.critical(self, "Error del Servidor", f"Fallo al iniciar el servidor: {e}")

    def aceptar_conexion(self):
        conn, _ = self.server_socket.accept()
        self.connection_accepted = True
        self.client_socket = conn
        QMessageBox.information(self, "Conexión", "Un jugador se ha conectado.")

    def iniciar_juego_host(self):
        if self.connection_accepted and self.server_socket:
            try:
                self.client_socket.sendall("INICIAR_JUEGO".encode())
                self.iniciar_juego(self.client_socket, is_host=True)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo iniciar el juego: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Aún no hay un jugador conectado.")

    def unirse_a_partida(self):
        server_info = self.ui.lineEdit.text().strip()
        if ":" in server_info:
            try:
                ip_address, port = server_info.split(":")
                port = int(port)

                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((ip_address, port))

                QMessageBox.information(self, "Cliente",
                                        f"Conectado exitosamente al servidor:\nIP: {ip_address}\nPuerto: {port}")

                threading.Thread(target=self.esperar_inicio_juego, daemon=True).start()
            except Exception as e:
                QMessageBox.critical(self, "Error de Cliente", f"No se pudo conectar al servidor:\n{e}")
        else:
            QMessageBox.warning(self, "Error", "Por favor, ingrese una IP y puerto válidos en el formato IP:Puerto.")

    def esperar_inicio_juego(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if data.decode() == "INICIAR_JUEGO":
                    self.iniciar_juego(self.client_socket, is_host=False)
                    break
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al esperar inicio del juego: {e}")
                break

    def iniciar_juego(self, socket_instance, is_host):
        self.juego_ventana = JuegoWindow(socket_instance, is_host)
        self.juego_ventana.show()
        self.close()

    def obtener_interfaces_de_red(self):
        interfaces = {}
        for interface in netifaces.interfaces():
            try:
                address_info = netifaces.ifaddresses(interface).get(netifaces.AF_INET, [{}])
                for addr in address_info:
                    ip = addr.get('addr')
                    if ip and not ip.startswith('127.') and ip != '0.0.0.0':
                        interfaces[interface] = ip
            except Exception as e:
                print(f"Error al leer información de la interfaz {interface}: {e}")
        return interfaces

    def closeEvent(self, event):
        try:
            if self.server_socket:
                self.server_socket.close()
            if self.client_socket:
                self.client_socket.close()
        except Exception:
            pass
        event.accept()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
