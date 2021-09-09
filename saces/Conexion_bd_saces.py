from datos_prueba import *
import psycopg2


class DataBase:

    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="saces3",
            user="postgres",
            password="12345678"
        )
        self.cursor = self.connection.cursor()
        print('conexion exitosa')

    def borrar_registros(self):
        sql = "delete from registro_acreditacion where resolucion in ('1','2','3','4','5');"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def get_registros_test(self):
        sql = "select id from registro_acreditacion  where resolucion in ('1','2','3','4','5')";
        try:
            self.cursor.execute(sql)
            list = self.cursor.fetchall()
            return list
        except Exception as e:
            raise

    def crear_registros(self):
        sql = insert_resoluciones()
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def borrar_actividades(self):
        sql = """delete from actividades where reg_id in (select id
								from registro_acreditacion 
								where resolucion in ('1','2','3','4','5')
	        )"""
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise


    def crear_actividades(self):
        list=db.get_registros_test()
        sql = ''
        for id in list:
            sql+=sql_actividades(id[0])
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise



db = DataBase()
db.borrar_actividades()
db.borrar_registros()
db.crear_registros()
db.crear_actividades()








