-- Sentiment and ticket demand trend
SELECT date,
       ROUND(AVG(ticket_demand_index), 2) AS avg_demand,
       ROUND(AVG(social_sentiment_score), 2) AS avg_sentiment,
       ROUND(AVG(competitor_sales_estimate), 2) AS avg_competitor_sales
FROM market_trends
GROUP BY date
ORDER BY date;
