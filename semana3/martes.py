from utilidades.lista import agregar

def main():
    entrada = input('Digite la lista por favor: ')
    listacompleta = [float(i)for i in entrada.split()]
    numero = float(input('Digite el numero a agregar a la lista: '))

    agregar(listacompleta, numero)

    print(listacompleta)


if __name__ == '__main__':
    main()