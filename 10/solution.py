with open("input.txt", "r") as f_r:
    with open("output.txt", "w") as f_w:
        mouth_365 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        file_info = f_r.read().splitlines()

        now_date = file_info[0].split(".")
        now_date_s = 0
        for l_1 in range(int(now_date[1]) - 1):
            now_date_s += mouth_365[l_1]
        now_date_s += int(now_date[0])

        cells = int(file_info[1])

        work_file = file_info[2:]
        for i in range(cells):
            el = work_file[i].split()
            date = el[1].split(".")
            date_sum = 0

            for l_2 in range(int(date[1]) - 1):
                date_sum += mouth_365[l_2]
            date_sum += int(date[0])

            if now_date_s - date_sum > 3:
                f_w.write(f"{el[0]}\n")
