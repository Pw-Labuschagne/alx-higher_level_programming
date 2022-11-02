-- Lists all cities in database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states ON cities.state.id ORDER BY cities.id;

