# HBNB - The Console
# This repository encompasses a comprehensive student project aimed at emulating the functionality of the AirBnB website.
# The initial stages focus on constructing a backend console, facilitating object management, and persistent storage using JSON serialization/deserialization.

# Project Tasks Overview
# Tasks	Files	Description
# 0: Authors/README File	AUTHORS	Project authors
# 1: Pep8	N/A	All code is pep8 compliant
# 2: Unit Testing	/tests	All class-defining modules are unittested
# 3. Make BaseModel	/models/base_model.py	Defines a parent class to be inherited by all model classes
# 4. Update BaseModel w/ kwargs	/models/base_model.py	Add functionality to recreate an instance of a class from a dictionary representation
# 5. Create FileStorage class	/models/engine/file_storage.py /models/__init__.py /models/base_model.py	Defines a class to manage persistent file storage system
# 6. Console 0.0.1	console.py	Add basic functionality to console program, allowing it to quit, handle empty lines and ^D
# 7. Console 0.1	console.py	Update the console with methods allowing the user to create, destroy, show, and update stored data
# 8. Create User class	console.py /models/engine/file_storage.py /models/user.py	Dynamically implements a user class
# 9. More Classes	/models/user.py /models/place.py /models/city.py /models/amenity.py /models/state.py /models/review.py	Dynamically implements more classes
# 10. Console 1.0	console.py /models/engine/file_storage.py	Update the console and file storage system to work dynamically with all classes update file storage

# Project Evolution & Features
# Pep8 Compliance: All code adheres to Pep8 standards for consistency and readability.
# Unit Testing: Ensures class-defining modules are thoroughly unit-tested, maintaining code integrity.
# BaseModel Definition: Establishes a parent class inherited by all subsequent model classes.
# FileStorage Class: Implements a robust file storage system managing persistent data storage.
# Console Development: Gradual enhancement of console features enabling object manipulation and storage management.
# Dynamic Class Implementation: Allows dynamic creation and management of various classes within the console.
# Enhanced Console & Storage (1.0): Updates console and storage systems to dynamically handle all classes.

# General Use
# Clone Repository: Begin by cloning this repository.
# Run the Console:
# shell
# Copy code
# /AirBnB_clone$ ./console.py
# Console Prompt:
# Upon running the command, the console prompt (hbnb) signifies access to the "HBnB" console. Various commands are available within the program.

# Commands Available
# create: Create an instance based on a given class.
# destroy: Delete an object based on class and UUID.
# show: Display an object based on class and UUID.
# all: Show all available objects or those of a specific class.
# update: Modify attributes of an object based on class and UUID.
# quit: Exit the console program (EOF also terminates).

# Alternative Syntax
# Users can issue commands using an alternative syntax, such as <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]]), offering advanced functionality for commands like all, count, show, destroy, and update.

# Usage Examples
# Primary Command Syntax
# Create an Object
# lua
# Copy code
# (hbnb) create BaseModel
# (hbnb) create BaseModel
# 3aa5babc-efb6-4041-bfe9-3cc9727588f8
# Show an Object
# scss
# Copy code
# (hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
# [BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
# <!-- Include examples for destroy, update, etc., for better demonstration -->

# Alternative Syntax
# Show all User Objects
# scss
# Copy code
# (hbnb) User.all()
# ["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
# <!-- Include examples for count, destroy, update, etc., for better demonstration -->

# Alternative Syntax (Cont.)
# Destroy a User
# scss
# Copy code
# (hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
# (hbnb) User.all()
# ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
# Update User (by attribute)
# scss
# Copy code
# (hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
# (hbnb) User.all()
# ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
# Update User (by dictionary)
# python
# Copy code
# (hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
# (hbnb) User.all()
# ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
# These command examples showcase the versatility and capabilities of the console, allowing users to perform a variety of operations on different classes of objects within the system.

# Installation & Execution
# To execute the project locally, follow these steps:
# Clone the Repository:
# bash
# Copy code
# git clone https://github.com/justinmajetich/AirBnB_clone.git
# Navigate to the Project Directory:
# Copy code
# cd AirBnB_clone
# Run the Console:
# Copy code
# ./console.py

# Additional Notes
# For more detailed instructions and examples, refer to the console documentation.
# Feel free to explore further commands and functionalities within the
Feel free to explore further commands and functionalities within the console for a better understanding of its capabilities.
This README aims to provide comprehensive guidance for understanding, installing, and utilizing the project's console interface. Should you have any queries or require further assistance, refer to the provided documentation or the project repository.
