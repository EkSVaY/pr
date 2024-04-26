with open("input.txt", "r", encoding="utf-8") as file:
    sting = file.read().upper()
    with open("output.txt", "w", encoding="utf-8") as file_2:
        file_2.write(sting)