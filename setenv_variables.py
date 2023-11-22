#!/usr/bin/python3

# Set the environment variables
import os

HBNB_ENV = "dev"
HBNB_MYSQL_USER = "hbnb_dev"
HBNB_MYSQL_PWD = "hbnb_dev_pwd"
HBNB_MYSQL_HOST = "hbnb_dev_pwd"
HBNB_MYSQL_DB = "hbnb_dev_db"
HBNB_TYPE_STORAGE = "db"

# Set the environment variables
os.environ["HBNB_ENV"] = HBNB_ENV
os.environ["HBNB_MYSQL_USER"] = HBNB_MYSQL_USER
os.environ["HBNB_MYSQL_PWD"] = HBNB_MYSQL_PWD
os.environ["HBNB_MYSQL_HOST"] = HBNB_MYSQL_HOST
os.environ["HBNB_MYSQL_DB"] = HBNB_MYSQL_DB
os.environ["HBNB_TYPE_STORAGE"] = HBNB_TYPE_STORAGE

# Print the environment variables
print("HBNB_ENV:", os.environ["HBNB_ENV"])
print("HBNB_MYSQL_USER:", os.environ["HBNB_MYSQL_USER"])
print("HBNB_MYSQL_PWD:", os.environ["HBNB_MYSQL_PWD"])
print("HBNB_MYSQL_HOST:", os.environ["HBNB_MYSQL_HOST"])
print("HBNB_MYSQL_DB:", os.environ["HBNB_MYSQL_DB"])
print("HBNB_TYPE_STORAGE:", os.environ["HBNB_TYPE_STORAGE"])

