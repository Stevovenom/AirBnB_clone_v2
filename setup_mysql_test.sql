-- Create database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_dev_db database to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges on the performance_schema database to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Application
FLUSH PRIVILEGES;
