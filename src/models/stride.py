class Stride:
    """
    Class to manage operations related to patient steps in the database.
    Inherits from the BBDD class to leverage connection and cursor.
    
    Attributes:
        Inherits all attributes from the BBDD class.

    Methods:
        create_stride: Insert a new step record into the database.
        get_stride_by_id: Retrieve a step record by its ID.
        get_stride_by_date_and_patient: Retrieve a step record by date and patient ID.
        get_strides_by_patient: Retrieve all step records for a patient.
        update_stride_document: Update the document of a step by date and patient ID.
        delete_stride: Delete a step record by date and patient ID.
    """

    def __init__(self, con) -> None:
        """
        Initialize the Stride instance and establish connection with the database.
        """
        self.conn = con.conn
        self.cursor = con.cursor

    def create_stride(self, id, date, document, description, patient_id):
        """
        Insert a new step record into the database.

        Args:
            id (str): Step ID.
            date (str): Step date.
            document (str): Document associated with the step.
            description (str): Step description.
            patient_id (int): ID of the patient associated with the step.
        """
        self.cursor.execute('''INSERT INTO STRIDE (STRIDE_ID, STRIDE_DATE, STRIDE_DOCUMENT, STRIDE_DESCRIPTION, STRIDE_PATIENT_ID) 
                                                    VALUES (?, ?, ?, ?, ?)''',
                            (id, date, document, description, patient_id))
        self.conn.commit()

    def get_stride_by_id(self, id):
        """
        Retrieve a step record by its ID.

        Args:
            id (str): Step ID.

        Returns:
            tuple or None: Step record if found, None if not found.
        """
        self.cursor.execute("SELECT * FROM STRIDE WHERE STRIDE_ID=?", (id,))
        stride = self.cursor.fetchone()
        if stride:
            return stride
        else:
            print("No stride found with the specified ID.")

    def get_stride_by_date_and_patient(self, date, patient_id):
        """
        Retrieve a step record by date and patient ID.

        Args:
            date (str): Step date.
            patient_id (int): ID of the patient associated with the step.

        Returns:
            tuple or None: Step record if found, None if not found.
        """
        self.cursor.execute("SELECT * FROM STRIDE WHERE STRIDE_DATE=? AND STRIDE_PATIENT_ID=?", (date, patient_id))
        stride = self.cursor.fetchone()
        if stride:
            return stride
        else:
            print("No stride found with the specified Date or patient ID.")

    def get_strides_by_patient(self, patient_id):
        """
        Retrieve all step records for a patient.

        Args:
            patient_id (int): ID of the patient.

        Returns:
            list: List of step records for the patient.
        """
        self.cursor.execute("SELECT * FROM STRIDE WHERE STRIDE_PATIENT_ID=?", (patient_id,))
        strides = self.cursor.fetchall()
        if strides:
            return strides
        else:
            print("No strides found with the specified patient ID.")

    def update_stride_document(self, date, document, patient_id):
        """
        Update the document of a step by date and patient ID.

        Args:
            date (str): Step date.
            document (str): New document associated with the step.
            patient_id (int): ID of the patient associated with the step.
        """
        self.cursor.execute("UPDATE STRIDE SET STRIDE_DOCUMENT=? WHERE STRIDE_DATE=? AND STRIDE_PATIENT_ID=?",
                            (document, date, patient_id))
        self.conn.commit()

    def delete_stride(self, patient_id, date):
        """
        Delete a step record by date and patient ID.

        Args:
            patient_id (int): ID of the patient.
            date (str): Step date.
        """
        stride_current = self.get_stride_by_date_and_patient(date, patient_id)
        if stride_current:
            self.cursor.execute("DELETE FROM STRIDE WHERE STRIDE_DATE=? AND STRIDE_PATIENT_ID=?", (date, patient_id))
            self.conn.commit()
            print("Stride deleted successfully.")
        else:
            print("Unable to delete stride. No stride found with the specified ID.")

    def __del__(self):
        """
        Close the connection to the database upon destroying the Stride instance.
        """
        self.conn.close()