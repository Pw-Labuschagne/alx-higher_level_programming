-- Creates a database htbn_0d_use and table states in MYSQL server
CREATE DATABSE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT SERIAL UNIQUE NOT NULL PRIMARY KEY,
	name VARCHAR(256)
	);
