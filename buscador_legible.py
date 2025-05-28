#!/usr/bin/env python3
def parse_inverted_index_line(line):
    try:
        keyword, videos_str = line.strip().split(' ', 1)
        videos = videos_str.split(',')
        
        print(f"🔍 Palabra clave: {keyword}")
        print("📹 Videos relacionados:")
        for i, video in enumerate(videos, 1):
            print(f"  {i}. {video}")
    except ValueError:
        print("❌ Formato no válido en la línea.")

# Ejemplo: línea de salida del comando
linea_salida = "Animal VIRAT_S_000204_04_000738_000977,VIRAT_S_040003_06_001441_001518"

parse_inverted_index_line(linea_salida)

