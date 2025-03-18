# EFT S9 Daniel Alarcón Poblete

# Programa de administración de pasajes Línea Aérea TETINKA

# Importar numpy para crear arreglo de los asientos.
import numpy as np
pasajeros = {}

# Arreglo con numpy para almacenar asientos del 1 al 48
asientos = np.arange(1, 49).reshape(8, 6)  # .reshape en 8 filas y 6 columnas de asientos

# Opción 1: Ver asientos disponibles
def ver_asientos():
    """
    Esta función muestra todos los asientos disponibles en el avión.
    Hace referencia al arreglo asientos.
    Los asientos disponibles se muestran en números.
    Los asientos no disponibles se muestran con X.
    Si el asiento no disponible tiene número del 101 al 109 se muestra como "X".
    Si el asiento no disponible tiene número del 110 al 148, se cambia por "X " 
    para mantener la forma del diagrama.
    """
    
    print("\nEstos son los asientos disponibles: ")

    def linea_blanco():
        print("|" + " " * 24 + "|")

    print(" _" * 12)

    
     # Mostrar los asientos
    for fila in range(asientos.shape[0]):
        linea_blanco()  # Imprimir línea en blanco entre cada fila de asientos
        # Imprimir cada asiento de la fila
        fila_asientos = "|"
        for columna in range(asientos.shape[1]):
            asiento_num = asientos[fila, columna]
            # Mostrar "X" si el asiento está ocupado
            if 101 <= asiento_num <= 109:
                fila_asientos += " X "  # Asiento ocupado (101 a 109)
            elif 110 <= asiento_num <= 148:
                fila_asientos += " X "  # Asiento ocupado (110 a 148)
            else:
                fila_asientos += f" {asiento_num:<2}"  # Formato para el número de asiento
            
            # Agregar espacios para representar el pasillo entre cada trio de asientos por fila.
            # Ej. entre 1 2 3 y 4 5 6
            if (columna + 1) % 3 == 0 and columna < asientos.shape[1] - 1:
                fila_asientos += " " * 5
        
        fila_asientos += " |"  # Diseño de final de fila en diagrama
        print(fila_asientos)  # Imprimir la fila de asientos
        
        # Insertar la fila de separación entre asientos 30 y 31
        if fila == 4:
            linea_blanco()
            print("|    |_ _ _ _ _ _ _|     |")  # Fila de separación
        
        linea_blanco()
    print(" ▔" * 12)
    print("")

