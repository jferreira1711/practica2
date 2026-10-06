import json
import os

class IngresoIncorrecto(Exception):
    pass
class PhonIncorrecto(Exception):
    pass
class NameIncorrecto(Exception):
    pass
class IndexIncorrecto(Exception):
    pass

ARCHIVO = 'archivos/contactos.json'


def cargar_contactos():
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('El archivo existe pero esta corrupto o vacio')
        return []


def guardar_contacto(contactos):
    os.makedirs(os.path.dirname(ARCHIVO), exist_ok=True)
    with open(ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(contactos, archivo, indent=4, ensure_ascii=False)


def formatear_contacto(numero, contacto):
    return (f"{numero}) Nombre: {contacto['nombre']}  "
            f"Apellido: {contacto['apellido']}  "
            f"Telefono: {contacto['telefono']}")


def pedir_num():
    while True:
        try:
            num = int(input('Digite por favor la opcion que necesita: '))
            if num <= 0 or num > 6:
                raise IngresoIncorrecto('Elija un numero entre 1 y 6')
            return num
        except ValueError:
            print('Valor digitado no permitido')
        except IngresoIncorrecto as e:
            print(f'No se puede procesar: {e}')


def pedir_info(mensaje, funcion):
    while True:
        try:
            return funcion(input(mensaje))
        except (NameIncorrecto, PhonIncorrecto) as e:
            print(f'No se puede procesar: {e}')


def comprobar_datos(nombre):
    if not nombre.replace(' ', '').isalpha():
        raise NameIncorrecto('No es valido lo que escribio, solo letras y espacios')
    return nombre.strip()


def comprobar_number(telefono):
    if not telefono.isdigit():
        raise PhonIncorrecto('No es valido el numero que escribio, solo digitos')
    return telefono


def buscar_concreta(contactos, nombre):
    lista_nueva = []
    indices = []
    for num, contacto in enumerate(contactos):
        if contacto['nombre'].lower() == nombre.lower():
            lista_nueva.append(contacto)
            indices.append(num)
    return lista_nueva, indices


def buscar_contacto(contactos):
    nombre = input('Escriba el nombre del contacto: ')
    lista_nueva, indices = buscar_concreta(contactos, nombre)

    if not lista_nueva:
        print('No se encontro ningun contacto con ese nombre')
        return

    for num, contacto in enumerate(lista_nueva):
        print(formatear_contacto(num + 1, contacto))


def eliminar_contacto(contactos):
    if not contactos:
        print('No hay contactos para eliminar')
        return

    nombre = input('Escriba el nombre del contacto: ')
    lista_nueva, indices = buscar_concreta(contactos, nombre)

    if len(lista_nueva) == 0:
        print('No se encontro ningun contacto con ese nombre')
        return

    if len(lista_nueva) > 1:
        print('Hay mas de un usuario con ese nombre')
        for num, contacto in enumerate(lista_nueva):
            print(formatear_contacto(num + 1, contacto))

        while True:
            try:
                usuario_eliminar = int(input('Elija que usuario eliminar: '))
                if usuario_eliminar <= 0 or usuario_eliminar > len(lista_nueva):
                    raise IndexIncorrecto('Valor no permitido, ese numero no esta en la lista')
                contactos.pop(indices[usuario_eliminar - 1])
                break
            except ValueError:
                print('Valor digitado no permitido')
            except IndexIncorrecto as e:
                print(f'No se puede procesar: {e}')
    else:
        contactos.pop(indices[0])

    guardar_contacto(contactos)
    print('Contacto eliminado')


def mostrar_contactos(contactos):
    if not contactos:
        print('No hay contactos guardados')
        return

    for num, contacto in enumerate(contactos):
        print(formatear_contacto(num + 1, contacto))


def main():
    contactos = cargar_contactos()
    while True:
        print("""
        Menu
        1)Agregar contacto
        2)Buscar contacto
        3)Eliminar contacto
        4)Lista de contactos
        5)Cantidad de contactos
        6)Salir""")
        num = pedir_num()

        if num == 1:
            nombre = pedir_info('Nombre del contacto: ', comprobar_datos)
            apellido = pedir_info('Apellido del contacto: ', comprobar_datos)
            telefono = pedir_info('Numero del contacto: ', comprobar_number)

            contactos.append({'nombre': nombre, 'apellido': apellido, 'telefono': telefono})
            guardar_contacto(contactos)
            print('Contacto agregado y guardado')
        elif num == 2:
            buscar_contacto(contactos)
        elif num == 3:
            eliminar_contacto(contactos)
        elif num == 4:
            mostrar_contactos(contactos)
        elif num == 5:
            print(f'La cantidad de sus contactos es: {len(contactos)}')
        elif num == 6:
            print('Hasta luego!!!')
            break


if __name__ == '__main__':
    main()