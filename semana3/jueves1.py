import json
def main():
    lista = []
    with open('archivos/datos.json', 'r') as archivo:
        lista = json.load(archivo)

    for num, i in enumerate(lista):
        print(f'{num+1}) Nombre: {i['name']} Apellido: {i['lastname']}')

    
        



if __name__ == '__main__':
    main()
