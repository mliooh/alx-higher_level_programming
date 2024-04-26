#!/usr/bin/python3
""" Module contains the base of all other classes
in the project.
"""
import json
import csv
import os.path


class Base:
    """ Base class. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a JSON string representation of
        list_dictionaries. """
        res = "[]"
        if list_dictionaries is None:
            return res
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation to
        list_objs to a file. """
        filename = f'{cls.__name__}.json'
        res = []
        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                res.append(list_objs[i].to_dictionary())

        text = cls.to_json_string(res)

        with open(filename, 'w', encoding='UTF-8') as f:
            return f.write(text)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string
        representation json_string. """
        res = []

        if not json_string:
            return res
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method that returns an instance with all
        attributes already set. """
        if cls.__name__ == "Rectangle":
            dummy = cls(12, 12)
        else:
            dummy = cls(12)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method that returns a list of instances. """
        filename = f'{cls.__name__}.json'
        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r', encoding='UTF-8') as f:
            list_text = f.read()

        cls_list = cls.from_json_string(list_text)
        inst_list = []

        for index in range(len(cls_list)):
            inst_list.append(cls.create(**cls_list[index]))

        return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = f"{cls.__name__}.csv"

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = f"{cls.__name__}.csv"

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
