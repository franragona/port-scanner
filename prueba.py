import socket
import argparse
import threading

# Configurar argparse
parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help="dirección objetivo", required=True)
args = parse.parse_args()

# Definir la función de escaneo
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Configura un tiempo de espera (timeout) para evitar que las conexiones lentas bloqueen el escaneo
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Puerto {port} está abierto")
        sock.close()
    except:
        pass

# Crear y lanzar múltiples hilos
target = args.target
threads = []

for port in range(1, 3):
    thread = threading.Thread(target=scan_port, args=(target, port))
    threads.append(thread)
    thread.start()
    
    # Limitar el número de hilos activos para no sobrecargar el sistema
    if len(threads) > 1000:
        for t in threads:
            t.join()
        threads = []

# Esperar a que todos los hilos terminen
for t in threads:
    t.join()
