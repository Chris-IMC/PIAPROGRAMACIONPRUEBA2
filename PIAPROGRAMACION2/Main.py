import argparse
import os
import logging
from .HASH import Hash
from .Configloggin import ConfigurarLogging
from .Nmap import Nmap
from .PYPDF2 import Metadata
from .CorreoConAdjunto import CorreoConAdjunto
from .Apishodan import APIshodan

import PIAPROGRAMACION2Prueba as PIA

def main():
    logger = PIA.ConfigurarLoggin(__name__)

    parser = argparse.ArgumentParser(description='Tareas de Ciberseguridad')
    parser.add_argument('--Escaneo_de_puertos_nmap', '-E', help="Escáner de puertos que permite identificar puertos abiertos, cerrados o filtrados")
    parser.add_argument('--Api_de_shodan', '-S', help="Extrae informacion de diversos tipos de dispositivos en internet", type=int)
    parser.add_argument('--Envio_de_correo', '-C', help="Envia correo con adjunto")
    parser.add_argument('--Metadata', '-M', help="Extrae metadata de archivos pdf")
    parser.add_argument('--Hash', '-H', help="Extrae el valor hash de un archivo")

    args = parser.parse_args()
    if args.Escaneo_de_puertos_nmap:
        Nmap = Nmap
        print(Nmap)

    if args.Api_de_shodan:
        api_de_shodan = APIshodan
        print(api_de_shodan)

    if args.Envio_de_correo:
        envio_de_correo = CorreoConAdjunto
        print(envio_de_correo)

    if args.Metadata:
        metadata = Metadata
        print(metadata)

    if args.Hash:
        hash = Hash
        print(hash)



if __name__ == "__main__":
    main()