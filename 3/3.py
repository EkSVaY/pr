with open("input.txt", "r", encoding="utf-8") as file:
    with open("output.txt", "w", encoding="utf-8") as file_2:
        string = ""
        for x in file.readlines():
            string += x[0]
        file_2.write(string)
