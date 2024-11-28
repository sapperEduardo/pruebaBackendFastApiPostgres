import psycopg


class UserConnection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=prueba user=root password=admin host=localhost port=5432")
            print("Conectado con exito!")
        except psycopg.OperationalError as err:
            print("Error al conectarse!")
            print(err)
            self.conn.close()

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
        INSERT INTO "users" (name, phone) VALUES( %(name)s, %(phone)s) 
        """, data)
        self.conn.commit()

    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
        SELECT * FROM "users";
        """)
            return data.fetchall()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
        SELECT * FROM "users" WHERE id = %s;
        """, (id,))
            return data.fetchone()
    
    def update_one(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
            UPDATE "users" SET name= %(name)s, phone= %(phone)s 
                        WHERE id= %(id)s
            """, data)
        self.conn.commit()


    def delete_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
            DELETE FROM "users"	WHERE id = %s;
        """, (id,))
        self.conn.commit()
    





    def __def__(self):
        self.conn.close()