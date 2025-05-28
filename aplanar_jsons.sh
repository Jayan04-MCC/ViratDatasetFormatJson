#!/bin/bash

# Carpeta de entrada y salida
ENTRADA="./"                    # donde están tus VIRAT_S_*.json
SALIDA="./json_aplanados"      # carpeta destino

mkdir -p "$SALIDA"

for i in {0..50}; do
    archivo=$(printf "VIRAT_S_%d.json" "$i")

    if [[ -f "$ENTRADA/$archivo" ]]; then
        echo "Procesando $archivo..."
        jq -c . "$ENTRADA/$archivo" > "$SALIDA/$archivo"
    else
        echo "Archivo $archivo no encontrado, se omite."
    fi
done

echo "¡Listo! JSONs aplanados guardados en $SALIDA"
