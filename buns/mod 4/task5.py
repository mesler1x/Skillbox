filename = input("Введите имя файла: ")
with open(filename, 'r') as file:
    data = file.read()
statistics = {}
for char in data:
    if char.isalpha():
        if char in statistics:
            statistics[char] += 1
        else:
            statistics[char] = 1
sorted_statistics = sorted(statistics.items(), key=lambda x: x[1])
output_filename = "result.txt"
with open(output_filename, 'w') as output_file:
    for item in sorted_statistics:
        output_file.write(f"{item[0]}: {item[1]}\n")