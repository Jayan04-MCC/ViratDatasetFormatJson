#!/usr/bin/env python3
import subprocess
from prettytable import PrettyTable

def buscar_y_formatear(objeto_buscado):
    comando = "hdfs dfs -cat /indice_objetos_mejorado/part-*"
    resultado = subprocess.getoutput(comando)
    
    lineas = resultado.strip().splitlines()
    
    camaras_encontradas = []
    objeto_actual = None
    
    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue
        
        if not ',' in linea:
            # Esta línea es el nombre del objeto
            objeto_actual = linea.strip()
        else:
            # Esta línea contiene cámaras
            if objeto_actual and objeto_actual.lower() == objeto_buscado.lower():
                camaras = [c.strip() for c in linea.split(',')]
                camaras_encontradas.extend(camaras)
    
    if not camaras_encontradas:
        print(f"\n🔍 No se encontró el objeto '{objeto_buscado}' en el índice.")
        return

    # Crear tabla
    tabla = PrettyTable()
    tabla.title = f"📌 Cámaras con el objeto: {objeto_buscado}"
    tabla.field_names = ["#", "ID Cámara", "Detalles"]
    tabla.align = "l"

    for idx, camara in enumerate(sorted(set(camaras_encontradas)), 1):
        partes = camara.strip().split('_')
        detalle = f"Secuencia: {partes[-2]}-{partes[-1]}" if len(partes) > 4 else "Sin segmentos"
        tabla.add_row([idx, camara.strip(), detalle])

    print(tabla)
    print(f"\n📊 Total de cámaras encontradas: {len(set(camaras_encontradas))}")

if __name__ == "__main__":
    objeto = input("\nIngrese el objeto a buscar (ej: Tree, Vehicle, Person): ").strip()
    buscar_y_formatear(objeto)
