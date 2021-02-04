from FiguraGeometrica import *

def write_menu():
    print("--------------------")
    print("FIGURAS GEOMÉTRICAS \n1. TRIÁNGULO \n2. RECTÁNGULO \n3. CUADRADO \n4. PENTÁGONO \n0. Salir")
    print("--------------------")

    option = get_value("Escoja una opcion: ",0)

    if (option == 1):
        base = get_value("Introduzca el valor de la base: ",1)
        h = get_value("Introduzca el valor de la altura: ",1)
        lado1 = get_value("Introduzca el valor del lado 1: ",1)
        lado2 = get_value("Introduzca el valor del lado 2: ", 1)
        t = Triangulo(base,lado1,lado2,h)
        get_info(t)
    elif (option == 2):
        base = get_value("Introduzca el valor de la base: ", 1)
        h = get_value("Introduzca el valor de la altura: ", 1)
        r = Rectangulo(base,h)
        get_info(r)
    elif(option==3):
        base = get_value("Introduzca el valor de la base: ", 1)
        c = Cuadrado(base)
        get_info(c)
    elif(option==4):
        lado = get_value("Introduzca el valor de los lados: ", 1)
        apotema = get_value("Introduzca el valor del apotema: ", 1)
        p = Pentagono(lado,apotema)
        get_info(p)
    elif (option == 0):
        print(exit(0))
    else:
        print("Error! Seleccione una opción válida")
        write_menu()

    write_menu()


def get_info(figura):
    print("-----------------")
    print("El área es: ", figura.calcular_area())
    print("El perímetro es: ", figura.calcular_perimetro())
    print("-----------------")

def get_value(msg,option):
    if(option==0):
        try:
            op = int(input(msg))
        except ValueError:
            op = None
        finally:
            return op
    if(option==1): #Option==1 means that we´re asking for a float, so, we´ll use this method to get values for the figures.
        try:
            op = float(input(msg))
        except ValueError:
            op = None
        finally:
            return op

if __name__ == '__main__':
    write_menu()
