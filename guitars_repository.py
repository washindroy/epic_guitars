from database_engine import database

class GuitarsRepository:
    def __init__(self, database):
        self.connection = database.connection
        self.cursor = self.connection.cursor()

    def get_guitars_list(self, limit=10):
        self.cursor.execute("SELECT * FROM public.guitars LIMIT %s",(limit,))
        guitars = self.cursor.fetchall()
        return guitars

    def create_guitar(self, guitar):
        query="""
                INSERT INTO public.guitars(brand, name, finish, price)
                VALUES (%s, %s, %s, %s)
                RETURNING *
            """
        values=(guitar.brand, guitar.name, guitar.finish, guitar.price)
        self.cursor.execute(query, values)
        created_guitar = self.cursor.fetchone()
        self.connection.commit()
        return created_guitar

    def update_guitar(self, guitar_id, guitar):
        query = """
                UPDATE public.guitars 
                SET brand = %s, name = %s, price = %s, finish = %s
                WHERE id = %s
                RETURNING *
            """
        
        new_values = (guitar.brand, guitar.name, guitar.price, guitar.finish, guitar_id)
        self.cursor.execute(query, new_values)
        updated_guitar = self.cursor.fetchone()
        self.connection.commit()
        return updated_guitar

    def delete_guitar(self, guitar_id):
        self.cursor.execute("DELETE FROM public.guitars WHERE id=%s", (guitar_id,))
        self.connection.commit()

    def get_guitar_details(self, guitar_id):
        self.cursor.execute("SELECT * FROM public.guitars WHERE id = %s",(guitar_id,))
        return self.cursor.fetchone()


guitar_repository = GuitarsRepository(database=database)