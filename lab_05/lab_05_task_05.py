# TODO написать функцию генерации случайных паролей
import random
import string  # Pycharm ругается, если написать "import random, string"


def get_random_password(sym_, len_pass=8) -> str:
    password = random.sample(sym_, len_pass)
    return "".join(password)


symbols = string.ascii_letters + string.digits  # надеюсь использование ascii_letters не принципиально
print(get_random_password(symbols))
