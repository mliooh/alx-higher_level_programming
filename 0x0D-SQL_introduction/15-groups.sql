-- Script that lists the number of records with the same score in second_table in MYSQL SERVER.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;