USE LittleLemonDM;

-- -----------------------------------------------------------------
-- 1. GetMaxQuantity – returns the highest quantity from Orders
-- -----------------------------------------------------------------
CALL GetMaxQuantity();

-- -----------------------------------------------------------------
-- 2. ManageBooking – retrieve booking details for a given ID
--    (example: BookingID = 1)
-- -----------------------------------------------------------------
CALL ManageBooking(1);

-- -----------------------------------------------------------------
-- 3. AddBooking – insert a new booking (choose an unused BookingID)
--    (Here we use 31, adjust if 31 already exists)
-- -----------------------------------------------------------------
CALL AddBooking(31, '2026-06-16', '19:00:00', 10, 2, 1, 3);

-- Verify the insertion
SELECT * FROM Bookings WHERE BookingID = 31;

-- -----------------------------------------------------------------
-- 4. UpdateBooking – update the booking we just added
-- -----------------------------------------------------------------
CALL UpdateBooking(31, '2026-06-17', '20:30:00', 12, 4, 2, 4);

-- Check the update
SELECT * FROM Bookings WHERE BookingID = 31;

-- -----------------------------------------------------------------
-- 5. CancelBooking – delete the booking (clean up)
-- -----------------------------------------------------------------
CALL CancelBooking(31);

-- Confirm deletion
SELECT * FROM Bookings WHERE BookingID = 31;