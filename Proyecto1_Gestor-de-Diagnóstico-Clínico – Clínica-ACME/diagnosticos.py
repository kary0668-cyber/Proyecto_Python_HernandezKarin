import json

# REGISTRAR DIAGNOSTICO
def registrar_diagnostico(datos):
    identificacion = input("Ingrese la identificación del paciente: ")
    
    paciente_encontrado = None
    
    for paciente in datos["pacientes"]:
        if identificacion == paciente["identificacion"]:
            paciente_encontrado = paciente
            break
        
    if paciente_encontrado == None:
        print("El paciente no se encuentra registrado")
        return
    
    identificacion_medico = input("Ingrese la identificación del médico: ")
    
    medico_encontrado = None
    
    for usuario in datos["usuarios"]:
        print("Usuario encontrado en JSON:", usuario["identificacion"], usuario["rol"])
        
        if identificacion_medico == usuario["identificacion"] and usuario["rol"].lower() == "medico":
            medico_encontrado = usuario
            break
        
    if medico_encontrado == None:
        print("El médico no se encuentra registrado o no tiene el rol de médico")
        return
    
    sintomas = input("Ingrese los síntomas del paciente: ")
    
    diagnostico_medico = input("Ingrese el diagnóstico médico: ")
    
    diagnostico = {
        "identificacion_paciente": paciente_encontrado["identificacion"],
        "nombre_paciente": paciente_encontrado["nombre"],
        "identificacion_medico": medico_encontrado["identificacion"],
        "nombre_medico": medico_encontrado["nombre"],
        "sintomas": sintomas,
        "diagnostico": diagnostico_medico
    }
    
    #Registrar medicamentos
    medicamentos = []

    while True:
        nombre_medicamento = input("Ingrese el nombre del medicamento: ")
        cantidad = input("Ingrese la cantidad: ")
        dosis_diaria = input("Ingrese la dosis diaria: ")
        tiempo_aplicacion = input("Ingrese el tiempo de aplicación: ")

        medicamento = {
            "nombre": nombre_medicamento,
            "cantidad": cantidad,
            "dosis_diaria": dosis_diaria,
            "tiempo_aplicacion": tiempo_aplicacion
        }

        medicamentos.append(medicamento)

        continuar = input("¿Desea agregar otro medicamento? (si/no): ")

        if continuar.lower() != "si":
            break
        
    # INCORPORAR MEDICAMENTOS AL DIAGNOSTICO
    diagnostico["medicamentos"] = medicamentos
    
    # AGREGAR DIAGNOSTICO A LA LISTA
    datos["diagnosticos"].append(diagnostico)

    # GUARDAR INFORMACION EN JSON
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

    print("Diagnóstico registrado correctamente")
