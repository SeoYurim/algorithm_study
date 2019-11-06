n, k = map(int, input().split())

c_value = []
total_val = []

for i in range(1, k+1):
    total_val.append(100001)
total_val[0] = 0

for i in range(n):
    c_value.append(int(input()))

for i in range(n):
    for j in range(c_value[i], k+1):
        m = min(total_val[j-c_value[i]] + 1, total_val[j])
        total_val.insert(j, m)
print(m)
if total_val[k] == 100001:
    total_val[k] = -1
else:
    print(total_val[k])