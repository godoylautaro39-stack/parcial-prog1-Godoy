
import validaciones 
import procesamientos



def cargar_datos(nombres: str, nota1: float, nota2: float, cantidad: int): 
    """
    Carga datos ingresados por el usuario

    Args:
        nombres (str): Nombre ingresado
        nota1 (float): Primer nota ingresada
        nota2 (float): Segunda nota ingresada
        cantidad (int): cantidad de alumnos 

    """
    for i in range(cantidad):
        
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
        
        while not validaciones.validar_nombres(nombre): 
            nombre = input ("Invalido, ingrese el nombre nuevamente: ")
        nombres [i] = nombre

        nota_1 = float(input(f"Ingrese la nota 1 del alumno {i + 1}: "))
        while not validaciones.validar_notas(nota_1):
            nota_1 = int (input ("Invalido, ingresela la nota nuevamente: "))
        nota1[i] = nota_1

        nota_2 = float(input(f"Ingrese la nota 2 del alumno {i + 1}: "))
        while not validaciones.validar_notas(nota_2):
            nota_2 = int (input ("Invalido, ingresela la nota nuevamente: "))
        nota2[i] = nota_2


def crear_listas(cantidad:int, valor_inicio) -> list: 
    """
    crea una lista multiplicando el valor inicial por la cantidad indicada

    Args:
        cantidad (int): Numero de elementos que contendra la lista
        Valor_inicio (): Valor inicial de la lista

    Returns:
        list: devuelve una nueva lista
    """
    lista = [valor_inicio] * cantidad
    return lista


def main ():
    """
    Funcion que ejecuta el programa
    """
    nombres = []
    nota1 = []
    nota2 = []
    promedios = []


    while True:
        print (""" 
        1. Cargar alumnos
        2. Mostrar listado
        3. Mostrar estadisticas
        4. Ver ranking (ordenado)
        5. Buscar Alumno
        6. Juegos con un nombre
        0. Salir
        """)


        match int(input("Seleccione una opcion: ")):
            
            case 1:
                cantidad = validaciones.validar_cantidad_alumnos()
                nombres = crear_listas(cantidad, "")
                nota1 = crear_listas(cantidad, 0)
                nota2 = crear_listas(cantidad, 0)

                cargar_datos(nombres, nota1, nota2, cantidad)
                promedios = procesamientos.carcular_promedio (nota1,nota2,cantidad)

            case 2:
                validaciones.validar_listas(nombres)
                procesamientos.mostrar_listado (nombres,promedios)


            case 3:
                if validaciones.validar_listas(nombres):
                    promedio_alumnos = procesamientos.calcular_promedio_total (promedios)
                    print (f"El promedio total del curso es de {promedio_alumnos}")

                    maximo = procesamientos.encontrar_maximo (promedios)
                    alumno_maximo = procesamientos.encontrar_alumno_maximo(promedios,nombres,maximo)
                    print (f"El alumno/a {alumno_maximo} cuenta con el promedio mas alto : {maximo}")

                    minimo = procesamientos.encontrar_minimo (promedios)
                    alumno_minimo = procesamientos.encontrar_alumno_minimo(promedios,nombres,minimo)
                    print (f"El alumno/a {alumno_minimo} cuenta con el promedio mas bajo : {minimo}")
                    procesamientos.contar_alumno_coindicion(promedios)


            case 4:
                if validaciones.validar_listas(nombres):
                    procesamientos.ordenar_burbuja(promedios, nota1, nota2, nombres)

                for i in range (len(nombres)):
                    print(f"{nombres[i]} promedio: {promedios[i]}")


            case 5:
                if validaciones.validar_listas(nombres):

                    alumno = (input("ingrese alumno alumno a buscar: "))
                    while not validaciones.validar_nombres(alumno):
                        alumno = (input("ingrese alumno alumno a buscar: "))

                    busqueda = procesamientos.buscar_alumno(nombres,alumno)

                    if busqueda == -1:
                        print("El alumno no existe: ")
                    else :
                        print(f"El alumno/a: {nombres[busqueda]}",
                            f"primer nota: {nota1[busqueda]}",
                            f"segunda nota: {nota2[busqueda]}",
                            f"promedio: {promedios[busqueda]}")


            case 6:
                nombre = input (f"Ingrese un nombre: ")
                while not validaciones.validar_nombres (nombre):
                        nombre = input (f"Ingrese un nombre: ")
                vocales = procesamientos.contar_vocales(nombre)
                print(f"el nombre {nombre} tiene {vocales} vocales")
                print (procesamientos.invertir_nombres(nombre))


            case 0:
                break


            case _:
                (print("opcion invalida"))


main ()