-- script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.cities, hbtn_0d_usa.states ORDER BY cities.id ASC;
