def type_check(t):
    def check_accepts(f):
        def wrapper(arg):
            if type(arg) == t:
                return f(arg)
            else:
                return "Bad Type"

        return wrapper
    return check_accepts