-- script that creates the table unique_id on the MySQL server
CREATE TABLE IF NOT EXITS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
