index = 0
s = "mind the gap!"
while index < len(s) and s[index] != "n":
    index += 1
print(s[:index])
