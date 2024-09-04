class User:
    """
    This class represents a User object and extends the BBDD class to interact with the database.

    Attributes:
        Inherits all attributes from the BBDD class.

    Methods:
        __create_user(username, password): Inserts a new user record into the USER table with the provided username and password.
        get_usuario(username): Retrieves user information from the USER table based on the username.
        update_password(username, new_password): Updates the password of a user in the USER table.
        delete_usuario(username): Deletes a user record from the USER table based on the username.
        close_connection(): Closes the connection to the database.
    """
    def __init__(self, con) -> None:
        """
        Initializes a User object and establishes a connection to the database.
        """
        self.conn = con.conn
        self.cursor = con.cursor
    
    def create_user(self, key, username, password):
        """
        Inserts a new user record into the USER table with the provided username and password.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.cursor.execute("INSERT INTO USER (USER_KEY, USER_NAME, PASSWORD) VALUES (?, ?, ?)", (key, username, password))
        self.conn.commit()
    
    def get_all_users(self):
        """
        Retrieves all usernames from the USER table.

        Returns:
            list: A list containing all usernames.
        """
        try:
            self.cursor.execute("SELECT USER_NAME FROM USER")
            users = self.cursor.fetchall()
            return [user[0] for user in users]
        except:
            return []
    
    def get_user(self, username):
        """
        Retrieves user information from the USER table based on the username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            tuple: A tuple containing user information if found, None otherwise.
        """
        try:
            self.cursor.execute("SELECT * FROM USER WHERE USER_NAME=?", (username,))
            return self.cursor.fetchone()
        except:
            return None
    
    def update_password(self, key, username, new_password):
        """
        Updates the password of a user in the USER table.

        Args:
            username (str): The username of the user whose password is to be updated.
            new_password (str): The new password for the user.
        """
        self.cursor.execute("UPDATE USER SET USER_KEY=?, PASSWORD=? WHERE USER_NAME=?", (key, new_password, username))
        self.conn.commit()

    def delete_user(self, username):
        """
        Deletes a user record from the USER table based on the username.

        Args:
            username (str): The username of the user to delete.
        """
        self.cursor.execute("DELETE FROM USER WHERE USER_NAME=?", (username,))
        self.conn.commit()






