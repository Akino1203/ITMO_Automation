def task_1(a: int, b: float, c: str, d: list, e: bool):
    a = 4
    print(a, "относится к типу", type(a))

    b = 22.3
    print(b, "относится к типу", type(b))

    c = 'cool'
    print(c, "относится к типу", type(c))

    d = ['aaa', 'bb', 'ccc']
    print(d, "относится к типу", type(d))

    e = True
    print(e, "относится к типу", type(e))

    return a, b, c, d, e


def task_2():
    print("a=[0:3] = ", a[0:3])
    return (a = [1, 2, 3, 5, 8, 13, 21])
task_2()


def my_function(number1: int, number2: int) -> int:
    return number1 ** 2
my_function()