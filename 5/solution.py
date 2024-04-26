with open("input.txt", "r", encoding="utf-8") as file:
    with open("output.txt", "w", encoding="utf-8") as file_2:
        numbers = file.read().splitlines()
        try:
            result = (int(numbers[0]) / int(numbers[1])) + int(numbers[2])
        except ValueError:
            file_2.write("data error")
        except ZeroDivisionError:
            file_2.write("division by zero")
        else:
            file_2.write(str(result))