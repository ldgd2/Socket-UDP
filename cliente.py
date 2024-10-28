import socket
import configparser

class ClienteUDP:
    def __init__(self):
        # Leer configuración del servidor desde config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.host = config['servidor']['host']
        self.port = int(config['servidor']['port'])

        # Crear socket UDP
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.activo = True  # Controla el ciclo del cliente

    def enviar_mensaje(self, mensaje):
        # Enviar mensaje al servidor
        self.client_socket.sendto(mensaje.encode(), (self.host, self.port))

    def recibir_mensaje(self):
        # Recibir respuesta del servidor
        try:
            data, _ = self.client_socket.recvfrom(1024)
            return data.decode()
        except Exception as e:
            print(f"Error recibiendo respuesta: {e}")
            return None

    def run(self):
        # Controla el ciclo del cliente hasta que decida desconectarse
        while self.activo:
            mensaje = input("Escribe un mensaje ('salir' para desconectar): ")
            if mensaje.lower() == 'salir':
                self.detener()  # Desconecta el cliente
            else:
                self.enviar_mensaje(mensaje)
                respuesta = self.recibir_mensaje()
                if respuesta:
                    print(f"Respuesta del servidor: {respuesta}")

    def detener(self):
        """Método para detener el cliente de manera controlada."""
        self.activo = False
        self.client_socket.close()
        print("Conexión cerrada.")


if __name__ == "__main__":
    cliente = ClienteUDP()
    cliente.run()
