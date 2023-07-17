# AirBnB Clone
![HBnB Logo](./image/hbnb_logo.png)


### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Further Information](#Furtherinformation)
- [Requirements](#Requirements)
- [Repo Contents](#FileContents)
- [Installation](#Installation)
- [Usage](#Usage)
- [Built with](#Built-with)
- [Acknowledgements](#Acknowledgements)

## Background Context :page_facing_up:
### Welcome to the AirBnB clone project!
This is the first towards building our first web app; the `AirBnB clone`. In this first phase a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.


## Environment :computer:
The console was developed in Ubuntu 20.04.6LTS using python3 (version 3.8.10).

## Requirements :memo:
Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 20.04.6, python3 and pep8 style corrector.

## Repo Contents :clipboard:
This repository constains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[review.py](./models/review.py) | Defines subclass Review |
|[state.py](./models/state.py) | Defines subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |


## Installation :hammer_and_wrench:
Clone the repository and run the console.py
```
$ git clone https://github.com/IdiJr/AirBnB_clone.git
```

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program |

###### Example No.1

```
~/AirBnB_clone# ./console.py
(hbnb) create User
d7057ba2-460b-48ad-86fc-22da1f6241ec
(hbnb) create User
a93a4748-8323-4666-bdb8-addbf00ba798
(hbnb) show User d7057ba2-460b-48ad-86fc-22da1f6241ec
[User] (d7057ba2-460b-48ad-86fc-22da1f6241ec) {'id': 'd7057ba2-460b-48ad-86fc-22da1f6241ec', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 42, 632337), 'updated_at': datetime.datetime(2023, 7, 17, 12, 46, 42, 633194)}
(hbnb) all User
["[User] (a93a4748-8323-4666-bdb8-addbf00ba798) {'id': 'a93a4748-8323-4666-bdb8-addbf00ba798', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 12, 423989), 'updated_at': datetime.datetime(2023, 7, 17, 12, 46, 12, 430335)}", "[User] (d7057ba2-460b-48ad-86fc-22da1f6241ec) {'id': 'd7057ba2-460b-48ad-86fc-22da1f6241ec', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 42, 632337), 'updated_at': datetime.datetime(2023, 7, 17, 12, 46, 42, 633194)}"]
(hbnb) update User a93a4748-8323-4666-bdb8-addbf00ba798 name Alx
(hbnb) all User
["[User] (a93a4748-8323-4666-bdb8-addbf00ba798) {'id': 'a93a4748-8323-4666-bdb8-addbf00ba798', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 12, 423989), 'updated_at': datetime.datetime(2023, 7, 17, 12, 48, 51, 976315), 'name': 'Alx'}", "[User] (d7057ba2-460b-48ad-86fc-22da1f6241ec) {'id': 'd7057ba2-460b-48ad-86fc-22da1f6241ec', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 42, 632337), 'updated_at': datetime.datetime(2023, 7, 17, 12, 46, 42, 633194)}"]
(hbnb) update User d7057ba2-460b-48ad-86fc-22da1f6241ec name Holberton
(hbnb) all User
["[User] (a93a4748-8323-4666-bdb8-addbf00ba798) {'id': 'a93a4748-8323-4666-bdb8-addbf00ba798', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 12, 423989), 'updated_at': datetime.datetime(2023, 7, 17, 12, 48, 51, 976315), 'name': 'Alx'}", "[User] (d7057ba2-460b-48ad-86fc-22da1f6241ec) {'id': 'd7057ba2-460b-48ad-86fc-22da1f6241ec', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 42, 632337), 'updated_at': datetime.datetime(2023, 7, 17, 12, 49, 52, 51724), 'name': 'Holberton'}"]
(hbnb) quit
```

###### Example No.2

```
~/AirBnB_clone# ./console.py
(hbnb) User.create()
94d1ada0-5d43-46e4-920d-9d6a6166d385
(hbnb) User.all()
["[User] (a93a4748-8323-4666-bdb8-addbf00ba798) {'id': 'a93a4748-8323-4666-bdb8-addbf00ba798', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 12, 423989), 'updated_at': datetime.datetime(2023, 7, 17, 12, 48, 51, 976315), 'name': 'Alx'}", "[User] (d7057ba2-460b-48ad-86fc-22da1f6241ec) {'id': 'd7057ba2-460b-48ad-86fc-22da1f6241ec', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 42, 632337), 'updated_at': datetime.datetime(2023, 7, 17, 12, 49, 52, 51724), 'name': 'Holberton'}", "[User] (ab7ed30b-23db-4596-af31-d19918ef9106) {'id': 'ab7ed30b-23db-4596-af31-d19918ef9106', 'created_at': datetime.datetime(2023, 7, 17, 12, 58, 11, 223314), 'updated_at': datetime.datetime(2023, 7, 17, 12, 58, 11, 224459)}", "[User] (94d1ada0-5d43-46e4-920d-9d6a6166d385) {'id': '94d1ada0-5d43-46e4-920d-9d6a6166d385', 'created_at': datetime.datetime(2023, 7, 17, 12, 59, 35, 167660), 'updated_at': datetime.datetime(2023, 7, 17, 12, 59, 35, 168560)}"]
(hbnb) User.show(a93a4748-8323-4666-bdb8-addbf00ba798)
[User] (a93a4748-8323-4666-bdb8-addbf00ba798) {'id': 'a93a4748-8323-4666-bdb8-addbf00ba798', 'created_at': datetime.datetime(2023, 7, 17, 12, 46, 12, 423989), 'updated_at': datetime.datetime(2023, 7, 17, 12, 48, 51, 976315), 'name': 'Alx'}
(hbnb) User.destroy(a93a4748-8323-4666-bdb8-addbf00ba798)
(hbnb) User.destroy(d7057ba2-460b-48ad-86fc-22da1f6241ec)
(hbnb) User.destroy(94d1ada0-5d43-46e4-920d-9d6a6166d385)
(hbnb) User.destroy(ab7ed30b-23db-4596-af31-d19918ef9106)
(hbnb) User.all()
[]
(hbnb) quit
```

## Built with :gear:
python3 (3.8.10)

### Version :pushpin:


### Acknowledgements :raised_hands:
To all the peers that contribuited with their knowledge

### Authors :fountain_pen:
* [Ali Baba Idi](https://github.com/IdiJr)
* [Emmanuel Addo](https://github.com/emmanueladdo)
