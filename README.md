#Welcome to the AirBnB clone project!

# AirBnB Clone Command Interpreter

This project creates a command line interface (CLI) to manage objects for the AirBnB rental property platform. 
It implements object relational mapping (ORM) functionality through a basic command interpreter.

## Overview

The CLI allows users to:

- Create, update, retrieve and delete objects representing core AirBnB listings and users
- Persist objects to a file-based storage engine for durability
- Retrieve and display objects through a simple interactive session
- Support input/output via pipes for non-interactive usage

Object classes follow inheritance through the BaseModel parent class to centralize common functionality like serialization/deserialization.

Unit tests validate core functionality and ensure changes don't break existing features. The code adheres to PEP 8 style guidelines for readability and consistency.

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/AirBnB_clone.git
``` 

2. Navigate to the project directory:

```
cd AirBnB_clone
```

3. Install dependencies (optional if running directly): 

```
pip install -r requirements.txt
```

## Usage

Run the command interpreter in interactive mode:

```
./console.py
```

Or pipe commands in non-interactive mode:

```
echo "help" | ./console.py 
```

## Commands

See the `help` command for full usage details of all available CRUD commands.

## Classes

The core object classes are:

- `BaseModel` 
- `User`
- `State`  
- `City`
- `Place`
- `Amenity`
- `Review`

## Testing

Run all tests:

```
python3 -m unittest discover tests
``` 

Or individual test files like `test_base_model.py`.

## Future Improvements

Some ideas for future enhancements:

- Add SQL database storage with SQLAlchemy 
- Implement CRUD API endpoints with Flask
- Add front-end interface with JavaScript
- Add additional object types like reservations
- Add validation, permissions, relationships

## Contributing

Pull requests are welcome! Please open an issue first to discuss any changes.

## Licensing
Authors

- Yohanes Senbeto
[https://github.com/YohanesSenbeto](https: // github.com/YohanesSenbeto)

- Eyob Sisay
[https://github.com/eyobsis](https: // github.com/eyobsis)
