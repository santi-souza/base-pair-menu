import math

# Primera parte: Funciones
def traducir_base(base):
    '''Traduce una base a un valor dado por la tabla dada'''
    if base.upper() == 'A':
        return 1
    elif base.upper() == 'C':
        return 2
    elif base.upper() == 'G':
        return 3
    elif base.upper() == 'T':
        return 4
    elif base.upper() == 'N':
        return 5
    elif base == '-' or base == '':
        return 0
    else:
        return -1
    
def parsearBases(base1, base2):
    '''Das dos bases y te devuelve una coordenada'''
    x = traducir_base(base1)
    y = traducir_base(base2)
    return (x, y)

def trasponer(punto):
    return (punto[1], punto[0])

def obtenerPromedio(punto1, punto2):
    x1 = int(punto1[0])
    y1 = int(punto1[1])
    x2 = int(punto2[0])
    y2 = int(punto2[1])
    return ((x1 + x2) / 2), ((y1 + y2) / 2)

def calcularDistancia(punto1, punto2):
    x1 = punto1[0]
    y1 = punto1[1]
    x2 = punto2[0]
    y2 = punto2[1]
    D = math.sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return D

def aplicarDesviacion(punto, secuencia):
    if len(secuencia) == 0:
        raise ValueError("La secuencia no puede estar vacía.")
    
    x = punto[0]
    y = punto[1]
    c = secuencia.lower().count('c')
    g = secuencia.lower().count('g')
    porcentaje = (float(c) + g) / len(secuencia)
    if porcentaje > 0.5:
        return (x + 1, y)
    elif porcentaje < 0.5:
        return (x, y + 1)
    else:
        return (x, y)

def ordenarImprimir(punto1, punto2):
    a = punto1[0]
    b = punto1[1]
    c = punto2[0]
    d = punto2[1]
    lista = [a, b, c, d]
    lista.sort()
    texto = ""
    for i in lista:
        texto += " " + str(i)
    return texto

def mayor_numero(punto):
    return max(punto[0], punto[1])

def parsearCodonInexacto(punto1, punto2, punto3):
    a = mayor_numero(punto1)
    b = mayor_numero(punto2)
    c = mayor_numero(punto3)
    bases = {1: "A", 2: "C", 3: "G", 4: "T", 5: "N"}
    if 1 <= a <= 5 and 1 <= b <= 5 and 1 <= c <= 5:
        return bases[a] + bases[b] + bases[c]
    else:
        return ""

def entrecinco(punto):
    a = punto[0] + punto[1]
    while a > 5:
        a -= 5
    return a

def parsearCodonExacto(punto1, punto2, punto3):
    a = entrecinco(punto1)
    b = entrecinco(punto2)
    c = entrecinco(punto3)
    if a > 0 and b > 0 and c > 0:
        bases = {1: "A", 2: "C", 3: "G", 4: "T", 5: "N"}
        return bases[a] + bases[b] + bases[c]
    else:
        return ""

# Segunda parte: Programa
def menu():
    print("=" * 40)
    print("MENU")
    print("=" * 40)
    print("1- Parsear bases.")
    print("2- Transponer un punto.")
    print("3- Obtener el promedio de dos puntos.")
    print("4- Calcular distancia entre dos puntos.")
    print("5- Aplicar desviación.")
    print("6- Ordenar números.")
    print("7- Parsear codon inexacto.")
    print("8- Parsear codon exacto.")
    print("0- Salir.")
    print("=" * 40)
    
    while True:
        try:
            op = int(input("Seleccione la opción deseada: "))
            if 0 <= op <= 8:
                return op
            print("Opción incorrecta, seleccione una opción correcta (0-8).")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Funciones complementarias del menú
def es_base_valida(base):
    return len(base) == 1 and (base.upper() in ['A', 'T', 'C', 'G', 'N', ' ', '-'])

def es_secuencia_valida(sec):
    return all(es_base_valida(b) for b in sec)

def pedir_una_base_valida():
    base = input("Ingrese una base: ")
    while not es_base_valida(base):
        print("La base ingresada no es válida.")
        base = input("Ingrese una nueva base: ")
    return base

def pedir_secuencia_valida():
    sec = input("Indique la secuencia de referencia: ")
    while not es_secuencia_valida(sec):
        print("La secuencia ingresada no es válida.")
        sec = input("Por favor, indique una secuencia válida: ")
    return sec

def pedir_dos_numeros():
    while True:
        try:
            x = int(input("Indique un número: "))
            y = int(input("Indique un número: "))
            return (x, y)
        except ValueError:
            print("Por favor, ingrese números válidos.")

# Opciones del menú
def opcion1():
    print("")
    base1 = pedir_una_base_valida()
    base2 = pedir_una_base_valida()
    print("El punto obtenido es:", parsearBases(base1, base2))
    print("")

def opcion2():
    print("")
    x = pedir_una_base_valida()
    y = pedir_una_base_valida()
    punto = parsearBases(x, y)
    resultado = trasponer(punto)
    print("El punto obtenido es:", resultado)
    print("")

def opcion3():
    print("")
    x1 = pedir_una_base_valida()
    y1 = pedir_una_base_valida()
    x2 = pedir_una_base_valida()
    y2 = pedir_una_base_valida()
    punto1 = parsearBases(x1, y1)
    punto2 = parsearBases(x2, y2)
    print("El promedio obtenido es:", obtenerPromedio(punto1, punto2))
    print("")

def opcion4():
    print("")
    x1 = pedir_una_base_valida()
    y1 = pedir_una_base_valida()
    x2 = pedir_una_base_valida()
    y2 = pedir_una_base_valida()
    punto1 = parsearBases(x1, y1)
    punto2 = parsearBases(x2, y2)
    print("La distancia obtenida es:", calcularDistancia(punto1, punto2))
    print("")

def opcion5():
    print("")
    x = pedir_una_base_valida()
    y = pedir_una_base_valida()
    punto = parsearBases(x, y)
    sec = pedir_secuencia_valida()
    print(aplicarDesviacion(punto, sec))
    print("")

def opcion6():
    print("")
    x1 = pedir_una_base_valida()
    y1 = pedir_una_base_valida()
    x2 = pedir_una_base_valida()
    y2 = pedir_una_base_valida()
    punto1 = parsearBases(x1, y1)
    punto2 = parsearBases(x2, y2)
    print("Los números obtenidos fueron:", ordenarImprimir(punto1, punto2))
    print("")

def opcion7():
    print("")
    punto1 = pedir_dos_numeros()
    punto2 = pedir_dos_numeros()
    punto3 = pedir_dos_numeros()
    print("El codón es:", parsearCodonInexacto(punto1, punto2, punto3))
    print("")

def opcion8():
    print("")
    punto1 = pedir_dos_numeros()
    punto2 = pedir_dos_numeros()
    punto3 = pedir_dos_numeros()
    print("El codón es:", parsearCodonExacto(punto1, punto2, punto3))
    print("")

# Programa principal
if __name__ == "__main__":
    seleccion = menu()  # Seleccionar la opción inicial del menú
    
    while seleccion != 0:
        if seleccion == 1:
            opcion1()
        elif seleccion == 2:
            opcion2()
        elif seleccion == 3:
            opcion3()
        elif seleccion == 4:
            opcion4()
        elif seleccion == 5:
            opcion5()
        elif seleccion == 6:
            opcion6()
        elif seleccion == 7:
            opcion7()
        elif seleccion == 8:
            opcion8()
        seleccion = menu()
    
    print("Fin del programa.")