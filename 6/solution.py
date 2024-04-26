with open("input.txt", "r", encoding="utf-8") as file:
    with open("output.txt", "w", encoding="utf-8") as file_2:
        numbers = file.read().splitlines()
        try:
            int(numbers[0])
        except ValueError:
            file_2.write("ERROR")
        else:
            if len(numbers) - 1 == int(numbers[0]):
                file_2.write("YES")
            else:
                file_2.write("NO")
