def main():
    name = input('Digite su nombre: ')
    apellido = input('Digite su apellido: ')
    notas = input('Digite sus notas por favor: ')
    listanotas = [ float(x) for x in notas.split()]
    prom = (sum(listanotas)/len(listanotas))
   
    with open('archivos/lectura.txt', 'a', encoding='utf-8') as archivo:
        print(f'El estudiante {name} {apellido} con notas : \n {listanotas} \n con promedio de {prom: .2f}', file=archivo)
        if prom >= 3:
            print('El estudiante fue aprovado', file=archivo)
        else:
            print('El estudiante fue reprobado', file=archivo)

if __name__ == '__main__':
    main()