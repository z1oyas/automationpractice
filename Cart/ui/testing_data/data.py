import random
import string

def generate_random(l=5):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for _ in range(l))
    return random_string


DATA_EMAIL = generate_random()+"@gmail.com"
DATA_PASSWORD = generate_random()
DATA_FIO = generate_random(10)
