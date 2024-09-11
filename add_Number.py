#Jimena Jacobo 

def add_number():
    numeros = list()
    numero = 0
    numerador = 0
    denominador = 1
    columna = 0

    while True:
        #print("\n Choose an option:")
        #print("....................................")
        print(f"\nYou are in the column:   {columna}")
        print("")
        print("1. Decimal")
        print("2. Fraction")
        print("3. New column")
        print("4. New row")

        opcion = int(input("Choose a valid option: "))
        
        if opcion == 1:
            numero += complex(input("\n Ingrese el número: "))
        elif opcion == 2:
            numerador = complex(input("\n Ingrese el numerador: "))
            denominador = complex(input("\n Ingrese el denominador: "))
            numero += numerador/denominador
        elif opcion == 3:
            numeros.append(numero)
            print("....................................")
            numero = 0
            columna += 1
            
        elif opcion == 4:
            numeros.append(numero)
            print("___________________________________________")
            #columna = 0
            break
        else: 
            print("\n Ingrese una opción válida")

    return numeros
