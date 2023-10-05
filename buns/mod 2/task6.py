domain = input()
dot = 0

for char in domain:
    if char == '.':
        dot += 1

current_domain = ""
for char in reversed(domain):
    if char == '.':
        print(current_domain[::-1])
        current_domain = ""
        dot -= 1
    else:
        current_domain += char

print(current_domain[::-1])