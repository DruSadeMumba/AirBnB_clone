#!/usr/bin/python3
"""Handling custom error for class_name and class_id."""
import models


class ClassNameNotFoundError(Exception):
    """Handling the issue of missing class name."""

    def __init__(self, class_name):
        self.message = f"Class '{class_name}' not found."
        super().__init__(self.message)


class InstanceIdNotFoundError(Exception):
    """Handling the issue of missing instance ID."""

    def __init__(self, instance_id, class_name):
        self.message = f"'{class_name}' with '{instance_id}' is not found."
        super().__init__(self.message)


class FieldNotFoundError(Exception):
    """Handling the issue of file which if not found."""

    def __init__(self, attr_name, class_name):
        self.message = f"'{attr_name}' of '{class_name}' is not found."
        super().__init__(self.message)


class ExtraFunctions:
    @classmethod
    def all(cls):
        """retrieve all instances of a class."""
        class_instance = models.storage.find_instance(cls.__name__)
        return class_instance

    @classmethod
    def count(cls):
        """retrieve the number of instances of a class."""
        class_count = len(models.storage.find_instance(cls.__name__))
        return class_count

    @classmethod
    def show(cls, obj_id):
        """retrieve an instance based on its ID."""
        ist = models.storage.find_classname_id(cls.__name__, obj_id)
        return ist

    @classmethod
    def destroy(cls, obj_id):
        """destroy an instance based on his ID."""
        deleted_obj = models.storage.pop_classname_id(cls.__name__, obj_id)
        return deleted_obj

    @classmethod
    def update(cls, obj_id, *keys):
        """update the attributes of the class."""
        if len(keys) == 0:
            print("** attribute name missing **")
            return
        if len(keys) == 1 and type(keys[0]) is type(dict):
            keys = keys[0].items()
        else:
            keys = [keys[:2]]
        for arg in keys:
            models.storage.update_class(
                cls.__name__,
                obj_id,
                *arg
            )
