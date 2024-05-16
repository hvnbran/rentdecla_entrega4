import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from controller.controlador import conectar_db, agregar_usuario, agregar_declaracion, consultar_usuario, eliminar_usuario

def main():
    while True:
        print("Selecciona una opción:")
        print("1. Agregar usuario")
        print("2. Agregar declaración de renta")
        print("3. Consultar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Ingresa el número de la opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del usuario: ")
            apellido = input("Ingresa el apellido del usuario: ")
            documento_identidad = input("Ingresa el documento de identidad del usuario: ")
            correo_electronico = input("Ingresa el correo electrónico del usuario: ")
            telefono = input("Ingresa el teléfono del usuario: ")
            salario = float(input("Ingresa el salario del usuario: "))
            agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono, salario)
            print("Usuario agregado exitosamente.")

        elif opcion == "2":
            Ingresos_laborales = float(input("Ingresos laborales: "))
            Otros_ingresos = float(input("Otros ingresos: "))
            Retenciones = float(input("Ingrese sus retenciones en la fuente: "))
            Seguridad_social = float(input("Ingrese su aporte a la seguridad social: "))
            Aportes_pension = float(input("Ingrese sus aportes a la pension: "))
            Gastos_creditos_hipotecarios = float(input("Ingrese sus gastos en creditos hipotecarios: "))
            Donaciones = float(input("Ingrese sus donaciones: "))
            Gastos_educacion = float(input("Ingrese sus gastos en educacion: "))
            id_usuario = int(input("Ingresa el ID del usuario: "))
            agregar_declaracion(Ingresos_laborales, Otros_ingresos,Retenciones, Seguridad_social,Aportes_pension, Gastos_creditos_hipotecarios, Donaciones, Gastos_educacion, id_usuario)
            print("Declaración de renta agregada exitosamente.")

        elif opcion == "3":
            id_usuario = int(input("Ingresa el ID del usuario a consultar: "))
            consultar_usuario(id_usuario)

        elif opcion == "4":
            id_usuario = int(input("Ingresa el ID del usuario a eliminar: "))
            eliminar_usuario(id_usuario)
            print("Usuario eliminado exitosamente.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
