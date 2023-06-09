from shodan import Shodan
import logging

logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log", format="%(asctime)s - %(levelname)s - %(message)s")

class APIshodan:
    api = Shodan('hSgHyoWTPKKxZsNHgEEM4mHGG2joLXIV')

    def apishodanmenu(self):

        print("Ingrese la direccion IP")
        direccion_ip = input("IP: ")
        host = api.host(direccion_ip)

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
                break

            except Exception as error:
                logging.error(error,exc_info=True)
                print("Hay un problema")










