-- Creates a table unique_id on MYSQL server
CREATE Table IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
