
from datetime import date

class User:
    def __init__ (self, date_of_birth: date):
        self._date_of_birth = date_of_birth


    @property
    def age (self):
        today = date.today()
        return (
            today.year
            - self._date_of_birth.year
            - (
                (today.month, today.day)
                < (self._date_of_birth.month, self._date_of_birth.day)
            )
        )


def is_over_18(func):
    def wrapper(user:User):
        age = user.age
        if age < 18:
            raise ValueError (f"User is under age. Current age: {age}")
            
        print(f"User is over 18. Current age: {age}")
    return wrapper

@is_over_18
def validate_age(user):
    pass

user1 = User(date(1994,7,12))
user2 = User(date(2016,4,25))

try:
    validate_age(user1)
    validate_age(user2)
except ValueError as ex:
    print(ex)