-- Creates database and table cities in MYSQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE IF TABLE NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE SERIAL NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES (id)
	);
