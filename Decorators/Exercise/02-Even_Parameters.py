def even_parameters(func):
    def wrapper(*args):
        for arg in args:
            try:
                if not arg % 2 == 0:
                    return "Please use only even numbers!"
            except:
                return "Please use only even numbers!"

        return func(*args)

    return wrapper
