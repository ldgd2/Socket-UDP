import configparser
from servidor import Servidor
import time

# Clase Main - Ejecuta las clases de conexión y administración de hilos
class Main:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.host = config['servidor']['host']
        self.port = int(config['servidor']['port'])
        self.servidor = Servidor(self.host, self.port)

    def run(self):
        self.servidor.iniciar_servidor()
        # Bucle infinito para mantener el servidor en ejecución
        while True:
            time.sleep(1)

# Iniciar la aplicación
if __name__ == "__main__":
    main = Main()
    main.run()
