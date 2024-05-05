from peewee import *
import mysql.connector


DB = MySQLDatabase(
    'topsis',
    user='root',
    password='1234',
    host='localhost',
    port=3306
)


class User(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=15, unique=True)
    password = CharField(max_length=30)

    def __str__(self):
        return self.username

    class Meta:
        database = DB
        table_name = 'users'


class Tablas(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=30)
    tabla = TextField()
    userid = ForeignKeyField(User, backref='tablas')

    def __str__(self):
        return self.name

    class Meta:
        database = DB
        table_name = 'tablas'


def create_database(nombre_base_de_datos):

    config = {
        'user': 'root',
        'password': '1234',
        'host': 'localhost',
        'port': 3306,
    }

    try:
        # Crear una conexión temporal
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Crear la base de datos si no existe
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_base_de_datos}")

        # Cerrar la conexión temporal
        cursor.close()
        connection.close()

        # Reabrir la conexión utilizando la base de datos recién creada
        config['database'] = nombre_base_de_datos
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        return connection, cursor

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None
