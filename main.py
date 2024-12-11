import pymysql
import socket
import netifaces
import threading
import requests
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QInputDialog
from PySide6.QtCore import Signal, QObject
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

    def __init__(self, usuario):
        super().__init__()
        self.ui = MenuPrincipalUI()
        self.ui.setupUi(self)
        self.usuario = usuario  # Guardamos el nombre del usuario que inició sesión
        self.ui.btnJugar.clicked.connect(self.abrir_ventana_lobby)

    def abrir_ventana_lobby(self):
        """Abre la ventana de lobby y pasa el nombre del usuario."""
        self.lobby_ventana = LobbyWindow(self.usuario)
        self.lobby_ventana.show()
        self.close()  # Cerramos esta ventana


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
                self.abrir_menu_principal(usuario)  # Pasamos el nombre del usuario
            else:
                QMessageBox.warning(self, "Login", "Usuario o contraseña incorrectos.")

    def abrir_menu_principal(self, usuario):
        """Abre el menú principal y pasa el nombre del usuario."""
        self.menu_ventana = MenuPrincipal(usuario)
        self.menu_ventana.show()
        self.close()

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

    def __init__(self, socket_instance=None, is_host=False,usuario_local=""):
        super().__init__()
        self.setupUi(self)
        self.turn = 0
        self.times = 0
        self.usuario_local = usuario_local.strip()  # Asegurarse de limpiar espacios en blanco
        self.usuario_oponente = None  # Inicialmente desconocido (lo obtenemos al conectar)
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

    def register_match(self, player1, player2, winner):
        """Registra las estadísticas de la partida en el Web Service. Solo ejecutado por el host."""
        if not self.is_host:
            print("El cliente no puede registrar las estadísticas en el Web Service.")
            return  # Prevención: Solo el host debe hacer esto

        url = "http://127.0.0.1:5000/register_match"  # URL del web service
        payload = {
            "player1": player1,
            "player2": player2,
            "winner": winner,
        }

        print(f"Intentando registrar match con los datos: {payload}")  # Depuración
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 201:
                print("Estadística registrada exitosamente.")
            else:
                print(f"Error al registrar estadística: {response.json()}")
        except requests.RequestException as e:
            print(f"Error de conexión al Web Service: {e}")

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

        # Validar sincronización de usuarios antes de continuar
        if not self.usuario_local or not self.usuario_oponente:
            QMessageBox.critical(self, "Error", "No se pudo encontrar el nombre de un jugador.")
            return  # Detener para evitar fallos

        if self.check_winner():
            winner = self.usuario_local if self.turn == 1 else self.usuario_oponente
            self.lblGanador.setText(f"{winner} Ganó")
            self.disable_all_buttons()

            # Registrar las estadísticas de la partida usando nombres reales
            self.register_match(self.usuario_local, self.usuario_oponente, winner)

        elif self.times == 9:
            self.lblGanador.setText("Empate")
            # Registrar un empate
            self.register_match(self.usuario_local, self.usuario_oponente, "draw")

    def send_move(self, button):
        try:
            index = [(row.index(button), col) for col, row in enumerate(self.buttons) if button in row][0]
            row, col = index
            row = 2 - row  # Reflejo vertical
            col = 2 - col  # Reflejo horizontal
            print(f"Enviando: row={row}, col={col}")  # Depuración
            self.socket_instance.sendall(f"{row},{col}".encode())
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo enviar el movimiento: {e}")

    def receive_data(self):
        """Recibe datos del oponente, sincronizando nombres, jugadas y resultados."""
        try:
            if not self.usuario_oponente:  # Ejecutar la sincronización al inicio
                if self.is_host:
                    self.socket_instance.sendall(self.usuario_local.encode())
                    self.usuario_oponente = self.socket_instance.recv(1024).decode()
                else:
                    self.usuario_oponente = self.socket_instance.recv(1024).decode()
                    self.socket_instance.sendall(self.usuario_local.encode())
                print(f"Sincronización completada: {self.usuario_local} vs {self.usuario_oponente}")

            # Mantener la conexión activa para recibir datos o resultados
            while True:
                data = self.socket_instance.recv(1024).decode()
                if data.startswith("RESULT:"):  # Procesar resultado si es necesario
                    self.recibir_resultado(data)
                    break  # Detener después de recibir el resultado final

                elif data:  # Datos de movimiento
                    row, col = map(int, data.split(","))
                    row = 2 - row  # Reflejo vertical
                    col = 2 - col  # Reflejo horizontal
                    button = self.buttons[row][col]
                    self.handle_turn(button)
                    self.my_turn = True

                else:
                    print("El servidor/cliente cerró la conexión.")
                    break
        except Exception as e:
            print(f"Error al recibir datos: {e}")
            self.close_socket()

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
        """Verifica si hay un ganador o empate y define el flujo según sea host o cliente."""
        winner_detected = None

        # Reglas de validación de filas, columnas y diagonales
        for i in range(3):
            if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != "":
                winner_detected = self.buttons[i][0].text()
            if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != "":
                winner_detected = self.buttons[0][i].text()

        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != "":
            winner_detected = self.buttons[0][0].text()
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != "":
            winner_detected = self.buttons[0][2].text()

        # Regla para empate
        is_draw = self.times == 9 and not winner_detected

        # Solo el host realiza las acciones finales
        if self.is_host:
            if winner_detected:
                winner_name = self.usuario_local if winner_detected == "X" else self.usuario_oponente
                self.enviar_resultado(winner_name)  # Enviar resultado al cliente
                self.register_match(self.usuario_local, self.usuario_oponente, winner_name)  # Registrar en el WS
            elif is_draw:
                self.enviar_resultado("draw")  # Enviar empate al cliente
                self.register_match(self.usuario_local, self.usuario_oponente, "draw")  # Registrar empate en el WS

        return winner_detected or is_draw

    def enviar_resultado(self, resultado):
        """Envía el resultado final del juego al cliente desde el host."""
        try:
            if self.is_host:
                message = f"RESULT:{resultado}"
                self.socket_instance.sendall(message.encode())  # Enviar el resultado
                self.mostrar_resultado(resultado)  # Mostrar en tu propia pantalla
        except Exception as e:
            print(f"Error al enviar el resultado: {e}")

    def recibir_resultado(self, message):
        """Recibe el resultado del host y lo aplica localmente."""
        if message.startswith("RESULT:"):
            resultado = message.split(":")[1]
            self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        """Muestra en la interfaz el resultado final."""
        if resultado == "draw":
            self.lblGanador.setText("Empate")
        else:
            self.lblGanador.setText(f"{resultado} Ganó!")

        self.disable_all_buttons()


    def close_socket(self):
        """Cerrar el socket de forma segura."""
        try:
            if self.socket_instance:
                self.socket_instance.shutdown(socket.SHUT_RDWR)
                self.socket_instance.close()
        except socket.error as e:
            print(f"Error al cerrar el socket: {e}")
        except Exception as e:
            print(f"Error inesperado al cerrar el socket: {e}")
        finally:
            self.socket_instance = None


