import uuid

class Conexion:
    def __init__(self, direccion, socket):
        # Generar un ID único para cada conexión
        self.id_sesion = str(uuid.uuid4())
        self.direccion = direccion  # Dirección del cliente (IP, puerto)
        self.socket = socket  # Socket del cliente
        self.hilo_comunicacion = None  # Hilo de comunicación asociado a la conexión
