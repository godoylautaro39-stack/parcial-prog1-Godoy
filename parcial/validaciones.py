def validar_nombres(nombre: str) -> bool: 
    """
    Valida los nombres cargados por el usuario

    Args:
        nombre (str): Nombre que se busca validar
    
    Returns:
        bool : True si el nombre cumple con los requisitos, Fasle si no los cumple
    """
    if len(nombre) < 5:
        print("El nombre debe tener al menos 5 caracteres")
        return False
    
    for i in range (len(nombre)):
        caracter = nombre [i]
        minuscula = "a" <= caracter <= "z"
        mayuscula = "A" <= caracter <= "Z"
        espacio = caracter == " "
        
        if not (mayuscula or minuscula or espacio):
            print("El nombre debe contener solo letras y espacios")
            return False
        
    return True

        
def validar_notas(nota: float ) -> bool: 
    """
    valida las notas ingresadar por el usuario

    Args:
        nota (float/int): nota que se busca validar
    
    Returns: True si la nota cumple con los requisitos, Fasle si no los cumple
    """
    if nota < 0 or nota > 10:
        print ("la nota debe ser entre 1-10" )
        return False

    return True


def validar_cantidad_alumnos() -> int:
    """
    valida la cantidad de alumnos ingresada

    Args:
        No recibre parametros
    
    Returns:
        int: Cantidad de alumnos a cargar en el sistema
    """
    while True :  
        cantidad = int(input("Ingrese la cantidad de alumnos: "))
        
        if cantidad <0 or cantidad > 30: 
            print("Cantidad de alumnos no válida")
        
        else :
            return cantidad

def validar_listas(nombres: list) -> bool:
    """
    Valida que las listas no esten vacias

    Args:
        nombres (list): Lista a comprobar que no este vacia
    
    Returns"
        bool: True en caso de cumplir con los requisitos, False si no los cumple
    """
    if len(nombres) == 0:
        print ("No hay datos cargados")
        return False
    return True




