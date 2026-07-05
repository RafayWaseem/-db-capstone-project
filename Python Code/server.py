from db import get_connection
from mysql.connector import Error

def create_procedures():

    connection, cursor = get_connection()
    if connection is None:
        return


    procedures = [
        """
        CREATE PROCEDURE GetMaxQuantity()
        BEGIN
            SELECT MAX(Quantity) AS MaxQuantity FROM Orders;
        END;
        """,

        """
        CREATE PROCEDURE ManageBooking(
            IN p_BookingID INT
        )
        BEGIN
            SELECT * FROM Bookings WHERE BookingID = p_BookingID;
        END;
        """,

        """
        CREATE PROCEDURE AddBooking(
            IN p_BookingID INT,
            IN p_BookingDate DATE,
            IN p_BookingTime TIME,
            IN p_TableNumber INT,
            IN p_NumberOfGuests INT,
            IN p_CustomerID INT,
            IN p_StaffID INT
        )
        BEGIN
            INSERT INTO Bookings (BookingID, BookingDate, BookingTime, TableNumber, NumberOfGuests, CustomerID, StaffID)
            VALUES (p_BookingID, p_BookingDate, p_BookingTime, p_TableNumber, p_NumberOfGuests, p_CustomerID, p_StaffID);
        END;
        """,

        """
        CREATE PROCEDURE UpdateBooking(
            IN p_BookingID INT,
            IN p_BookingDate DATE,
            IN p_BookingTime TIME,
            IN p_TableNumber INT,
            IN p_NumberOfGuests INT,
            IN p_CustomerID INT,
            IN p_StaffID INT
        )
        BEGIN
            UPDATE Bookings
            SET BookingDate = p_BookingDate,
                BookingTime = p_BookingTime,
                TableNumber = p_TableNumber,
                NumberOfGuests = p_NumberOfGuests,
                CustomerID = p_CustomerID,
                StaffID = p_StaffID
            WHERE BookingID = p_BookingID;
        END;
        """,

        """
        CREATE PROCEDURE CancelBooking(
            IN p_BookingID INT
        )
        BEGIN
            DELETE FROM Bookings WHERE BookingID = p_BookingID;
        END;
        """
    ]

    for proc_sql in procedures:
        try:
            cursor.execute(proc_sql)
            print(f"Successfully created procedure: {proc_sql.split()[2]}")  # get procedure name
        except Error as e:
            # If the procedure already exists
            print(f"Error creating procedure: {e}")

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    create_procedures()