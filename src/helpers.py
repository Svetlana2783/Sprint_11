import random
import string
from faker import Faker

fake = Faker()


def generate_unique_email():
    return f"test+{''.join(random.choices(string.ascii_lowercase + string.digits, k=10))}@example.com"


def generate_password():
    return fake.password()


def generate_name():
    return fake.name()
