-- Script that lists all records of the second_table in MYSQL SERVER.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;