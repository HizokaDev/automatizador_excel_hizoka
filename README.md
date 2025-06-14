4# 🧾 Automatizador de Reportes Excel

Este proyecto permite consolidar automáticamente datos desde múltiples archivos Excel con estructuras distintas (como informes de pagos y transferencias) hacia una plantilla base, generando un reporte unificado listo para análisis o uso en Power BI.

---

## 🚀 ¿Qué hace este programa?

- 📥 Carga datos desde dos archivos `.xlsx`:
  - `s400.xlsx`: Liquidaciones o pagos
  - `fsat.xlsx`: Detalle de transferencias
- 🔎 Detecta automáticamente los archivos por su contenido, no por su nombre.
- 🛠️ Une ambos datasets en una **plantilla base prediseñada**
- 📤 Exporta un nuevo archivo con la fecha del día

---

## 🧠 ¿Qué lo hace especial?

- ✅ Funciona con archivos reales sin necesidad de modificarlos
- ✅ Detecta el tipo de archivo leyendo sus columnas
- ✅ Modularizado: funciones separadas para exportar, procesar y ejecutar
- ✅ Generación automática del nombre de salida
- ✅ Compatible con Windows y Pydroid3

---

## 📁 Estructura del proyecto


## ▶️ ¿Cómo usar?

1. Copia todos los archivos a una misma carpeta (por ejemplo, `scripts/`).
2. Asegúrate de tener Python y los paquetes `pandas` y `openpyxl` instalados.
3. Ejecuta el script `actualizar_reporte.py` desde consola o Pydroid3.

---

## ⚙️ Requisitos

- Python 3.x
- pandas
- openpyxl

Instala con:

```bash
pip install pandas openpyxl


---

🆕 Próxima actualización

📦 En camino: versión empaquetada en .zip con ejecutable .bat para uso directo en Windows sin conocimientos técnicos.
Pronto disponible como versión portátil para clientes.


---

👤 Autor

Desarrollado por Hizoka, como parte de su entrenamiento autodidacta en automatización de tareas con Python y Excel.



---

📝 Licencia

Uso libre para fines educativos y personales. Créditos al autor.
