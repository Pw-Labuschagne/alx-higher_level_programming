-- Creates a database htbn_0d_use and table states in MYSQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE NOT NULL SERIAL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);
