from .DB import DBConnection

class UserController:

    def __init__(self, connection):
        self.connection = connection

    #these should be name, image_id, salt, password_hash)
    def insert(self, parameters):
        query = """
        INSERT INTO main_schema."Users"(
        user_image_id, salt, password_hash, first_name)
        VALUES (%s, %s, %s, %s);
        """
        self.connection.insert(query, parameters)

    def request_name(self, name):
        query = """
        SELECT * from main_schema."Users"
        WHERE first_name = %s;
        """
        return self.connection.request(query, [name])
    

