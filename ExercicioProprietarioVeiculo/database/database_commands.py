from .database import get_connection

class Get_Proprietarios:

    def __init__(self):
        self.conn = get_connection()
        cursor = self.conn.cursor()
        cursor.execute("insert into proprietarios values ('teste1','12345678900','Carro 1')", (prop_id,))

    def get_proprietario(self, prop_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proprietarios WHERE id=?", (prop_id,))
        return cursor.fetchone()
    
    def get_all_proprietarios(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM proprietarios")
        return cursor.fetchall()