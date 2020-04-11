import re 

flag_hex_reached = False
with open("text.txt") as f:
    for line in f:
        line  = line.strip()
        if flag_hex_reached or line.startswith("Hex"):
            flag_hex_reached = True
            # x = re.search(r"[A-Za-z0-9]+ [A-Za-z0-9]*", line)
            # print(x.string) [x for x in strings if x]
            x = re.sub("\s\s", "_", line)
            print([i for i in x.split("_") if i])