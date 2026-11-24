import json
from collections import Counter

def cargar_datos():
    with open("datos.json", "r", encoding=utf-8) as archivo:
        datos = json.load(archivo)
    return datos

def validar_fecha(fecha):
    if len(fecha) != 10:
        return False
    
    if fecha[4] != "-" or fecha[7] != "-":
        return False
    
    return True

def reporte_anual_giagnostico():
    datos = cargar_datos()
    
    diagnostico = datos["diagnosticos"]
    usuarios = datos["usuarios"]
    pacientes = datos["pacientes"]
    
    anos = {}
    invalidos = 0 
    
    #agrup
    for diagnostico in diagnostico:
        
        fecha = diagnostico["fecha"]
        
        if not validar_fecha(fecha):
            invalidos += 1
            continue
        
        ano = fecha[:4]
        
        if ano not in anos:
            anos[ano] = []
            
        anos[ano].append(diagnostico)
        
    reporte = {"anos": {}}
    
    for ano, registro in anos.item():
        medicos = set
        pacientes_unicos = set()
        
        total_sintomas = 0
        total_medicamentos = 0
        
        nombres_diagnosticos = []
        
    for registro in registros:
        medicos.add(registros["medico_id"])
        pacientes_unicos.add(registro["paciente_id"])
        
        total_sintomas += len(registro["sintomas"])
        total_medicamentos += len(registro "medicamentos")
        
        nombres_diagnosticos.append(registro["diagnosticos"])
        
    contador = Counter(nombres_diagnosticos)
    diagnostico_mas_comun = contador.most_common(1)[0][0]
    
    registros_ordenados =sorted(
        registros,
        key=lambda registro: registro["fecha"]
    )
    
    total = len(registros)
    reporte["anos"][ano] = {
        "total_diagnostico": total,
        "medicos_participantes": len(medicos),
        "pacientes_atendidos": len(pacientes_unicos),
        "promedio_sintomas": round(total_sintomas / total, 2)
        "promedio_medicamentos": round(total_medicamentos / total, 2),
        "diagnostico_mas_comun":diagnostico_mas_comun,
        "primer_diagnostico": registro_ordenados[0],
        "ultimo_diagnostico":registro_ordenados[-1]
}

with open(
    "roporte_anual_diagnostico.json",
    "w"
    encoding="utf-8"
) as archivo:
    json.dump(reporte, archivo, indent=4, ensure_ascii=False)
    
    print("\n--- INFORME ANUAL ---")
    print("Informe generado correctamente.")
    print("Diagnosticos con fecha invalida:",invalidos)