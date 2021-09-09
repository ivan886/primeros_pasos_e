import psycopg2

class DataBase:

    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost',
            database='marvel',
            user='postgres',
            password='12345678'
        )
        self.cursor = self.connection.cursor()
        print('conexion exitosa')

    def lista_personajes(self):
        sql = "select id, name, description, universe_id  from characters"
        try:
            self.cursor.execute(sql)
            lista = self.cursor.fetchall()
            return lista
        except Exception as e:
            raise


bd = DataBase()
lista = bd.lista_personajes()

print(lista)
