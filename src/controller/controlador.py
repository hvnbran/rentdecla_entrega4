import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import psycopg2
import SecretConfig

# Función para conectarse a la base de datos
def conectar_db():
    try:
        conn = psycopg2.connect(
            host=SecretConfig.PGHOST,
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        return None  # No se imprime el mensaje de error para evitar problemas en las pruebas

# Función para agregar un nuevo usuario
def agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono, salario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "INSERT INTO usuarios (Nombre, Apellido, Documento_Identidad, Correo_Electronico, Telefono, Salario) VALUES (%s, %s, %s, %s, %s, %s)"
                cur.execute(sql, (nombre, apellido, documento_identidad, correo_electronico, telefono, salario ))
                conn.commit()
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print(f"Error al agregar el usuario: {error}")

# Función para agregar una nueva declaración de renta
def agregar_declaracion(Ingresos_laborales, Otros_ingresos,Retenciones, Seguridad_social,Aportes_pension, Gastos_creditos_hipotecarios, Donaciones, Gastos_educacion, id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "INSERT INTO retencion (Ingresos_laborales, Otros_ingresos,Retenciones, Seguridad_social,Aportes_pension, Gastos_creditos_hipotecarios, Donaciones, Gastos_educacion, id_usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql, (Ingresos_laborales, Otros_ingresos,Retenciones, Seguridad_social,Aportes_pension, Gastos_creditos_hipotecarios, Donaciones, Gastos_educacion, id_usuario))
                conn.commit()
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print(f"Error al agregar la declaración de renta: {error}")

# Función para consultar los datos de un usuario y su declaración de renta
def consultar_usuario(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                # Consultar datos del usuario
                sql = "SELECT * FROM usuarios WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                usuario = cur.fetchone()
                
                # Consultar datos de la declaración de renta
                sql = "SELECT * FROM declaracion WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                declaracion = cur.fetchone()
                
                if usuario:
                    print("Datos del usuario:")
                    print(f"ID_Usuario: {usuario[0]}")
                    print(f"Nombre: {usuario[1]}")
                    print(f"Apellido: {usuario[2]}")
                    print(f"Documento_Identidad: {usuario[3]}")
                    print(f"Correo_Electronico: {usuario[4]}")
                    print(f"Telefono: {usuario[5]}")
                    print(f"Salario: {usuario[8]}")
                    
                    if declaracion:
                        print("\nDatos de la declaración de renta:")
                        print(f"Ingresos_laborales: {declaracion[1]}")
                        print(f"Otros_ingresos: {declaracion[2]}")
                        print(f"Retenciones: {declaracion[3]}")
                        print(f"Seguridad_social: {declaracion[4]}")
                        print(f"Aportes_pension: {declaracion[5]}")
                        print(f"Gastos_creditos_hipotecarios: {declaracion[6]}")
                        print(f"Donaciones: {declaracion[6]}")
                        print(f"Gastos_educacion: {declaracion[6]}")
                        print(f"Total a pagar: {declaracion[7]}")
                else:
                    print("No se encontró el usuario.")
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print(f"Error al consultar el usuario: {error}")


# Función para eliminar un usuario
def eliminar_usuario(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "DELETE FROM usuarios WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                conn.commit()
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print(f"Error al eliminar el usuario: {error}")
