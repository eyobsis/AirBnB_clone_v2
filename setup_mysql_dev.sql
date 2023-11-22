-- Create database hbnb_dev_db
CREATE DATABASE hbnb_dev_db;

-- Create user hbnb_dev with password hbnb_dev_pwd
CREATE USER hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;

-- Check if database and user already exist, and print a message if they do
IF EXISTS (SELECT 1 FROM mysql.db WHERE db = 'hbnb_dev_db') THEN
  SELECT 'Database hbnb_dev_db already exists';
ELSE
  CREATE DATABASE hbnb_dev_db;
END IF;

IF EXISTS (SELECT 1 FROM mysql.user WHERE User = 'hbnb_dev' AND Host = 'localhost') THEN
  SELECT 'User hbnb_dev already exists';
ELSE
  CREATE USER hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
END IF;
