import csv
import os
import re

def limpiar_nombre_archivo(nombre):
    # Elimina caracteres no permitidos en nombres de archivos
    nombre = re.sub(r'[\\/*?:"<>|]', "", nombre)
    return nombre.strip()

def generar_archivos_obsidian():
    archivo_csv = 'CU.csv'
    
    if not os.path.exists(archivo_csv):
        print(f"❌ No se encontró el archivo {archivo_csv}")
        return

    with open(archivo_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Configuración de nombres
            nombre_cu = row['Nombre']
            id_cu = row['ID']
            filename = f"{limpiar_nombre_archivo(nombre_cu)}.md"
            
            # Construcción del contenido con Propiedades (YAML)
            # Usamos triple comilla para que Obsidian maneje bien los textos largos
            contenido = "---\n"
            contenido += f"id: {id_cu}\n"
            contenido += f"actores_primarios: \"{row['Actores Primarios']}\"\n"
            contenido += f"actores_secundarios: \"{row['Actores Secundarios']}\"\n"
            contenido += f"tipo: caso_de_uso\n"
            contenido += "---\n\n"
            
            # Cuerpo del archivo
            contenido += f"# {nombre_cu}\n\n"
            
            contenido += "## Descripción\n"
            contenido += f"{row['Descripción']}\n\n"
            
            contenido += "## Condiciones\n"
            contenido += f"**Precondiciones:**\n{row['pre condiciones del sistema']}\n\n"
            contenido += f"**Postcondiciones:**\n{row['poscondiciones']}\n\n"
            
            contenido += "## Flujo Principal\n"
            contenido += f"{row['flujo principal']}\n\n"
            
            if row.get('flujos alternativos') and row['flujos alternativos'] != "N/A":
                contenido += "## Flujos Alternativos\n"
                contenido += f"{row['flujos alternativos']}\n"

            # Guardar el archivo
            try:
                with open(filename, 'w', encoding='utf-8') as f_md:
                    f_md.write(contenido)
                print(f"✅ Creado: {filename}")
            except Exception as e:
                print(f"❌ Error al crear {filename}: {e}")

if __name__ == "__main__":
    generar_archivos_obsidian()

