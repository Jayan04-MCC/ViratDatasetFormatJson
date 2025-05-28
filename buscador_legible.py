#!/usr/bin/env python3
import subprocess
from prettytable import PrettyTable

def buscar_y_formatear(objeto):
    # Obtener datos del índice desde HDFS
    comando = f"hdfs dfs -cat /indice_objetos_mejorado/part-* | grep -i '{objeto}'"
    resultado = subprocess.getoutput(comando)
    
    if not resultado:
        print(f"\n🔍 No se encontró el objeto '{objeto}' en el índice.")
        return

    # Procesar la línea del índice (ej: "Tree\tVIRAT_S_0001,VIRAT_S_0002")
    objeto, lista_camaras = resultado.split('\t')
    camaras = lista_camaras.split(',')

    # Crear tabla
    tabla = PrettyTable()
    tabla.title = f"📌 Cámaras con el objeto: {objeto.strip()}"
    tabla.field_names = ["#", "ID Cámara", "Detalles"]
    tabla.align = "l"

    # Agregar filas (agrupando cámaras similares)
    for idx, camara in enumerate(sorted(set(camaras)), 1):
        # Extraer segmento numérico para cámaras tipo VIRAT_S_XXXXX_XX_XXXXXX_XXXXXX
        partes = camara.split('_')
        detalle = f"Secuencia: {partes[-2]}-{partes[-1]}" if len(partes) > 4 else "Sin segmentos"
        tabla.add_row([idx, camara.strip(), detalle])

    # Mostrar resultados
    print(tabla)
    print(f"\n📊 Total de cámaras encontradas: {len(camaras)}")

if __name__ == "__main__":
    objeto = input("\nIngrese el objeto a buscar (ej: Tree, Vehicle, Person): ").strip()
    buscar_y_formatear(objeto)
