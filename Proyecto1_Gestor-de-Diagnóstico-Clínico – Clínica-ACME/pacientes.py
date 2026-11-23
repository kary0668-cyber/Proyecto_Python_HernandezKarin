import json

#registrar paciente 
def registrar_paciente(datos):
    identificacion = input("Ingrese la identificación: ")
    nombre = input("Ingrese el nombre: ")
    apellidos = input("Ingrese los apellidos: ")
    telefono = input("Ingrese el telefono:")
    correo = input("Ingrese el correo: ")
    direccion = input("Ingrese la direccion: ")
    genero = input("Ingrese el genero: ")
    estado_civil = input("Ingrese el estado civil: ")
    
    #VALIDAR SI EL PACIENTE YA EXISTE
    for paciente_existente in datos["pacientes"]:
        if identificacion == paciente_existente["identificacion"] or correo == paciente_existente["correo"]:
            print("Paciente registrado correctamente")
            return    
    
    #Crerar diccionario paraincorporarlo a la lista de pacientes y guardarlo en el archivo JSON.
    paciente ={
    "identificacion": identificacion,
    "nombre": nombre,
    "apellidos": apellidos,
    "telefono": telefono,
    "correo": correo,
    "direccion": direccion,
    "genero": genero,
    "estado_civil": estado_civil
}

    #agregar usuario a la lista
    datos["pacientes"].append(paciente)
    
    #guardar informacion en json
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
        
        print("Paciente registrado correctamente")    