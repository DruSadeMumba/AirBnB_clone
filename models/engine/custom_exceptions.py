#!/usr/bin/python3
"""Handling custom error for class_name and class_id."""


class ClassNameNotFoundError(Exception):
    """Handling the issue of missing class name."""

    def __init__(self, class_name):
        self.message = f"Class '{class_name}' not found."
        super().__init__(self.message)


class InstanceIdNotFoundError(Exception):
    """Handling the issue of missing instance ID."""

    def __init__(self, instance_id):
        self.message = f"Instance ID '{instance_id}' not found."
        super().__init__(self.message)
