def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase
def say_hello():
    return "hello, world"


print(say_hello())  # Вывод: "HELLO, WORLD"

def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if user == "admin":
            return func(user, *args, **kwargs)
        else:
            print("Access denied")
    return wrapper


@require_admin
def delete_database(user):
    print("Database deleted!")


# Проверка
delete_database("admin")   # Database deleted!
delete_database("user1")   # Access denied
