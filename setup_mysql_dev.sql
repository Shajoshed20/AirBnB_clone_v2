-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user 'hbnb_dev' if it doesn't exist
CREATE USER IF
	NOT EXISTS 'hbnb_dev'@'localhost'
	IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant Priviledges to the user 'hbnb_dev'
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.*
	TO 'hbnb_dev'@'localhost'
	IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT
	ON `performance_schema`.*
	TO 'hbnb_dev'@'localhost'
	IDENTIFIED BY 'hbnb_dev_pwd';

-- Reload priviledges to apply the changes
FLUSH PRIVILEGES;
