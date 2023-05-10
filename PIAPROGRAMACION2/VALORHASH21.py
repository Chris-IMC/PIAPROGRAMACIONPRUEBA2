import hashlib


Archivo = input("Ingrese el nombre del archivo que desea sacar su valor Hash:")

while True:
    try:
        with open(Archivo, 'rb') as f:
            SHA512 = hashlib.sha512()
            for chunk in iter(lambda: f.read(4096), b""):
                SHA512.update(chunk)
                print(SHA512.hexdigest())
            break
    except ValueError:
        print("Ingrese bien el archivo")