from flask import Flask

def custom_validation_parser(value):
    if not value:
        raise ValueError("Must not be empty.")
    return value