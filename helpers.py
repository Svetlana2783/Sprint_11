import random
import string
from faker import Faker

def generate_unique_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"test+{random_string}@example.com"

def generate_password():
    fake = Faker()
    return fake.password()

def generate_name():
    fake = Faker()
    return fake.name()