# Opción 2: Comprar asiento
def comprar():
    """
    
    Esta función permite comprar asientos disponibles.
    Solicita los datos de usuario y aplica descuento si el banco es bancoDuoc.
    Al comprar un asiento que estaba disponible, se le suma 100 al número de asiento.
    De este modo, todo número de asiento mayor a 100, está comprado.
    Si el asiento ya estaba comprado, se muestra un mensaje de error.
    """
    

  # Definir precios
    p_premium = 250000  
    p_general = 170300  
    a_general = [i for i in range(2, 48, 3)] # Asientos con precio general
    descuento = 0.88    # Descuento del 12% para usuarios de bancoDuoc

    while True:
        ver_asientos() #Se muestran los asientos disponibles.
        try:
            # Ingresar el número de asiento
            compra_asiento = input("Ingrese el número de asiento que desea comprar: ")
          
            # Convertir la entrada a un número entero
            compra_asiento = int(compra_asiento)
           
            if compra_asiento < 1 or compra_asiento > 48:
                print("El número de asiento ingresado no es válido. Intente nuevamente.")
                continue  # Volver a solicitar el asiento

            # Convertir el número de asiento a un índice
            indice = compra_asiento - 1  # Restar 1 para obtener el índice correcto
            

            # Verificar si el asiento ya está ocupado
            if asientos.flat[indice] > 100:
                print("Lo sentimos, ese asiento ya está ocupado.\n")
                return
            

            # Determinar el precio del asiento
            # Revisar si es asiento del medio
            if compra_asiento in a_general:
                precio = p_general
            else:  # Asiento ventana o pasillo
                precio = p_premium

            
            # Pedir datos de pasajero
            # Nombre
            while True: 
                nombrePasajero = input("Ingrese el nombre y los apellidos pasajero: ")
                if nombrePasajero.strip() == "": #Verificar que no esté en blanco
                  print("El nombre del pasajero no estar en blanco.")
                else:
                  print(f"El nombre {nombrePasajero} ha sido ingresado correctamente.")
                  break 

            
            # RUT del pasajero
            while True:
              rutPasajero = input("Ingrese el RUT del pasajero sin puntos y sin guión (ej: 12345678K): ")
              rutPasajero = rutPasajero.upper()
              rutPasajero = rutPasajero.strip()

              # Validar que no esté en blanco 
              if rutPasajero == "":
                print("El RUT del pasajero no puede estar en blanco.")
    
              # Validar que tenga 8 o 9 caracteres, último puede ser K
              elif len(rutPasajero) != 8 and len(rutPasajero) != 9:
                print("El RUT debe tener 8 o 9 caracteres (incluyendo el dígito verificador).")
        
              # Validar que el RUT solo contenga números y opcionalmente la letra K
              elif not (rutPasajero[:-1].isdigit() and (rutPasajero[-1].isdigit() or rutPasajero[-1].upper() == 'K')):
                print("El RUT sólo puede contener números y el dígito verificador puede ser número o K.")
    
              else:
                print(f"El RUT del pasajero {rutPasajero} ha sido ingresado correctamente.")
                break



            # Teléfono
            while True:
              telefonoPasajero = input("Ingrese el teléfono del pasajero, sólo números (ej: 56991234567): ")
    
              # Validar que no esté en blanco 
              if telefonoPasajero.strip() == "":
                print("El teléfono no puede estar en blanco.")
                telefonoPasajero = telefonoPasajero.strip()
              # Validar que tenga 11 digitos
              elif len(telefonoPasajero) != 11 or not telefonoPasajero.isdigit():
                print("El número de teléfono debe tener 11 dígitos y contener sólo números.")
        
              else:
                print(f"El teléfono {telefonoPasajero} ha sido ingresado correctamente.")
                break


            # Banco
            while True:
              try:
                banco = int(input("Ingrese el número de banco: \n1. bancoDuoc \n2. Otro\n"))        
                if banco == 1:
                  bancoPasajero = "bancoDuoc"
                  print(f"El nombre del banco {bancoPasajero} ha sido ingresado correctamente.")
                  precio = precio*descuento #Aplicar 12% de descuento
                  break 
                elif banco == 2:
                  bancoPasajero = input("Ingrese el nombre del banco: ")
                  if bancoPasajero.strip() == "": #Verificar que no esté en blanco
                    print("El nombre del banco no puede estar en blanco.")
                  else:
                    print(f"El nombre del banco {bancoPasajero} ha sido ingresado correctamente.")
                    break 
                else:
                  print("Debe ingresar 1 o 2.")
              except ValueError:
                print("\nDebe ingresar un número.\n")



            # Mostrar el precio al usuario y confirmar compra.
            while True:
              try:
                print(f"El precio del asiento {compra_asiento} es ${precio}.")
                aceptar = int(input("¿Desea comprarlo? \n1. Sí \n2. No "))
           
                if aceptar == 1:
                # Marcar el asiento como ocupado
                  asientos.flat[indice] = 100 + compra_asiento  # Cambiar a 100 + número de asiento
                  print(f"El asiento {compra_asiento} ha sido comprado con éxito.\n")
                  
                  # Agregar los datos a una lista para cada pasajero
                  datos_pasajero = [nombrePasajero, rutPasajero, telefonoPasajero, bancoPasajero, precio]

                  # Agregar la lista al diccionario con clave numero de asiento
                  pasajeros[compra_asiento] = datos_pasajero
                  return


                elif aceptar == 2:
                  print("Compra cancelada.")
                  return
                else:
                  print("Debe ingresar 1 o 2.")
                  return
              except ValueError:
                print("\nDebe ingresar un número.\n")

            

        except ValueError:
            print("\nDebe ingresar un número.\n")
        except IndexError:
            print("\nEl número de asiento debe estar entre 1 y 48.\n")




# Opción 3: Anular pasaje
def anular():
    """
    Esta función permite anular un pasaje, dejando el asiento disponible nuevamente
    y eliminando los datos del pasajero correspondiente.
    """
    while True:
        try:
            # Verificar si hay asientos ocupados
            if not pasajeros:
                print("No hay asientos ocupados en este momento.")
                break 

            # Pedir número de asiento para desea anular
            anular_asiento = int(input("\nIngrese el número de asiento que desea anular (Ingrese 0 para Salir): "))

            # Permitir salir ingresando 0
            if anular_asiento == 0:
                print("\nVolviendo al Menú principal.\n")
                break

            # Validar que el número de asiento esté en el rango correcto
            if anular_asiento < 1 or anular_asiento > 48:
                print("El número de asiento debe estar entre 1 y 48.")
                continue 

            # Validar que el asiento esté ocupado
            if anular_asiento not in pasajeros:
                print(f"El asiento {anular_asiento} no está ocupado. Intente nuevamente.")
                continue

            # Confirmar que el usuario realmente desea anular el pasaje
            while True:
                try:
                    confirmar = int(input(f"¿Está seguro de que desea anular el asiento {anular_asiento}? \n1. Sí\n2. No:  "))

                    if confirmar == 1:
                        asientos.flat[anular_asiento - 1] = anular_asiento  # Restaurar el número original del asiento
                        del pasajeros[anular_asiento]  # Eliminar los datos del pasajero

                        print(f"El asiento {anular_asiento} ha sido liberado exitosamente.")
                        break 
                    elif confirmar == 2:
                        print("Anulación cancelada.")
                        break 
                    else:
                        print("Debe ingresar 1 o 2.")
                except ValueError:
                    print("Debe ingresar un número.")
            break
        except ValueError:
            print("Debe ingresar un número.")


    



