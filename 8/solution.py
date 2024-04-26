with open("input.txt", "r") as f:
    with open("output.txt", "w") as f_2:
        steps = f.read().splitlines()
        if len(steps) == 365:
            a = 28
        elif len(steps) == 366:
            a = 29
        mouth_365 = [31, a, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mof = 0
        for days in mouth_365:
            summa = 0
            for i in range(mof, mof + days):
                summa += int(steps[i])
            print(summa / days)
            f_2.write(f"{summa / days}\n")
            mof += days
