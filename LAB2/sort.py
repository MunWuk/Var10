data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
if __name__ == '__main__':
    # Решение без lambda-функции
    def key_function(x):
        return abs(x)


    result = sorted(data, key=key_function, reverse=True)
    print(result)

    # Решение с lambda-функцией
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)