import os

# Configuración de carpetas
base_dir = "Clase_Calidad_Sistemas"
ejercicios_dir = os.path.join(base_dir, "ejercicios_python")
os.makedirs(ejercicios_dir, exist_ok=True)

# 1. Contenido de los 10 ejercicios
ejercicios = {
    "ej01_pep8.py": """# MAL CÓDIGO
def f(a,b):
 return a*b

# CÓDIGO DE CALIDAD (PEP 8 + Type Hints)
def calcular_area_rectangulo(base: float, altura: float) -> float:
    \"\"\"Calcula el área de un rectángulo basándose en sus dimensiones.\"\"\"
    return base * altura
""",
    "ej02_complejidad.py": """# MAL CÓDIGO (Alta Complejidad Ciclomática)
def obtener_dia(n):
    if n == 1: return "Lunes"
    elif n == 2: return "Martes"
    elif n == 3: return "Miércoles"
    # ... esto escala mal

# CÓDIGO DE CALIDAD (Uso de Diccionarios)
def obtener_nombre_dia(dia_idx: int) -> str:
    dias = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes"}
    return dias.get(dia_idx, "Día no válido")
""",
    "ej03_excepciones.py": """import logging

# MAL CÓDIGO (Silenciar errores)
try:
    res = 10 / 0
except:
    pass

# CÓDIGO DE CALIDAD (Excepciones específicas y Logging)
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"Error de división: {e}")
""",
    "ej04_srp.py": """# CÓDIGO DE CALIDAD (Principio de Responsabilidad Única)
class ReporteManager:
    def leer_datos(self): pass
    def calcular_metricas(self): pass
    def generar_pdf(self): pass

# En lugar de tener una sola función gigante que hace las tres cosas.
""",
    "ej05_hardcoding.py": """import os

# MAL CÓDIGO
api_key = "SECRET_12345"

# CÓDIGO DE CALIDAD (Variables de Entorno)
api_key = os.getenv("API_KEY_SERVICE", "valor_por_defecto_seguro")
""",
    "ej06_typing.py": """from typing import List, Dict

# CÓDIGO DE CALIDAD (Tipado Estático para evitar bugs)
def procesar_usuarios(usuarios: List[str]) -> Dict[str, int]:
    return {u: len(u) for u in usuarios}
""",
    "ej07_dry.py": """# CÓDIGO DE CALIDAD (Don't Repeat Yourself)
def formatear_moneda(valor: float) -> str:
    return f"${valor:,.2f}"

# Se usa esta función en lugar de escribir f"${v:,.2f}" en 10 lugares distintos.
""",
    "ej08_docstrings.py": """# CÓDIGO DE CALIDAD (Documentación Estándar)
def enviar_email(destino: str, asunto: str):
    \"\"\"
    Envía un correo electrónico de notificación.
    
    Args:
        destino (str): Correo del receptor.
        asunto (str): Título del mensaje.
    \"\"\"
    pass
""",
    "ej09_generadores.py": """# CÓDIGO DE CALIDAD (Eficiencia de Memoria)
def leer_archivo_gigante(ruta):
    # Usa un generador para no cargar todo en RAM
    with open(ruta) as f:
        for linea in f:
            yield linea.strip()
""",
    "ej10_seguridad.py": """import ast

# MAL CÓDIGO (Vulnerable a Inyección)
# resultado = eval(input("Suma: ")) 

# CÓDIGO DE CALIDAD (Evaluación Segura)
entrada = "5 + 10"
resultado = ast.literal_eval(entrada) if entrada.isdigit() else "Error"
"""
}

# 2. Guion para la presentación (Markdown)
teoria_md = """# Clase: Calidad de los Sistemas Informáticos


"""

# Escribir archivos
for nombre, contenido in ejercicios.items():
    with open(os.path.join(ejercicios_dir, nombre), "w", encoding="utf-8") as f:
        f.write(contenido)

with open(os.path.join(base_dir, "PRESENTACION.md"), "w", encoding="utf-8") as f:
    f.write(teoria_md)

print(f"¡Listo! Revisa la carpeta '{base_dir}'")