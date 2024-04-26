import os

os.mkdir(f"simple")
with open("input.txt", "r") as f_r:
    with open("simple\output.txt", "w") as f_w:
        read = f_r.readlines()
        for i in range(0, len(read), 2):
            f_w.write(read[i])
