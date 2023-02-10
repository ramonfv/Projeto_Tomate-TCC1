from setuptools import setup, find_packages

# with open("config/requirements.txt") as requirement_file:
#     requirements = requirement_file.read().split()
    

setup(
    name="modules",
    version="1.0.0",
    packages=find_packages(), # package = any folder with an __init__.py file
)