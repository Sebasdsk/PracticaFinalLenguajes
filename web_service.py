from flask import Flask, request, jsonify
import pymysql
from datetime import datetime

app = Flask(__name__)

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


def init_db_connection():
    """Inicia y regresa una conexión a la base de datos."""
    return pymysql.connect(**DB_CONFIG)


@app.route("/register_match", methods=["POST"])
def register_match():
    """
    Endpoint para registrar las estadísticas de una partida.
    Se espera que el cuerpo de la solicitud contenga:
        - player1: str (usuario 1)
        - player2: str (usuario 2)
        - winner: str (ganador o "draw" para empate)
        - timestamp: str (opcional, se generará automáticamente si no se proporciona)
    """
    data = request.json
    player1 = data.get("player1")
    player2 = data.get("player2")
    winner = data.get("winner")
    timestamp = data.get("timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if not player1 or not player2 or not winner:
        return jsonify({"error": "player1, player2 y winner son requeridos"}), 400

    try:
        connection = init_db_connection()
        with connection.cursor() as cursor:
            # Ejecutar el query de inserción
            query = """
                INSERT INTO estadisticas (usuario1, usuario2, ganador, fecha_hora)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (player1, player2, winner, timestamp))
            connection.commit()
        return jsonify({"message": "Estadística registrada exitosamente"}), 201
    except pymysql.MySQLError as e:
        return jsonify({"error": f"Error al registrar los datos: {str(e)}"}), 500
    finally:
        connection.close()


# Agregar otro endpoint para obtener estadísticas (opcional)
@app.route("/get_stats", methods=["GET"])
def get_stats():
    """
    Endpoint para obtener todas las estadísticas en la base de datos.
    """
    try:
        connection = init_db_connection()
        with connection.cursor() as cursor:
            # Consultar las estadísticas
            query = "SELECT * FROM estadisticas ORDER BY fecha_hora DESC"
            cursor.execute(query)
            results = cursor.fetchall()
        return jsonify(results), 200
    except pymysql.MySQLError as e:
        return jsonify({"error": f"Error al obtener los datos: {str(e)}"}), 500
    finally:
        connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)