#!/bin/bash

# Script para buscar una palabra en el índice invertido de HDFS y mostrar resultados formateados

# Configuración
HDFS_BIN_PATH="./usr/local/hadoop/bin/hdfs"
HDFS_FILE_PATH="/indice_invertido/part-00000"

# Función para mostrar ayuda
mostrar_ayuda() {
    echo "Uso: $0 [-h]"
    echo "Busca una palabra en el índice invertido de HDFS y muestra los resultados formateados."
    echo ""
    echo "Opciones:"
    echo "  -h    Mostrar esta ayuda"
}

# Procesar opciones
while getopts ":h" opcion; do
    case $opcion in
        h)
            mostrar_ayuda
            exit 0
            ;;
        *)
            echo "Opción inválida: -$OPTARG" >&2
            mostrar_ayuda
            exit 1
            ;;
    esac
done

# Solicitar palabra al usuario
read -p "Ingrese la palabra a buscar: " palabra

# Verificar si se ingresó una palabra
if [ -z "$palabra" ]; then
    echo "Error: Debe ingresar una palabra para buscar."
    exit 1
fi

# Ejecutar el comando HDFS y procesar la salida
echo -e "\nBuscando '$palabra' en el índice invertido..."
echo "========================================"

resultado=$("$HDFS_BIN_PATH" dfs -cat "$HDFS_FILE_PATH" | grep -i "\"$palabra\"")

if [ -z "$resultado" ]; then
    echo "No se encontraron coincidencias para '$palabra'."
    exit 0
fi

# Procesar y formatear la salida
echo -e "\nResultados para: $palabra"
echo "----------------------------------------"

# Extraer y mostrar las ubicaciones
ubicaciones=$(echo "$resultado" | awk -F'"' '{print $2}' | tr ',' '\n' | sed 's/^ *//;s/ *$//')

contador=1
while IFS= read -r linea; do
    if [ -n "$linea" ]; then
        echo "$contador. $linea"
        ((contador++))
    fi
done <<< "$ubicaciones"

echo -e "\nBúsqueda completada. Se encontraron $((contador-1)) ubicaciones."
