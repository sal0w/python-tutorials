lines = []
with open("text.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            lines.append(line)
print(lines)
# for line in lines:
#     print(line)
        