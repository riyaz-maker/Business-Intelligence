-- Average session duration by month
SELECT strftime('%Y-%m', session_date) AS month,
       ROUND(AVG(duration_minutes), 2) AS avg_duration
FROM sessions
GROUP BY month
ORDER BY month;

-- Daily active users
SELECT session_date, COUNT(DISTINCT user_id) AS active_users
FROM sessions
GROUP BY session_date
ORDER BY session_date;
