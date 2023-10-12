def t(m):
    for i in range(len(m)):
        for j in range(i, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m


n = int(input())
mat = []
for i in range(1, n+1):
    mat.append([i for i in range(1, n + 1)])

for line in mat:
    print(line)
print()
for line in t(mat):
    print(line)