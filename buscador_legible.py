#!/usr/bin/env python3
import subprocess

def parse_inverted_index_line(line):
    try:
        keyword, videos_str = line.strip().split(' ', 1)
        videos = sorted(videos_str.split(','))
        
        print(f"\n🔍 Palabra clave: {keyword}")
        print("📹 Videos relacionados (ordenados):")
        for i, video in enumerate(videos, 1):
            print(f"  {i}. {video}")
    except ValueError:
        print("❌ Formato no válido en la línea.")

def buscar_palabra_clave(palabra):
    comando = f"./../bin/hdfs dfs -cat /indice_invertido/part-00000 | grep -i '{palabra}'"
    resultado = subprocess.getoutput(comando)

    if resultado:
        parse_inverted_index_line(resultado)
    else:
        print(f"🔍 No se encontraron resultados para '{palabra}'.")

if __name__ == "__main__":
    palabra = input("🔎 Ingresa la palabra clave a buscar: ").strip()
    if palabra:
        buscar_palabra_clave(palabra)
    else:
        print("⚠️ No se ingresó ninguna palabra.")


