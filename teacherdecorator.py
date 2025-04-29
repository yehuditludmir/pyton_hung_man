from Client import getCookie
from game import playGame
from regidtr_login import login
def my_decorator1(func):
    def wrapper(*args, **kwargs):
        print("Before")

        # if name == "Sara":
        return func(*args, **kwargs)

    # else:
    return wrapper
    #     print("Error")
    # print("After")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("you start")
        r = func(*args, **kwargs)
    return wrapper


# @my_decorator
def check(o):
    if o == 'Not found cookie':
        return login()
    return playGame()



def decorator(func):
    def wrapper(*args):
        print("x")
        return func(*args)

    return wrapper


@my_decorator1
def say_hello(name):
    print(f"Hello {name}!")


@my_decorator1
def h(x):
    print(x)


@decorator
def a(z):
    print(z)
    print("aaaaaa")


check(getCookie())
