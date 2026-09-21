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
        qeury="""
                INSERT INTO public.guitars(brand, name, finish, price)
                VALUES (%s, %s, %s, %s)
            """
        values=(guitar.brand, guitar.name, guitar.finish, guitar.price)
        guitar = self.cursor.execute(qeury,values)
        database.connection.commit()
        return guitar

    def update_guitar(self, guitar_id, guitar):
        query = """
                UPDATE public.guitars 
                SET brand = %s, name = %s, price = %s, finish = %s
                WHERE id = %s;
            """
        
        new_values = (guitar.brand, guitar.name, guitar.price, guitar.finish, guitar_id)
        guitar = self.cursor.execute(query, new_values)
        database.connection.commit()

    def delete_guitar(self, guitar_id):
        self.cursor.execute("DELETE FROM public.guitars WHERE id=%s", (guitar_id,))

    def get_guitar_details(self, guitar_id):
        self.cursor.execute("SELECT * FROM public.guitars WHERE id = %s",(guitar_id,))
        return self.cursor.fetchone()


guitar_repository = GuitarsRepository(database=database)