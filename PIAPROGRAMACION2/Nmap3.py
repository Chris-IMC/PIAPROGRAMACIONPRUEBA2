import nmap
import csv
import os
import logging

#148.234.5.206
logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log", format="%(asctime)s - %(levelname)s - %(message)s")



class Nmap:
    def DireccecionIp3(self):
        print("introduzca la direccion ip que desea escanear: ")

        while True:
            try:
                direccion_ip = int("IP:")
                if not direccion_ip:
                    print("Vueva a intentar introducir una direccion IP")
                else:
                    break

            except Exception as error:
                logging.error(error, exc_info=True)
                print(" Hay un problema con la direccion")

            return direccion_ip

    def Nmap3(self):
        while True:
            try:
                scanner_nmap = ScannerNmap()
                IP = scanner_nmap.DireccionIP()
                scanner = nmap.PortScanner()
                sc = scanner.scan(hosts=IP, arguments='--open')
                hosts_list = [(x, sc['scan'][x]['hostnames'][0]['name'], list(sc['scan'][x]['tcp'].keys())) for x in
                          scanner.all_hosts()]
                for item in hosts_list:
                    with open('scanHosts1.csv', 'a', newline='') as csvf:
                        writer = csv.writer(csvf)
                        writer.writerow(item)

            except Exception as error:
                logging.error(error, exc_info=True)
                print("Hay un problema")

