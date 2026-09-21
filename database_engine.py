import psycopg2


class DatabaseEngine:
    def __init__(self, url):
        self.connection = psycopg2.connect(url)

    def get_cursor(self):
        cursor = self.connection.cursor()
        return cursor
    


database = DatabaseEngine(url="postgresql://postgres:0000@localhost:5432/postgres")