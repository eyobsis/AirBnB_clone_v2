#Welcome to the AirBnB clone - MySQL!

This repository contains the initial stage of a student project to build a clone of the AirBnB website. The project includes a backend interface, or console, to manage program data. The console allows the user to create, update, and destroy objects, as well as manage file storage. The storage is persistent between sessions using JSON serialization/deserialization. 
 
To use the project, you can clone the repository and run the "console.py" file. This will start the HBnB console, where you can enter various commands to interact with the models and manipulate the data. 
 
The supported commands include: 
- help [command]: Prints helpful information about a command. 
- quit: Closes the command interpreter. 
- EOF: Closes the command interpreter. 
- create Model [prop_key=prop_value]...: Creates a new instance of the Model class with the given properties. 
- count Model: Prints the number of instances of the Model class. 
- show Model id: Prints the string representation of an instance of the Model class with the given id. 
- destroy Model id: Deletes an instance of the Model class with the given id. 
- all [Model]: Prints a list containing the string representation of all instances of the Model class. 
- update Model id attr_name attr_value: Updates an instance of the Model class with the given id by assigning the attribute value attr_value to its attribute named attr_name. 
- update Model id dict_repr: Updates an instance of the Model class with the given id by storing the key, value pairs in the given dictionary as its attributes. 
 
The supported models include BaseModel, User, State, City, Amenity, Place, and Review. 
 
There are also some environment variables that can be set to configure the project, such as HBNB_ENV, HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB, and HBNB_TYPE_STORAGE. 
 
The examples provided show the syntax and usage of the commands in the console for creating, showing, destroying, and updating objects. 
 
Before pushing any commits, it is recommended to run the script ./test.bash to ensure that no tests are failing and the code complies with the project's styling standard.

## Contributing

Pull requests are welcome! Please open an issue first to discuss any changes.

## Licensing
Authors

- Yohanes Senbeto
[https://github.com/YohanesSenbeto](https: // github.com/YohanesSenbeto)

- Eyob Sisay
[https://github.com/eyobsis](https: // github.com/eyobsis)
