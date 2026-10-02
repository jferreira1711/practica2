
def main():
    lista = []
    while True:
        try:
            numero = float(input('Digite el numero:'))
            lista.append(numero)
        except ValueError:
            print('Valor no valido. Adios!!')
            break
        finally:
            print(lista)

if __name__ == '__main__':
    main()