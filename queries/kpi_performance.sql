-- Match performance metrics
SELECT match_date,
       home_team,
       away_team,
       home_score,
       away_score,
       attendance,
       CASE 
           WHEN home_score > away_score THEN home_team
           WHEN home_score < away_score THEN away_team
           ELSE 'Draw'
       END AS winner
FROM matches;

-- Win/Loss count per team
SELECT team, 
       SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END) AS wins,
       SUM(CASE WHEN result = 'Loss' THEN 1 ELSE 0 END) AS losses
FROM (
    SELECT home_team AS team,
           CASE 
               WHEN home_score > away_score THEN 'Win'
               WHEN home_score < away_score THEN 'Loss'
               ELSE 'Draw'
           END AS result
    FROM matches
    UNION ALL
    SELECT away_team AS team,
           CASE 
               WHEN away_score > home_score THEN 'Win'
               WHEN away_score < home_score THEN 'Loss'
               ELSE 'Draw'
           END AS result
    FROM matches
)
GROUP BY team
ORDER BY wins DESC;
