import sqlite3
from sqlite3 import Error
import models.encrypt as nc
from paths import DB_PATH

class BBDD:
    """
    This class provides methods to interact with a SQLite database
    containing tables to manage patients and their appointment data.

    Attributes:
        conn (sqlite3.Connection): Connection to the SQLite database.
        cursor (sqlite3.Cursor): Cursor to execute SQL queries.
    """
    
    def __init__(self) -> None:      
        """
        Initializes the connection to the database.
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect(DB_PATH)
            self.cursor = self.conn.cursor()
        except Error as e:
            print(e)
        
    def conection (self):
        """
        Method to create the PATIENT and STRIDE tables in the database if they don't exist.

        Returns:
            bool: True if the tables were created successfully, False otherwise.
        """
        
        try:
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS USER (
                                    USER_KEY text PRIMARY KEY,
                                    USER_NAME text NOT NULL UNIQUE,
                                    PASSWORD text NOT NULL
                                )
                                ''')
            
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS PATIENT (
                                    PATIENT_ID INTEGER  PRIMARY KEY,
                                    PATIENT_NAME TEXT NOT NULL,
                                    PATIENT_LASTNAME TEXT NOT NULL,
                                    PATIENT_DATE TEXT,
                                    PATIENT_GENDER TEXT,
                                    PATIENT_PHONE TEXT,
                                    PATIENT_MAIL TEXT,
                                    PATIENT_RSIZE REAL DEFAULT 0.0,
                                    PATIENT_LSIZE REAL DEFAULT 0.0
                                )
                                ''')
            
            self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS STRIDE (
                                    STRIDE_ID INTEGER  PRIMARY KEY,
                                    STRIDE_DATE TEXT,
                                    STRIDE_DOCUMENT TEXT,
                                    STRIDE_DESCRIPTION TEXT,
                                    STRIDE_PATIENT_ID INTEGER ,
                                    FOREIGN KEY (STRIDE_PATIENT_ID) REFERENCES PATIENT(PATIENT_ID)
                                )
                                ''')
        except Error as e:
            print(e)
        try:
            key, encrypt_password = nc.encrypt('user')
            self.cursor.execute("INSERT INTO USER (USER_KEY, USER_NAME, PASSWORD) VALUES (?, ?, ?)", (str(key),'user', str(encrypt_password)))
            self.conn.commit()
        except:
            pass
    
    def close_conection(self):
        """
        Closes the database connection when the object is destroyed.
        """
        self.conn.close()