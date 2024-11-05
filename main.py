class Calculator:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = True
            return super().__new__(cls)

    def __init__(self):
        self.command_flag = None

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiple(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return "Ошибка. Деление на 0 не допустимо." if y == 0 else x / y

    def run(self):
        while self.command_flag != 0:

            val1, val2 = map(int, input("Введите два числа через пробел: ").split())

            print("-" * 18)
            print("1. +")
            print("2. -")
            print("3. :")
            print("4. x")
            print("0. Выход")
            command = int(input("Выберите действие: "))

            if command == 0:
                break
            elif command == 1:
                print(self.add(val1, val2))
            elif command == 2:
                print(self.subtract(val1, val2))
            elif command == 3:
                print(self.divide(val1, val2))
            elif command == 4:
                print(self.multiple(val1, val2))


cal = Calculator()
cal.run()