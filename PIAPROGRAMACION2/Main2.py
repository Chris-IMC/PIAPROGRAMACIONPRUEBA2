import argparse
import os
import logging
from HASH import Hash
from Configloggin import ConfigurarLogging
from Nmap import Nmap
from PYPDF2 import Metadata
from CorreoConAdjunto import CorreoConAdjunto
from Apishodan import APIshodan

def main():


    parser = argparse.ArgumentParser(description='Tareas de Ciberseguridad')
    parser.add_argument('--Escaneo_de_puertos_nmap', '-E', help="Escáner de puertos que permite identificar puertos abiertos, cerrados o filtrados", action='store_true')
    parser.add_argument('--Api_de_shodan', '-S', help="Extrae informacion de diversos tipos de dispositivos en internet", type=int)
    parser.add_argument('--Envio_de_correo', '-C', help="Envia correo con adjunto")
    parser.add_argument('--Metadatapdf', '-M', help="Extrae metadata de archivos pdf")
    parser.add_argument('--Hash', '-H', help="Extrae el valor hash de un archivo")

    args = parser.parse_args()
    if args.Escaneo_de_puertos_nmap:
        nmap = Nmap()
        nmap.DireccecionIp()


    elif args.Api_de_shodan:
        apishodan = Apishodan()
        apishodan.apishodanmenu()

    elif args.Envio_de_correo:
        correo = CorreoConAdjunto()
        correo.enviar_correo()

    elif args.Metadatapdf:
        metadata = Metadata
        metadata.MetadataPFD()

    elif args.Hash:
        hash = Hash()
        hash.menu()

if __name__ == "__main__":
    main()
