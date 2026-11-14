import json

# CONSULTAR HISTORIA CLINICA
def consultar_historia_clinica(datos):

    identificacion = input("Ingrese la identificación del paciente: ")

    paciente_encontrado = None

    for paciente in datos["pacientes"]:
        if identificacion == paciente["identificacion"]:
            paciente_encontrado = paciente
            break

    if paciente_encontrado == None:
        print("El paciente no se encuentra registrado")
        return
    
    print("------ HISTORIA CLINICA ------")
    print("Paciente:", paciente_encontrado["nombre"])
    print("Identificación:", paciente_encontrado["identificacion"])
    
    diagnostico_encontrado = False

    for diagnostico in datos["diagnosticos"]:
        if identificacion == diagnostico["identificacion_paciente"]:
            diagnostico_encontrado = True 

            print("Síntomas:", diagnostico["sintomas"])
            print("Diagnóstico:", diagnostico["diagnostico"])
            print("Médico:", diagnostico["nombre_medico"])

            print("MEDICAMENTOS FORMULADOS")

            for medicamento in diagnostico["medicamentos"]:
                print("Medicamento:", medicamento["nombre"])
                print("Cantidad:", medicamento["cantidad"])
                print("Dosis diaria:", medicamento["dosis_diaria"])
                print("Tiempo de aplicación:", medicamento["tiempo_aplicacion"])
    if diagnostico_encontrado == False:
        print("El paciente no tiene diagnósticos registrados")            