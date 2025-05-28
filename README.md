# VIRAT Object Detection MapReduce

Este proyecto utiliza un enfoque de MapReduce para procesar anotaciones de objetos detectados en videos del dataset **VIRAT**. A través de los scripts `mapper.py` y `reducer.py`, se agrupan los objetos por tipo, mostrando en qué cámaras fueron detectados y con qué nivel de confianza.

## Estructura del Proyecto

- `mapper.py`: Lee las anotaciones en formato JSON línea por línea y emite pares clave-valor en formato `tipo_de_objeto -> cámara:confianza`.
- `reducer.py`: Agrega las salidas del mapper, agrupando por tipo de objeto, eliminando duplicados de cámaras y ordenando por nivel de confianza.

---

## Formato de Entrada

El programa espera datos en **formato JSON por línea**. Ejemplo de entrada:

```json
{
  "meta": {
    "VIRAT_S_000001": { "some_info": "..." }
  },
  "types": {
    "id1": { "type": "Person", "confidence": 0.95 },
    "id2": { "type": "Vehicle", "confidence": 0.87 }
  }
}
```

---

## Mapper (`mapper.py`)

### Función:
Extrae, para cada objeto detectado, su tipo, la cámara donde fue detectado y la confianza asociada.

### Entrada:
Línea por línea desde `stdin`, cada línea debe ser un JSON válido.

### Salida:
Líneas con el formato:
```
<tipo_de_objeto>\t<camera_id>:<confianza>
```

### Ejemplo de salida:
```
Person	VIRAT_S_000001:0.95
Vehicle	VIRAT_S_000001:0.87
```

---

## Reducer (`reducer.py`)

### Función:
Agrupa todas las detecciones por tipo de objeto, elimina duplicados de cámaras y ordena por nivel de confianza descendente.

### Entrada:
Líneas generadas por `mapper.py`.

### Salida:
Líneas con el formato:
```
<tipo_de_objeto>\t<camera_id1>(confianza1),<camera_id2>(confianza2),...
```

### Ejemplo de salida:
```
Person	VIRAT_S_000001(0.9),VIRAT_S_000002(0.8)
Vehicle	VIRAT_S_000003(0.95)
```

---

## Cómo ejecutar

Si tienes un archivo de entrada `input.jsonl` con los datos anotados:

```bash
cat input.jsonl | ./mapper.py | sort | ./reducer.py > output.txt
```

Asegúrate de que ambos scripts tengan permisos de ejecución:

```bash
chmod +x mapper.py reducer.py
```

---

## Requisitos

- Python 3.x
- Entrada en formato JSON por línea (`.jsonl`)
- Estructura esperada con claves `"meta"` y `"types"`

---

## Notas

- Los errores de parseo o datos mal formateados se envían a `stderr`.
- Las cámaras se identifican por patrones como `VIRAT_S_000001` dentro de la sección `"meta"`.
