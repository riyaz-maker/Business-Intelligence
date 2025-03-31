-- Daily ticket sales
SELECT event_date, COUNT(*) AS tickets_sold
FROM bookings
GROUP BY event_date
ORDER BY event_date;

-- Monthly ticket sales
SELECT strftime('%Y-%m', event_date) AS month, COUNT(*) AS tickets_sold
FROM bookings
GROUP BY month
ORDER BY month;

-- Ticket type distribution
SELECT ticket_type, COUNT(*) AS total_bookings, ROUND(AVG(price), 2) AS avg_price
FROM bookings
GROUP BY ticket_type;
