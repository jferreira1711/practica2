def main():
    lista = ['Hacer aseo', 'Estudiar Python', 'Ejercicio']
    with open('archivos/jueves2.txt', 'w', encoding='utf-8') as archivo:
        for num, i in enumerate(lista):
            print(f'{num+1}) {i}',file=archivo)

    with open('archivos/jueves2.txt', 'r', encoding='utf-8') as archivo:
        for lineas in archivo:
            print(lineas.split())


if __name__ == '__main__':
    main()