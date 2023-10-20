-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
USE hbtn_0d_usa;
SET @california_id = (SELECT id FROM states WHERE name = 'California');

SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = @california_id
ORDER BY cities.id ASC;
