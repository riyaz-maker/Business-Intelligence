-- Monthly revenue breakdown
SELECT strftime('%Y-%m', revenue_date) AS month,
       SUM(price) AS gross_revenue,
       SUM(tax) AS total_tax,
       SUM(total) AS net_revenue
FROM revenue
GROUP BY month
ORDER BY month;

-- Revenue per user
SELECT user_id, ROUND(SUM(total), 2) AS user_total_revenue
FROM revenue
GROUP BY user_id
ORDER BY user_total_revenue DESC;