class LobbyWindow(QWidget):
    """Ventana del lobby del juego."""

    # Definimos una señal personalizada para manejar la conexión en el hilo principal
    conexion_exitosa = Signal(object)

    def __init__(self, usuario):
        super().__init__()
        self.ui = UiLobby()
        self.ui.setupUi(self)
        self.usuario = usuario  # Guardamos el nombre del usuario
        self.ui.btnCrearPartida.clicked.connect(self.crear_partida)
        self.ui.btnUnirse.clicked.connect(self.unirse_a_partida)
        self.server_socket = None
        self.client_socket = None
        self.fixed_port = 5051

        # Conexión de la señal para manejar la apertura del juego en el hilo principal
        self.conexion_exitosa.connect(self.iniciar_juego)

    def crear_partida(self):
        """Inicia el servidor y espera conexiones."""
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
                self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.server_socket.bind((ip_address, self.fixed_port))
                self.server_socket.listen(1)

                self.ui.lbIdGenerado.setText(f"{ip_address}:{self.fixed_port}")
                QMessageBox.information(self, "Servidor",
                                        f"Servidor iniciado en:\nIP: {ip_address}\nPuerto: {self.fixed_port}")

                # Crear un hilo para aceptar la conexión
                threading.Thread(target=self.aceptar_conexion, daemon=True).start()
            else:
                QMessageBox.warning(self, "Advertencia", "No seleccionaste ninguna interfaz.")
        except Exception as e:
            QMessageBox.critical(self, "Error del Servidor", f"Fallo al iniciar el servidor: {e}")

    def aceptar_conexion(self):
        """Espera una conexión de cliente y lanza la partida."""
        try:
            conn, _ = self.server_socket.accept()  # Esperamos una conexión
            # Conexión exitosa: Emitimos una señal para pasar al método iniciar_juego desde el hilo principal.
            self.conexion_exitosa.emit(conn)
        except socket.error as e:
            print(f"Error al aceptar la conexión: {e}")
        except Exception as e:
            print(f"Error inesperado al aceptar la conexión: {e}")

    def unirse_a_partida(self):
        """Se conecta a un servidor."""
        server_info = self.ui.lineEdit.text().strip()
        if ":" in server_info:
            try:
                ip_address, port = server_info.split(":")
                port = int(port)
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((ip_address, port))

                # Redirigir directamente al juego tras conectarse exitosamente.
                self.iniciar_juego(self.client_socket, is_host=False)
            except socket.error as e:
                QMessageBox.critical(self, "Error de Cliente", f"No se pudo conectar al servidor:\n{e}")
            except Exception as e:
                QMessageBox.critical(self, "Error de Cliente", f"Error inesperado:\n{e}")
        else:
            QMessageBox.warning(self, "Error", "Por favor, ingrese una IP y puerto válidos en el formato IP:Puerto.")

    def iniciar_juego(self, socket_instance, is_host=True):
        try:
            if not socket_instance:
                raise ValueError("Socket de juego no válido. La conexión no se estableció correctamente.")

            # Señaliza que estás en transición hacia la ventana del juego
            self.transitioning = True

            self.juego_ventana = JuegoWindow(socket_instance, is_host, self.usuario)
            self.juego_ventana.show()
            self.hide()

            # Una vez que la nueva ventana se muestra completamente, desactiva el flag
            self.transitioning = False
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo iniciar la ventana del juego: {e}")


    def obtener_interfaces_de_red(self):
        """Obtiene las interfaces de red activas con direcciones IPv4 válidas."""
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
        """Cierra los sockets cuando se cierra la ventana."""
        try:
            if self.server_socket:
                self.server_socket.shutdown(socket.SHUT_RDWR)
                self.server_socket.close()
            if self.client_socket:
                self.client_socket.shutdown(socket.SHUT_RDWR)
                self.client_socket.close()
        except socket.error as e:
            print(f"Error al cerrar el socket: {e}")
        except Exception as e:
            print(f"Error inesperado al cerrar el socket: {e}")
        finally:
            self.server_socket = None
            self.client_socket = None
        event.accept()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
