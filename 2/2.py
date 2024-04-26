with open("input.txt", "r", encoding="utf-8") as file:
    sting = file.readlines()
    with open("output.txt", "w", encoding="utf-8") as file_2:
        for i in range(len(sting)):
            if sting[i][0] == "a" or sting[i][0] == "A":
                file_2.write(sting[i])