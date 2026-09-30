from utilidades.temperatura import fac, caf


def main():
    while(True):
        opcion = int(input("""Menu
        1) Fahrenheit a Celsius
        2) Celsius a Fahrenheit
        3) Salir
        >>"""))
        if opcion == 1:
            temperatur = float(input('Digite la temperatura en F: '))
            print(f'La temperatura {temperatur} F en C es de : {(fac(temperatur)): .2f} C')
        elif opcion == 2:
            temperatur = float(input('Digite la temperatura en C: '))
            print(f'La temperatura {temperatur} C en F es de : {(caf(temperatur)): .2f} F')
        elif opcion == 3:
            print('Hasta luegO!!')
            break
        else:
            print('Opcion no valida')

if __name__ == "__main__":
    main()