import json
class VariableIncorrecta(Exception):
    pass

def main():
    num = 0
    lista = []
    while True:
        try:
            num = int(input('Cuanto estudiantes vas a ingresar: '))
            if num <= 0:
                raise VariableIncorrecta(f"Variable no valida, debe de ser un numero positivo")
            else:
                break
        except ValueError:
            print('Usted dijito un valor Incorrecto')
        except VariableIncorrecta as e:
            print(f'No se puede procesar: {e}')


    for i in range(num):
        name  = input('Digite su Nombre: ')
        lastname = input('Digite su apellido: ')
        lista.append({'name': name , 'lastname': lastname})

    with open('archivos/estudiantes.json', 'w') as archivo:
        json.dump(lista,archivo, indent=4, ensure_ascii=False)

    with open('archivos/estudiantes.json', 'r') as archivo:
        lista_json = json.load(archivo)
        for num2, i in enumerate(lista_json):
            print(f"{num2+1}) Nombre: {i['name']} Apellido: {i['lastname']}") 


if __name__ == '__main__':
    main()