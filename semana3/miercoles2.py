class EdadNoValida(Exception):
    pass

def comprobar(age):
    if age < 0 or age > 120:
        raise EdadNoValida(f'La edad escriba de {age}, no es valida. La edad maxima es 120 años.')
    
    else:
        print(f'La edad de {age} esta en el rago de edad permitido')
    return age

def main():
    while True:
        try:
            age = int(input('Digite el numero de su edad, por favor: '))
            comprobar(age)
        except ValueError:
            print('Valor no valido, por favor ingrese otro valor nuevamente.')
        except EdadNoValida as e:
            print(f'No se puede procesar: {e}')

if __name__ == '__main__':
    main()