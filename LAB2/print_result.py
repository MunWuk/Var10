def print_result(func):
    def write(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(result, list):
            for item in result:
                print(item)
        if isinstance(result, dict):
            for key, var in result.items():
                print(f'{key} = func{var}')
        else:
            print(result)
        return result

    return write()




