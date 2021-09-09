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


    def insertar_poderes(self, poder):
        sql = f"INSERT INTO powers(name) VALUES ( '{poder}');\n "
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise





poderes = ['Volar',
           'Invisibilidad',
           'Súper fuerza',
           ' Manipulación del fuego',
           'Súper velocidad',
           'Telepatía',
           'Creaciones de luz',
           'Invulnerabilidad',
           'Telequinesis',
           'Cambiar de forma']

bd = DataBase()
for poder in poderes:
    bd.insertar_poderes(poder)
