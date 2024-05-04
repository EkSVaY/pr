with open ('input(6).txt', 'r') as f_r:
    s = f_r.read().splitlines()
    with open ('input(6).txt', 'w') as f_w:
        for i in range(len(s)):
            if s[i] != "100":
                f_w.write(f'{s[i]}\n')
