def decorator(func):
    def this_is_decorator():
        print("Это декоратор")
        func()

    return this_is_decorator


# некоторые функции

def my_name():

    print('Саша')


def friends_name():
    print('Федя')


my_name()
friends_name()


# а сейчас тоже самое, с декоратором

@decorator
def my_name():
    print('Саша')


@decorator
def friends_name():
    print('Федя')


my_name()
friends_name()
