class Patient:
    """
    This class represents a Patient object and extends the BBDD class to interact with the database.

    Attributes:
        Inherits all attributes from the BBDD class.
        
    Methods:
        create_patient: Inserts a new patient record into the PATIENT table.
        get_patient_by_id: Retrieves patient information from the PATIENT table based on the patient's ID.
        update_patient: Updates patient information in the PATIENT table based on the patient's ID.
        delete_patient: Deletes a patient record from the PATIENT table based on the patient's ID.
    """

    def __init__(self, con):
        """
        Initializes a Patient object by establishing a connection to the database.
        """
        self.conn = con.conn
        self.cursor = con.cursor

    def create_patient(self, id, name, lastname, bird_date, gender, phone, mail, address):
        """
        Inserts a new patient record into the PATIENT table.

        Args:
            id (int): The patient's ID.
            name (str): The patient's name.
            lastname (str): The patient's last name.
            birth_date (str): The patient's birth date (formatted as 'DD-MM-YYYY').
            gender (str): The patient's gender.
            phone (str): The patient's phone number.
            mail (str): The patient's email address.
            address (str): The patient's home address.
        """
        self.cursor.execute('''INSERT INTO PATIENT (PATIENT_ID, PATIENT_NAME, PATIENT_LASTNAME, PATIENT_DATE, PATIENT_GENDER,
                                                    PATIENT_PHONE, PATIENT_MAIL, PATIENT_ADDRESS) 
                                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                            (id, name, lastname, bird_date, gender, phone, mail, address))
        self.conn.commit()
        
    def get_patient_by_id(self, id):
        """
        Retrieves patient information from the PATIENT table based on the patient's ID.

        Args:
            id (int): The ID of the patient to retrieve.

        Returns:
            tuple: A tuple containing patient information if found, None otherwise.
        """
        self.cursor.execute("SELECT * FROM PATIENT WHERE PATIENT_ID=?", (id,))
        patient = self.cursor.fetchone()
        if patient:
            return patient
        else:
            return False

    def update_patient(self, id, **kwargs):
        """
        Updates patient information in the PATIENT table based on the patient's ID.

        Args:
            id (int): The ID of the patient to update.
            name (str): (Optional) The updated patient's name.
            lastname (str): (Optional) The updated patient's last name.
            bird_date (str): (Optional) The updated patient's birth date (formatted as 'YYYY-MM-DD').
            gender (str): (Optional) The updated patient's gender.
            phone (str): (Optional) The updated patient's phone number.
            mail (str): (Optional) The updated patient's email address.
            address (str): (Optional) The updated patient's home address.
        """
        patient_current = self.get_patient_by_id(id)
        if patient_current:
            fields_to_update = []
            for key, value in kwargs.items():
                if value:
                    fields_to_update.append((key, value))
            update_query = "UPDATE PATIENT SET " + ", ".join([f"{field} = ?" for field, _ in fields_to_update]) + " WHERE PATIENT_ID = ?"
            update_values = [value for _, value in fields_to_update]
            update_values.append(id)
            try:
                self.cursor.execute(update_query, tuple(update_values))
                self.conn.commit()
                return 's'
            except:
                return 'e1'
        else:
            return 'e2'

    def delete_patient(self, id):
        """
        Deletes a patient record from the PATIENT table based on the patient's ID.

        Args:
            id (int): The ID of the patient to delete.
        """
        patient_current = self.get_patient_by_id(id)
        if patient_current:
            try:
                self.cursor.execute("DELETE FROM PATIENT WHERE PATIENT_ID=?", (id,))
                self.conn.commit()
                return 's'
            except:
                return 'e1'
        else:
            return 'e2'
    
    def get_all_patient (self):
        try:
            self.cursor.execute("SELECT PATIENT_ID, PATIENT_NAME, PATIENT_LASTNAME, PATIENT_DATE, PATIENT_GENDER FROM PATIENT")
            return self.cursor.fetchall()
        except:
            return None

    def __del__(self):
        """
        Closes the database connection when the object is destroyed.
        """
        self.conn.close()