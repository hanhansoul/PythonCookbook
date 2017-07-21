filename = "input"

s = set()
cnt = 0
with open(filename, 'r', encoding='UTF-8') as f:
    for line in f:
        if line not in s:
            s.add(line)
        else:
            cnt += 1
            print(line)

print(len(s))
