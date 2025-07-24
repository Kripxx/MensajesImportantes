from config.database import Database


class CitacionModel:
    def __init__(self):
        self.db = Database()

    def crear_citacion(self, area_id, motivo_id, asunto, contenido):
        query = """
        INSERT INTO citaciones (area_id, motivo_id, asunto, contenido)
        VALUES (%s, %s, %s, %s)
        """
        return self.db.execute(query, (area_id, motivo_id, asunto, contenido))

    def obtener_todas(self):
        query = """
        SELECT c.*, a.nombre as area_nombre, m.nombre as motivo_nombre 
        FROM citaciones c
        JOIN areas a ON c.area_id = a.id
        JOIN motivos m ON c.motivo_id = m.id
        """
        return self.db.fetch_all(query)