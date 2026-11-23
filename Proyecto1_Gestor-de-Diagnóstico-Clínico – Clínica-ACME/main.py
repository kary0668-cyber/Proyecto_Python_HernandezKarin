import json
from usuarios import registrar_usuario
from pacientes import registrar_paciente
from diagnosticos import registrar_diagnostico
from historias_clinicas import consultar_historia_clinica

#Funcion para cargar los datos (Y)
def cargar_datos():
    with open("datos.json", "r", ) as archivo:
        datos = json.load(archivo)
        
    return datos
    
    
#Funion para guardar los datos 
def guardar_datos(datos):
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
        
#cargar informacion del JSON
datos = cargar_datos()

#Iniciar sesion
print("------ CLÍNICA ACME ------")

correo = input("Ingrese su correo: ")
contrasena = input("Ingrese su contraseña: ")

acceso = False

for usuario in datos["usuarios"]:
    
    if correo == usuario["correo"] and contrasena == usuario["contrasena"]:
        print("Bienvenido a la Clínica ACME")
        acceso = True
        break
    
#Menú principal
if acceso:
    
    while True:
        print("""
-------- CLíNICA ACME -------
1. Registrar usuarios
2. Registrar pacientes
3. Diagnosticar pacientes
4. Consultar historia clinica
5. Cerrar sesion
---------------------------------------------
""")
        opcion=input("Elige la opcion: ")
        if opcion=="1":
            registrar_usuario(datos)
            
        elif opcion=="2":
            registrar_paciente(datos)
            
        elif opcion=="3":
            registrar_diagnostico(datos)
            
        elif opcion=="4":
            consultar_historia_clinica(datos)
        elif opcion=="5":
            print("Cerrar sesion...")
            break
        else:
            print("Opcion incorrecta. Intentelo denuevo.")
else:
    print("Usuario o contraseña incorrecta")
