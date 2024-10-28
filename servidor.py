import socket
from hilo_conexiones import HiloConexiones

class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Diccionario para almacenar conexiones activas
        self.conexiones = {}

    def iniciar_servidor(self):
        self.server_socket.bind((self.host, self.port))
        print(f"Servidor UDP escuchando en {self.host}:{self.port}")

        # Inicia el hilo de conexiones
        hilo_conexiones = HiloConexiones(self.server_socket, self)
        hilo_conexiones.start()

    def agregar_conexion(self, conexion):
        """Agrega una conexión a las conexiones activas."""
        self.conexiones[conexion.direccion] = conexion
        print(f"Conexión agregada: {conexion.direccion} con ID de sesión {conexion.id_sesion}")

    def get_conexion(self, direccion):
        """Retorna la conexión existente para una dirección dada o None si no existe."""
        return self.conexiones.get(direccion)
