def tags(tag):
    def add_tag(f):
        def wrapper(*args):
            return f"<{tag}>{f(*args)}</{tag}>"

        return wrapper
    return add_tag
