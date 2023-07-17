#!/usr/bin/python3
"""
This is the console base for the ABnB
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """ HBNB command prompt to access models data """
    prompt = '(hbnb) '
    my_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
            }

    def do_nothing(self, arg):
        """ Does nothing """
        pass

    def do_quit(self, arg):
        """ Close program and saves the data """
        return True

    def do_EOF(self, arg):
        """ Close program and saves the data, when
        user input is CTRL + D
        """
        print("")
        return True

    def emptyline(self):
        """ Overrides the empty line """
        pass

    def do_create(self, arg):
        """ Creates new instance of basemodel class
        Structure: create [class name]
        """
        if not arg:
            print("** class name missing **")
            return
        mydata = shlex.split(arg)
        if mydata[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.my_dict[mydata[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of the instance
        based on the class name and id
        Structure: show [class name] [id]
        """
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            obj_instance = str(objs_dict[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes instance based on the class name and id
        (saves the changes into the JSON file)
        Structure: destroy [class name] [id]
        """
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        Structure: all [class name] or all
        """
        # prints the whole file
        storage.reload()
        myjson = []
        objects_dict = storage.all()
        if not arg:
            for key in objects_dict:
                myjson.append(str(objects_dict[key]))
            print(json.dumps(my_json))
            return
        token = shlex.split(arg)
        if token[0] in HBNBCommand.my_dict.keys():
            for key in objects_dict:
                if token[0] in key:
                    myjson.append(str(objects_dict[key]))
            print(json.dumps(myjson))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Structure: update [class name] [id] [arg_name] [arg_value]
        """
        if not arg:
            print("** class name missing **")
            return
        mydata = shlex.split(arg)
        storage.reload()
        objs_dict = storage.all()
        if mydata[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(mydata) == 1):
            print("** instance id missing **")
            return
        try:
            key = mydata[0] + "." + mydata[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(mydata) == 2):
            print("** attribute name missing **")
            return
        if (len(mydata) == 3):
            print("** value missing **")
            return
        my_instance = objs_dict[key]
        if hasattr(my_instance, mydata[2]):
            data_type = type(getattr(my_instance, mydata[2]))
            setattr(my_instance, mydata[2], data_type(mydata[3]))
        else:
            setattr(my_instance, mydata[2], mydata[3])
        storage.save()

    def do_update2(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Structure: update [class name] [id] [dictionary]
        """
        if not arg:
            print("** class name missing **")
            return
        my_dictionary = "{" + arg.split("{")[1]
        mydata = shlex.split(arg)
        storage.reload()
        objs_dict = storage.all()
        if mydata[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(mydata) == 1):
            print("** instance id missing **")
            return
        try:
            key = mydata[0] + "." + mydata[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (my_dictionary == "{"):
            print("** attribute name missing **")
            return

        my_dictionary = my_dictionary.replace("\'", "\"")
        my_dictionary = json.loads(my_dictionary)
        my_instance = objs_dict[key]
        for mi_key in my_dictionary:
            if hasattr(my_instance, mi_key):
                data_type = type(getattr(my_instance, mi_key))
                setattr(my_instance, mi_key, my_dictionary[mi_key])
            else:
                setattr(my_instance, mi_key, my_dictionary[mi_key])
        storage.save()

    def do_count(self, arg):
        """
        Counts number of instances of a class
        """
        counter = 0
        objects_dict = storage.all()
        for key in objects_dict:
            if (arg in key):
                counter += 1
        print(counter)

    def default(self, arg):
        """ handle new ways of inputing data """
        val_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        arg = arg.strip()
        values = arg.split(".")
        if len(values) != 2:
            cmd.Cmd.default(self, arg)
            return
        class_name = values[0]
        command = values[1].split("(")[0]
        line = ""
        if (command == "update" and values[1].split("(")[1][-2] == "}"):
            inputs = values[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = values[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if (command in val_dict.keys()):
            val_dict[command](line.strip())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