# Opción 4: Modificar datos del pasajero
def mod_datos():
    """
    Esta función permite modificar los datos de un pasajero.
    Solicita el número de asiento y el RUT para verificar al pasajero,
    luego permite modificar el nombre y/o el teléfono.
    """

    # Verificar si hay pasajeros registrados
    if not pasajeros:
        print("No hay pasajeros registrados en este momento.")
        return

    while True:
        try:
            # Solicitar el número de asiento
            asiento_modificar = int(input("\nIngrese el número de asiento del pasajero (1 al 48) - Ingrese 0 para Salir: "))

            # Permitir salir si se ingresa 0
            if asiento_modificar == 0:
                print("\nVolviendo al Menú principal.\n")
                return

            # Validar que el número de asiento esté dentro del rango permitido
            if asiento_modificar < 1 or asiento_modificar > 48:
                print("El número de asiento debe estar entre 1 y 48.")
                continue

            # Validar que el asiento esté ocupado
            if asiento_modificar not in pasajeros:
                print(f"El asiento {asiento_modificar} no está ocupado. Intente nuevamente.")
                continue

           # Solicitar el RUT para verificar la identidad del pasajero
            rut_verificacion = input("Ingrese el RUT del pasajero para verificar (ej: 12345678K) - Ingrese 0 para Salir: ").upper().strip()

            # Permitir salir si se ingresa "0"
            if rut_verificacion == "0":
                print("\nVolviendo al Menú principal.\n")
                return

            # Verificar si el RUT coincide con el registrado para ese asiento
            if pasajeros[asiento_modificar][1] != rut_verificacion:
                print("El RUT ingresado no coincide con el pasajero de este asiento. Intente nuevamente.")
                continue

            # Mostrar el submenú para modificar los datos
            while True:
                print("\n¿Qué dato desea modificar?")
                print("1. Nombre del pasajero")
                print("2. Teléfono del pasajero")
                print("3. Volver al Menú principal.")

                try:
                    opcion = int(input("Seleccione una opción: "))

                    if opcion == 1:
                        # Modificar nombre del pasajero
                        nuevo_nombre = input("Ingrese el nuevo nombre del pasajero: ")
                        if nuevo_nombre.strip():
                            pasajeros[asiento_modificar][0] = nuevo_nombre
                            print("El nombre del pasajero ha sido actualizado correctamente.")
                            print(f"El nuevo nombre es {nuevo_nombre}.")
                        else:
                            print("El nombre no puede estar en blanco.")
                    elif opcion == 2:
                        # Modificar teléfono del pasajero
                        nuevo_telefono = input("Ingrese el nuevo teléfono del pasajero, sólo números (ej: 56991234567): ").strip()
                        if len(nuevo_telefono) == 11 and nuevo_telefono.isdigit():
                            pasajeros[asiento_modificar][2] = nuevo_telefono
                            print("El teléfono del pasajero ha sido actualizado correctamente.")
                            print(f"El nuevo teléfono es {nuevo_telefono}.")
                        else:
                            print("El número de teléfono debe tener 11 dígitos y contener sólo números.")
                    elif opcion == 3:
                        print("\nVolviendo al menú principal.\n")
                        return
                    else:
                        print("Debe ingresar 1, 2 o 3.")
                except ValueError:
                    print("Debe ingresar un número.")
        except ValueError:
            print("Debe ingresar un número.")


# Opción 5: Salida del programa con mensaje y versión

def salir():
  print('\nGracias por usar el sistema de administración de pasajes de Línea Aérea TETINKA.') 
  print('Saliendo del programa.')
  avion = """
       __|__
--@--@--(_)--@--@--
    """
  print(avion)
  print('\n¡Hasta pronto!\n')
  print('Autor: Daniel Alarcón Poblete')

  # Importar datetime
  from datetime import datetime

  # Asignar fecha a la variable fecha_actual y mostrar
  fecha_actual = datetime.now().strftime("%d-%m-%Y")
  print(f'La fecha actual es: {fecha_actual}')




# Menú

def menu():
  while True:
    try:
      print('Bienvenido a Línea Aérea TETINKA')
      print('1. Ver asientos disponibles.')
      print('2. Comprar asiento.')
      print('3. Anular pasaje.')
      print('4. Modificar datos del pasajero.')
      print('5. Salir.')
      opcion = int(input('Ingrese una opción: '))

# Opción 1
      if opcion == 1:
        print("\nHa seleccionado la opción 1. Ver asientos disponibles.")
        ver_asientos()
# Opción 2
      elif opcion == 2:
        print("\nHa seleccionado la opción 2. Comprar asiento.")
        comprar()
# Opción 3
      elif opcion == 3:
        print("\nHa seleccionado la opción 3. Anular pasaje.")
        anular()
# Opción 4
      elif opcion == 4:
        print("\nHa seleccionado la opción 4. Modificar datos del pasajero.")
        mod_datos()
# Opción 5
      elif opcion == 5:
        print("\nHa seleccionado la opción 5. Salir.")
        salir()
        break
# Opción no válida
      else:
        print(f"\nLa opción {opcion} no es válida, intente nuevamente.\n")
        print("Debe ser un número del 1 al 5.\n")

    except ValueError:
      print("\nDebe ingresar un número.\n")






# Ejecutar Menú

menu()