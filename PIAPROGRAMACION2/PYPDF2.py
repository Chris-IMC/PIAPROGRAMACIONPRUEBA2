import PyPDF2
import logging


logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log", format="%(asctime)s - %(levelname)s - %(message)s")

class Metadata:

    def MetadataPFD(self):
        try:
            pdf = open("Textos y actividades del Manual de la Cultura de la Legalidad.pdf", "rb")
            reader = PyPDF2.PdfReader(pdf)
            while True:
                pagenumber = int(input("Ingresa un numero:"))
                page = reader.getPage(pagenumber)
                metad = reader.metadata
                print("Extrayendo texto del pdf..")
                print(page.extractText())
                print("Extrayendo metadata del pdf ")
                print(metad)
                if not pagenumber:
                    print("Ponga un numero de pagina")
                break

        except Exception as error:
            logging.error(error, exc_info=True)
            print("Hay un problema")



