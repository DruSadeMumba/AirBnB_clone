#!/usr/bin/python3
"""Handling custom error for class_name and class_id."""


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
