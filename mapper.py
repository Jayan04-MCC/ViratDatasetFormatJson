#!/usr/bin/env python3
import sys
import json
import re

for line in sys.stdin:
    try:
        data = json.loads(line)
        # Extrae el ID de cámara (ej: "VIRAT_S_000001" de los meta)
        camera_id = next(k for k in data["meta"].keys() if re.match(r'VIRAT_S_\d+', k))
        
        # Procesa cada objeto en 'types'
        for obj_id, obj_info in data["types"].items():
            obj_type = obj_info["type"]
            confidence = obj_info["confidence"]
            # Emite: tipo_de_objeto, cámara y confianza
            print(f"{obj_type}\t{camera_id}:{confidence}")
            
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
