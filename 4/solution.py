with open("input.txt", "r", encoding="utf-8") as file:
    with open("output.txt", "w", encoding="utf-8") as file_2:
        for i in file.readlines():
            if len(i) - 1 > 20:
                file_2.write(i)