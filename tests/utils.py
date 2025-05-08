import json
from pathlib import Path
from configuraciones.models import Provincia


class TestUtils:
    """
    Clase auxiliar para crear datos de prueba relacionados con Relevamiento.
    """

    @staticmethod
    def cargar_initial_data(json_file, datos):
        # Obtener la ruta al archivo JSON
        data_dir = Path(__file__).parent / "mocked_data"
        json_path = data_dir / json_file

        # Cargar el JSON
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Reemplazar placeholders con valores reales
        initial_data = data["initial_data"]

        # Reemplazar valores dinámicos
        replacements = {
            "{{comedor_id}}": str(datos["comedor"].id),
            "{{modalidad_prestacion_nombre}}": datos["modalidad_prestacion"].nombre,
            "{{tipo_espacio_nombre}}": datos["tipo_espacio"].nombre,
            "{{cantidad_colaboradores_nombre}}": datos["cantidad_colaboradores"].nombre,
        }

        # Función para reemplazar en toda la estructura
        def replace_values(obj):
            if isinstance(obj, dict):
                return {k: replace_values(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [replace_values(item) for item in obj]
            elif isinstance(obj, str) and obj in replacements:
                return replacements[obj]
            return obj

        return replace_values(initial_data)

 