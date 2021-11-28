import logging

logger = logging.getLogger("testLogger")


class Student:
    def __init__(self, name: str, age: int, university: str):
        logger.info("Generating new student with name %s, age %s, university %s...", name, age, university)
        self.name = name
        self.age = age
        self.university = university

    def set_age(self, age: int):
        logger.debug("Updating student age from %s to %s...", self.age, age)
        self.age = age

    def set_name(self, name: str):
        logger.debug("Updating student name from %s to %s...", self.name, name)
        self.name = name

    def set_university(self, university: str):
        logger.debug("Updating student university from %s to %s...", self.university, university)
        self.university = university
