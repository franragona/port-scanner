# Port Scanner en Python

Este proyecto es un escáner de puertos simple escrito en Python. Permite a los usuarios identificar puertos abiertos en una dirección IP o nombre de dominio específico, útil para realizar pruebas de seguridad básicas.

## Descripción

El escáner de puertos utiliza la biblioteca `socket` para manejar las conexiones de red y `threading` para ejecutar múltiples escaneos en paralelo, mejorando la eficiencia y velocidad del proceso. La dirección IP o el nombre de dominio objetivo se especifican como un argumento de línea de comandos mediante `argparse`.

## Características

- Escaneo rápido de puertos mediante hilos.
- Muestra los puertos abiertos en la dirección objetivo.
- Configuración de tiempo de espera para evitar bloqueos en el escaneo.
- Manejo básico de errores durante el escaneo.

## Requisitos

- Python 3.x
- Bibliotecas estándar: `socket`, `argparse`, `threading`

## Uso

Ejecuta el script desde la línea de comandos de la siguiente manera:

```bash
python port_scanner.py -t <IP_o_nombre_de_dominio>
