
user_logged_in = False


def requires_login(func):
    def wrapper(value):
        user_logged_in = value 
        if not user_logged_in:
            raise PermissionError ("User not authenticated")
        
        func(value)

    return wrapper

@requires_login
def view_profile(value:bool):
    print("Showing user's profile")

try:
    view_profile(1)
    view_profile(0)
except PermissionError as ex:
    print(ex)