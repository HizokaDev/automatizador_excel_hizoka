import os
import pandas as pd
from datetime import datetime
from exportar_excel import exportar_datos

# Columnas clave para identificar cada tipo de archivo
columnas_s400 = {"Nro Liq", "Fecha Liq", "Código Cliente", "Monto Liq", "Estado"}
columnas_fsat = {"ID_Cliente", "Nombre", "Producto", "Fecha", "Total", "TieneError"}

ruta_actual = os.path.dirname(os.path.abspath(__file__))

df_s400 = None
df_fsat = None

# Buscar archivos .xlsx en la carpeta
archivos_excel = [f for f in os.listdir(ruta_actual) if f.endswith(".xlsx")]

for archivo in archivos_excel:
    ruta_archivo = os.path.join(ruta_actual, archivo)
    try:
        df = pd.read_excel(ruta_archivo, engine="openpyxl")  # Se fuerza el motor openpyxl
        columnas_archivo = set(df.columns)

        if columnas_s400.issubset(columnas_archivo) and df_s400 is None:
            df_s400 = df
            print(f"✅ Archivo s400 detectado: {archivo}")
        elif columnas_fsat.issubset(columnas_archivo) and df_fsat is None:
            df_fsat = df
            print(f"✅ Archivo fsat detectado: {archivo}")
        else:
            print(f"🔍 Archivo no identificado (omitido): {archivo}")

    except Exception as e:
        print(f"⚠️ Error al leer {archivo}: {e}")

# Verificar si ambos fueron encontrados
if df_s400 is None or df_fsat is None:
    print("❌ No se detectaron ambos archivos requeridos (s400 y fsat).")
    exit()

# Buscar plantilla base
archivo_madre = "plantilla_base.xlsx"
ruta_excel_madre = os.path.join(ruta_actual, archivo_madre)

if not os.path.exists(ruta_excel_madre):
    print(f"❌ No se encontró el archivo de plantilla base: {archivo_madre}")
    exit()

# Generar ruta de salida
fecha_hoy = datetime.now().strftime("%Y%m%d")
archivo_salida = f"reporte_completo_{fecha_hoy}.xlsx"
ruta_salida = os.path.join(ruta_actual, archivo_salida)

# Exportar datos
exportar_datos(
    excel_madre_path=ruta_excel_madre,
    salida_path=ruta_salida,
    df_s400=df_s400,
    df_fsat=df_fsat,
    confirmar_sobrescritura=False
)

print(f"✅ ¡Datos exportados exitosamente a:\n{ruta_salida}")