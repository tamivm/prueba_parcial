
entrada_general = []
entrada_vip = []
tipo_entrada= ""
codigo_confirmacion = ""
valores = ""

while True:
    print ("MENU PRINCIPAL")
    print ("1.- Comprar entrada.")
    print ("2.- Consultar comprador.")
    print ("3.- Cancelar compra.")
    print ("4.- Salir")
    try:
        opcion = input("Ingrese una opción para continuar: ")

    except ValueError:
        print ("Ingrese un número válido")

        
    while True:
         nombre = input("Ingrese el nombre del comprador: ").lower()
         entrada_tipo = input("Ingrese el tipo de entrada (G/V): ").lower()
         try:
            codigo_confirmacion = int(input("Ingrese codigo de confirmación: ")).strip().len()
         except ValueError:
            print("Intente nuevamente, clave solo de un máximo de 6 caracteres con al menos 1 letra mayuscula, 1 numero y sin espacios ")
         break

        
    consultar_comprador = {
        "01": ["Tamara", "v", "123345L"],
        "02": ["Maria", "g", "12346M"],
        "03": ["Sebastian", "v", "12347J"],
        "04": ["Miguel", "g", "12348P"],
            }
    def compradores_concierto(nombre):
     while True:
        nombre = input("Ingrese el comprador a buscar: ").lower()
        valores = consultar_comprador.values()
        comprador =[]

        for valor in valores:
            if valor [0].lower == nombre.lower():
                comprador.append (valor[0])

                if comprador:
                    print (f"Los datos del comprador son: {compradores_concierto}")  
                else:
                    print ("El comprador no se encuentra")
            
    def elimnar_compra():
        while True:
            nombre_eliminar = input("Ingrese el nombre del comprador a eliminar: ").lower()
            claves = consultar_comprador.keys()
            comprador_error = None
            for clave in claves:
                comprador = consultar_comprador [clave]
                if comprador [0].lower == nombre_eliminar.lowe()
                comprador_error =clave
                print ("Compra cancelada")
            if comprador_error !=None:
                del consultar_comprador [comprador_eliminar]
                print ("El comprador no se encuentra")           




                








            
            
