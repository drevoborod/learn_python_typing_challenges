import datetime
from datetime import date


def calculate_age(date_of_birth: date) -> int:
    pass


if __name__ == "__main__":
    assert calculate_age(date_of_birth=datetime.date(1965, 6, 2)) == 57
