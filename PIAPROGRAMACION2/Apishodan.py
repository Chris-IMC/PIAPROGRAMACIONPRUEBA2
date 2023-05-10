from shodan import Shodan
import logging

logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log", format="%(asctime)s - %(levelname)s - %(message)s")

class APIshodan:

    def apishodanmenu(self):

        while True:
            api = Shodan('hSgHyoWTPKKxZsNHgEEM4mHGG2joLXIV')
            try:
                direccion_ip = input("Inngrese la direccion IP: ")
                host = api.host(direccion_ip)
                if not direccion_ip:
                    print("Ingrese bien la direccion IP:")
                else:
                    break
            except Exception as error:
                logging.error(error, exc_info=True)
                print("Hay un problema")

        while True:
            try:
                file = open('BusquedaShodan.txt', 'a+', encoding="utf-8")

                file.write("Informacion general")
                file.write('''
                    Direccion: {}
                    Hostname: {}
                    Dominio: {}
                    Pais: {}
                    Ciudad: {}
                    Organizacion: {}
                    ISP: {}
                    ASN: {}
                    Puertos abiertos: {}
                    '''.format(host['ip_str'], host['hostnames'], host['domains'], host['country_name'], host['city'],
                               host['org'], host['isp'], host['asn'], host['ports']))

                file.close()
                print("Archivo txt guardado con exito")

            except Exception as error:
                logging.error(error,exc_info=True)
                print("Hay un problema")











