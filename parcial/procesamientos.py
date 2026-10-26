
def carcular_promedio(nota1:list, nota2:list, cantidad:int)-> list:
    """
    Calcula el promedio de cada alumno

    Args:
        nota1 (list): lista con las primeras notas
        nota2 (list): lista con las segundas notas
        cantidad (int): cantidad de lumnos
    
        Returns:
            list: Lista con los promedio de cada alumno
    """
    promedio = [0] * cantidad

    for i in range (cantidad):
        promedio [i] = (nota1[i] + nota2[i] ) / 2
    return promedio

def calcular_promedio_total(promedio:list)-> float:
        """
        Calcula el promedio total de los alumnos

        Args:
            promedio (list): Lista con los promedios de cada alumno
        
        Returns:
            float: valor del promedio total
        """
        suma_promedios = 0 

        for i in range (len(promedio)):
            suma_promedios += promedio [i]

        promedio_total = suma_promedios / len(promedio)
        return promedio_total


def encontrar_maximo(promedios:list)-> float:
    """
    Ecuentra el promedio mas alto

    Args:
        alumnos (list): Lista con los promedios de cada alumno

    Returns:
        float: Valor del promedio mas alto
    """
    numero_maximo = 0

    for i in range (len(promedios)):
        numero = promedios[i]
        if numero > numero_maximo:
            numero_maximo = numero
    return numero_maximo 


def encontrar_alumno_maximo(promedio: float, nombre: str, maximo: float):
    """
    Ecuenta al alumno con el promedio mas alto

    Args:
        promedio (float): Lista con los promedios de cada alumno
        nombre (str): Lista con los nombres de cada alumno
        maximo (float): Valor del promedio mas alto
    
    Returns: El nombre del alumno con promedio mas alto
    """
    for i in range (len(promedio)):
        if promedio[i] == maximo:
            return nombre[i]


def encontrar_minimo(promedios:list)-> int:
    """
    Ecuentra el promedio mas bajo
    
    Args:
        alumnos (list): Lista con los promedios de cada alumno

    Returns:
        float: Valor del promedio mas bajo
    """
    numero_minimo = 10

    for i in range(len(promedios)):
        numero = promedios[i]
        if numero < numero_minimo:
            numero_minimo = numero
    return numero_minimo


def encontrar_alumno_minimo(promedio:list, nombre:list, minimo:int)-> str:
    """
    Ecuenta al alumno con el promedio mas bajo

    Args:
        promedio (float): Lista con los promedios de cada alumno
        nombre (str): Lista con los nombres de cada alumno
        minimo (float): Valor del promedio mas bajo
    
    Returns: El nombre del alumno con promedio mas bajo
    """
        
    for i in range (len(promedio)):
        if promedio[i] == minimo:
            return nombre[i]
        
    return


def mostrar_listado(nombre:list, promedio:list):
    """
    Muestra el nombre y promedio de cada alumno

    Args:
        nombre (list): Lista con los nombres de cada alumno
        promedio (list) Lista con los promedios de cada alumno
    """
    for i in range (len(nombre)):
        print (f"el alumno/a {nombre [i]} tiene un promedio de {promedio[i]}")


def contar_alumno_coindicion(promedio:list):
    """
    cuenta la cantidad de alumnos segun su coindicion

    Args:
        promedio (list): Lista con los promedios de cada alumno
    """
    promocion = 0
    aprobado = 0
    desaprobado = 0

    for i in range (len(promedio)):
        if promedio [i] >= 6:
            promocion += 1

        elif promedio [i] >= 4 and promedio [i] < 6:
            aprobado += 1

        elif promedio [i] < 4:
            desaprobado +=1

        else:
            print (f"no existe ninguna nota")

    print(f"los promocionados son: {promocion}, "
        f"Los aprobados son: {aprobado}, "
        f"Los desaprobados son: {desaprobado} .")


def invertir_nombres(nombre:str)->str :
    """
    Invierte el nombre deseado

    Args:
        nombre (str): Nombre ingresado por el usuario
    """
    return nombre[::-1]


def contar_vocales(nombre: str) -> int:
    """
    cuenta la cantidad de vocales que conntiene un nombre

    Args:
        nombre (str): El nombre al cual se le quiere contar las vocales

    Returns:
        int: Cantidad total de vocales encontradas
    """
    vocales = "aeiou"
    contador = 0
    for i in range (len(nombre)):
    
        for j in range (len(vocales)):
            if nombre [i] == vocales[j]:
                contador += 1
    return contador


def buscar_alumno(nombres: list, alumno: str) -> int:
    """
    Busca la posicion de un alumno en una lista

    Args:
        nombres (list): Lista con los nombres de los alumnos
        alumno (str): Nombre del alumno a encontrar
    
    Returns:
        int: El indice del alumno encontrado, o -1 si no existe
    """
    
    for i in range(len(nombres)):
        if nombres[i] == alumno:
            return i
    return -1


def ordenar_burbuja(promedio: list, nota1: list, nota2: list,nombres: list):
    """
    Ordena las listas de mayor a menor segun el promedio del alumno

    Args:
        promedio (list): Lista con los promedios de cada alumno
        nota1 (list): Lista con la primer nota de cada alumno
        nota2 (list): Lista con la segunda nota de cada alumno
    """
    
    alumnos = len(promedio)

    for i in range (alumnos):
        for j in range (alumnos - 1):
            if promedio [j] < promedio [j + 1]:
                auxiliar = promedio [j + 1]
                promedio [j + 1] = promedio [j]
                promedio [j] = auxiliar

                auxiliar = nombres [j + 1]
                nombres [j + 1] = nombres [j]
                nombres [j] = auxiliar

                auxiliar = nota1 [j + 1]
                nota1 [j + 1] = nota1 [j]
                nota1 [j] = auxiliar

                auxiliar = nota2 [j + 1]
                nota2 [j + 1] = nota2 [j]
                nota2 [j] = auxiliar






















