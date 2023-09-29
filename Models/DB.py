import psycopg # this uses psycopg version 3


class DBConnection:
    def __init__(self, database, user, password, host, port):
        self.user = user
        self.database = database
        self.password = password
        self.host = host
        self.port = port
        self.config =  {'user':user,
            'password':password,
            'host':host,
            'port':port,
            'dbname':database}

    def request(self, query, parameters):
        with psycopg.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                return cursor.execute(query, parameters).fetchall()

    def insert(self, query, parameters):
        with psycopg.connect(**self.config) as conn:
            with conn.cursor() as cursor:
                return cursor.execute(query, parameters)


"""
    def connection(self, database, user, password, host, port):
        config = {'user':user,
            'password':password,
            'host':host,
            'port':port,
            'dbname':database}
        try:
            cnx = psycopg.connect(**config)
        except psycopg.Error as err:
            print(err)
            exit(1)
        else:
            return cnx
"""

