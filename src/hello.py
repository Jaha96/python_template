""" Hello World module"""
import os
from dotenv import load_dotenv
from contextlib import suppress

with suppress(Exception):
    load_dotenv(override=True)

print("My custom env arg from .env file: ", os.getenv("CUSTOM_ARG"))
print("Hello World!")
