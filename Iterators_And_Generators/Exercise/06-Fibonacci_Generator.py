def fibonacci():
    num = 0
    num2 = 1
    while True:
        yield num
        num3 = num
        num += num2
        num2 = num3
