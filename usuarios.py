import json

#registro de usuario
def registrar_usuario(datos):
    identificacion = input("Ingrese la identificación: ")
    nombre = input("Ingrese el nombre: ")
    apellidos = input("Ingrese los apellidos: ")
    telefono = input("Ingrese el telefono:")
    correo = input("Ingrese el correo: ")
    direccion = input("Ingrese la dirección: ")
    contrasena = input("Ingrese la contraseña: ")
    rol = input("Ingrese el rol (medico/administrativo): ")
    
    #VALIDAR SI EL USUARIO YA EXISTE
    for usuario_existente in datos["usuarios"]:
        if identificacion == usuario_existente["identificacion"] or correo == usuario_existente["correo"]:
            return


#cREAR DICCIONARIO
    usuario ={
    "identificacion": identificacion,
    "nombre": nombre,
    "apellidos": apellidos,
    "telefono": telefono,
    "correo": correo,
    "direccion": direccion,
    "contrasena": contrasena,
    "rol": rol
}
    #agregar usuario a la lista
    datos["usuarios"].append(usuario)
    
    #guardar informacion en json
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
        
    print("Usuaruio registrado correctamente")