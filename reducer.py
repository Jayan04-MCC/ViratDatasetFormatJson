#!/usr/bin/env python3
import sys
from collections import defaultdict

index = defaultdict(list)

for line in sys.stdin:
    try:
        obj_type, camera_data = line.strip().split("\t")
        camera_id, confidence = camera_data.split(":")
        index[obj_type].append((camera_id, float(confidence)))
    except ValueError:
        continue

# Ordena por confianza (mayor primero) y elimina duplicados
for obj_type in index:
    unique_cams = {}
    for cam, conf in sorted(index[obj_type], key=lambda x: x[1], reverse=True):
        if cam not in unique_cams:
            unique_cams[cam] = conf
    
    # Formato: "Tipo -> Cámara(confianza),Cámara(confianza)"
    cam_list = ",".join([f"{cam}({conf:.1f})" for cam, conf in unique_cams.items()])
    print(f"{obj_type}\t{cam_list}")
