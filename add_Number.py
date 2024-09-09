#Jimena Jacobo 

def add_number():
    numeros = list()
    numero = 0
    numerador = 0
    denominador = 1

    while True:
        print("\n Seleccione la opcion de número:")
        print("1. Sin fracción")
        print("2. Fracción")
        print("3. Nuevo numero")
        print("4. Salir")

        opcion = int(input("\n Seleccione una opción válida (1-2): "))
        if opcion == 1:
            numero += complex(input("\n Ingrese el número: "))
            #print(numero)
        elif opcion == 2:
            numerador = complex(input("\n Ingrese el numerador: "))
            denominador = complex(input("\n Ingrese el denominador: "))
            numero += numerador/denominador
            #print(numero)
        elif opcion == 3:
            numeros.append(numero)
            #print(numeros, numero)
            numero = 0
        elif opcion == 4:
            numeros.append(numero)
            break
        else: 
            print("\n Ingrese una opción válida")

    #print(numeros)

    return numeros


#if __name__ == "__main__":
 #   numbers = add_number()