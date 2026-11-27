def file_split(file, n):
    with open(file, encoding="utf-8") as f:
        lines = f.readlines()
    sp_size = -(-len(lines) // n)
    for sp_cnt in range(n):
        with open(f"{sp_cnt:02d}.txt", "w", encoding="utf-8") as g:
            g.writelines(lines[sp_cnt * sp_size:(sp_cnt + 1) * sp_size])
            
file_split("popular-names.txt", 10)