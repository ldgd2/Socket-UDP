import threading

class HiloComunicacion(threading.Thread):
    def __init__(self, server_socket, direccion):
        super().__init__()
        self.server_socket = server_socket
        self.direccion = direccion
        self.activo = True

    def run(self):
        # Este hilo se mantiene activo para poder recibir y procesar mensajes sucesivos
        while self.activo:
            pass

    def procesar_mensaje(self, mensaje):
        """Envía una respuesta al mensaje recibido sin impresión adicional."""
        try:
            respuesta = f"Tu mensaje fue: {mensaje}".encode()
            self.server_socket.sendto(respuesta, self.direccion)
        except Exception as e:
            print(f"Error en la comunicación con {self.direccion}: {e}")
            self.detener()

    def detener(self):
        self.activo = False
